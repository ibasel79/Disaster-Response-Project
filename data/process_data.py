# import libraries
import sys
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

#load data into df
def load_data(messages_filepath, categories_filepath):
   
    global messages
    global categories
    global df
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages, categories)
    return df
    pass

#clean data
def clean_data(df):
    
    category_list = df["categories"].str.split(";",expand=True)
    row= category_list.iloc[0]
    words=[x[:-2] for x in row]
    category_colnames = words
    category_list.columns = category_colnames
    
   
    for column in  category_list:
          
            category_list[column] =  category_list[column].astype(str).str[-1:]
            category_list[column] =  category_list[column].astype(int)
   
    #drop unused columns then drop the dublicates
    df=df.drop(['categories','original'],axis=1)
    df = pd.concat([df,category_list],axis=1)
    df=df.drop_duplicates()
    return df
    pass

#save data and export to Data Base
def save_data(df, database_filename):
    engine = create_engine('sqlite:///'+ database_filename)
    df.to_sql('Messages', engine, index=False,if_exists='replace')
    pass  

#main function
def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
        
        
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()