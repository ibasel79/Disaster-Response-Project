import json
import plotly
import pandas as pd
import pickle 

import plotly.graph_objs as go
import plotly.express as px
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from plotly.graph_objs import Scatter
from plotly.graph_objs import Line

from sklearn.externals import joblib
from sqlalchemy import create_engine

app = Flask(__name__)

#tokenize
def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql_table('Messages', engine)

# load model
model = joblib.load("../models/classifier.pkl")
clf = model.set_params(n_jobs=1)

# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # TODO: Below is an example - modify to extract data for your own visuals
    
    #first graph data
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    
    #second graph data
    deaths_by_infrastructure=0
    infrastructure_disasters= 0
    for i in range (len(df)):
        if df['infrastructure_related'][i]==1 and df['death'][i]==1:
            deaths_by_infrastructure += 1
            
        if df['infrastructure_related'][i]==1 :
            infrastructure_disasters += 1 
     
    graph2_names = ['infrastructure disasters','deaths']
    graph2_values = [infrastructure_disasters,deaths_by_infrastructure]
   
    #third graph data
    floods=0
    storm=0
    fire=0
    earthquake=0
        
    for i in range (len(df)):
        if df['floods'][i]==1 :
            floods += 1 
        if df['storm'][i]==1 :
            storm += 1 
        if df['fire'][i]==1 :
           fire += 1 
        if df['earthquake'][i]==1 :
           earthquake  += 1 
   

    graph3_values=[floods,storm,fire,earthquake]
    graph3_names=['floods','storm','fire','earthquake']
    
    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
        {'data': [ Bar(x=genre_names,y=genre_counts)],'layout': {'title': 'Distribution of Message Genres','yaxis': {'title': "Count"},'xaxis': {'title': "Genre"}}},
        
        {'data': [ Bar(x=graph2_names ,y=graph2_values)],'layout': {'title': 'deaths cused by infrastructure disasters','yaxis': {'title': "Count"},'xaxis': {'title': ""}}},
          {'data': [ Bar(x=graph3_names ,y=graph3_values)],'layout': {'title': 'natural disasters occurrence','yaxis': {'title': "occurrence"},'xaxis': {'title': "disaster"}}} ]
    
      
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()