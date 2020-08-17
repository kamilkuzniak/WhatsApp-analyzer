WhatsApp Analyser
-------------------
This script allows for the analysis of WhatsApp chats with any number of participants.
Additionally, a simple machine learning model has been utilized (naive Bayes) 
to try to predict the author of the message based on its content.
#### Calculated metrics and plots:
* Number of words and messages sent
* Average message length
* Number of media sent
* 10 most commonly used words
* Plot of messages sent by hour/day/month
* Plot of words sent by hour/month

Installation
-------------------
* Clone this repository to your computer
* Get into the folder using cd whatsapp_analyser
* Install the required libraries using pip install -r requirements.txt
* Get into the data folder using cd data
* Put your chat file in this location 

Usage
-------------------
* Get into the folder src using cd whatsapp_analyser/src
* Run the chat_analyzer file using python chat_analyzer.py
