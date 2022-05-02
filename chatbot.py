import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
with open('user_info.json') as user_info:
    user_dict = json.load(user_info)
with open('breed_urls.json') as breed_list:
    breed_list_dict = json.load(breed_list)

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbotmodel.h5')  # The output will be numerical data


# Clean up the sentences
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


# Converts the sentences into a bag of words
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    # bow: Bag Of Words, feed the data into the neural network
    bow = bag_of_words(sentence)
    # This is the line printing the 1/1 [=====================] bullshit and idk how to get rid of that. If you, dear reader, figure it out, plsss tell me
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.4
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    if not intents_list:
        intents_list = [{'intent': "noises", 'probability': '0'}]
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result, tag


def get_breed(message):
    cleaned = clean_up_sentence(message)
    base_message = [word.lower() for word in cleaned]
    base_message_str = ''.join(base_message)
    for key in breed_list_dict:
        lower = key.lower()
        if lower in base_message_str:
            return key
    for key in breed_list_dict:
        lower = key.lower()
        for word in base_message:
            if len(word) > 4 and word in lower:
                return key
    return ""


print()
# print("You can chat with the bot now! Say 'exit' to exit.")
print("Hello there! Bark Bark! What is your username?")
username = input()
if username in user_dict:
    print(
        f"Welcome back {username}! Type 'help' to see the types of things I respond to or type 'exit' to exit.")
else:
    user_dict[username] = {}
    user_dict[username]["favorites"] = []
    user_dict[username]["breeds_searched"] = []
    user_dict[username]["tricks_learned"] = []
    print(f"Welcome {username}! I am Squeakers, a dog chatbot, with much love and knowledge for dogs! Type 'help' to see the types of things I respond to or type 'exit' to exit.")


while True:
    message = input(username + ": ")
    if message == 'help' or message == 'Help':
        print("""
        I know information about a lot of breeds! See the breed_list.txt file
        for a list of breeds that you can talk to me about.

        Here is a sample list of things I know how to respond to:
        Add corgi to the list of my favorite dogs
        Show me my favorite dogs
        What dog breeds did I ask about previously?
        Teach me a trick!
        What tricks have we learned together?
        How do I groom a golden retriever?
        Bark!
        """)
        continue

    if message == 'exit' or message == 'Exit':
        with open("user_info.json", "w") as outfile:
            json.dump(user_dict, outfile, indent=4)
        break
    ints = predict_class(message)
    res, tag = get_response(ints, intents)
    if tag == "greetings" or tag == "introduction" or tag == "noises" or tag == "my favorites" or tag == "goodbye":
        print(res)
    elif tag == "favorite":
        breed = get_breed(message)
        if breed == "":
            print("I'm sorry, I think you were trying to add a favorite breed, but I failed to recognize the breed from your message.")
        else:
            if res not in user_dict[username]["favorites"]:
                user_dict[username]["favorites"] += [breed]
                if res not in user_dict[username]["breeds_searched"]:
                    user_dict[username]["breeds_searched"] += [breed]
                with open("user_info.json", "w") as outfile:
                    json.dump(user_dict, outfile, indent=4)
                print(res)
            else:
                print("Bark! " + breed +
                      " should already be in your list of favorites!")
    elif tag == "view favorites":
        print(res, user_dict[username]["favorites"])
    elif tag == "trick":
        print("Repeat after me exactly: " + res)
        trick_response = input(username + ": ")
        if trick_response == res:
            if res not in user_dict[username]["tricks_learned"]:
                print("Great job! You've learned " + res)
                user_dict[username]["tricks_learned"] += [res]
                with open("user_info.json", "w") as outfile:
                    json.dump(user_dict, outfile, indent=4)
            else:
                print("Nice! You've already previously learned " +
                      res + " but it's always good to reinforce tricks.")
        else:
            print("Not a match! Better luck learning " + res + " next time!")
    elif tag == "view tricks":
        print(res, user_dict[username]["tricks_learned"])
    elif tag == "breeds searched":
        print(res, user_dict[username]["breeds_searched"])
    else:  # asking about specific breed information
        breed = get_breed(message)
        if breed == "":
            print("I'm sorry, I think you were trying to ask me about the " + tag +
                  " of a breed, but I failed to recognize the breed from your message.")
        else:
            if breed not in user_dict[username]["breeds_searched"]:
                user_dict[username]["breeds_searched"] += [breed]
                with open("user_info.json", "w") as outfile:
                    json.dump(user_dict, outfile, indent=4)
            replaced = res.replace("breed", breed)
            print(replaced + "fact about " + breed +
                  " ...still working on this :'( scraping the akc dog site for information didn't totally work out yet...pls go easy on me")
