# Dog-Chatbot
A chatbot that acts like a dog and tells you dog facts!

## Introduction:
Welcome to “Squeakers” the dog chat bot! Squeakers has a lot of love and knowledge for dogs.
Squeakers remembers your favorite dog breeds and all the dog breeds that you asked questions about. 
You can also ask Squeakers to teach you a trick! Squeakers will remember the tricks that you guys have learned together. 
Furthermore, you can ask Squeakers specific information (grooming, markings, color, diet, etc.) about any dog breed (golden retrievers, corgis, poodles, terriers, hounds, etc.)

## Getting Started:
There are two .py files you have to run in the command line for the project to work.
First, run    `python training.py`
	This trains the chatbot using neural networks.
Then, run   `python chatbot.py`
	Squeakers will ask you for your username, and from there you can chat!
*If there is some dependency missing that prevents a successful compile, please run `npm install <dependency name>`. 
I don’t think you should have to do this, but I don’t particularly remember if I installed anything first so please help me out here with a possible npm installation or two. 

## System Description and Logic:
The chatbot is trained on an intents.json file using neural networks. The intents.json file has the following format:

![image](https://user-images.githubusercontent.com/43458707/166195282-3aa7f915-49f1-4054-948d-751bd358b54b.png)


There are many tags, each indicating a possible thing that the user could want to ask or indicate. For example, all of the 
responses above like “hello”, “hey”, “hi”, etc. are things that the user could say that would simply indicate a greeting. 
The responses are possible things that I would want my chatbot to respond. For some tags, there is only a single 
response (such as when the user asks about a fact). When there are multiple responses, one of them is chosen at random.

## Diagram of Logic

![image](https://user-images.githubusercontent.com/43458707/166195444-eb0badc3-42fc-413a-9982-0a2683fed7c7.png)

## Sample Dialogs
There is some excess printing going on in between the user input and chatbot response… this is due to the model.predict() method printing some extra info,
I couldn’t figure out how to get rid of it so please just ignore this :) This is a #TODO for me

![image](https://user-images.githubusercontent.com/43458707/166195512-4908fd09-11bb-45e4-a57a-17e2a8effce0.png)

I had chatted with my bot previously with the username ‘Craig’ (those chats aren’t shown, so it remembers info that isn’t shown here). This is how that went again!

![image](https://user-images.githubusercontent.com/43458707/166195549-3f5ebf4d-5436-45d8-adfe-a239876bd1c1.png)




