# Disaster-Response-Project
### Introduction
this project is part of udacity's nano degree in data science.
in this project we where asked to clean the dataset using ETL then build a ML model.


### Summary
This project is set to make identifying the people in need and providing them with the proper resourses during disasters, Faster and easier by Building ML model that classifiy each comming message from diffrent sources to specifec well descriped Category.
This Disaster Response System has been built by gathring Tweets provieded By Udacity and training the model on learning the features of each category.

### Instructions:


1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
        
        
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`
        
        

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

### Deployment
Here we See the home page of the dashboard that has a navgition bar and the message box followed by few graphs to conclude the findings:

![BaselGithub1](https://user-images.githubusercontent.com/93598105/148646343-9f0fe3c6-31d3-4056-8d88-e848a66d7d3c.PNG)

Next , after writing a message in the message box the app takes you to the next page where it shows the results after the classifer has classifed the input message to diffrent categories:

![BaselGithub2](https://user-images.githubusercontent.com/93598105/148646326-65532084-3ec4-4a28-b0e0-0b1732e4bda9.PNG)

Here are exapmle of how the results show:
![BaselGithub3](https://user-images.githubusercontent.com/93598105/148646353-c682d64c-8e95-48d3-9233-cb60ab63aae9.PNG)

### Licencse
All the content has been provieded by Udacity as part of the Data Scientist Nanodgree.
