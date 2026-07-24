#Chat based study buddy (mini chat bot) Rule based 

import datetime
import time

name= input("Welcome, Enter your name: ")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morining")
elif 11 <= presentHour<= 17:
    print("Good Afternoon")
elif 17<= presentHour <= 20:
    print("Good Evening")
else:
    print("Good Night,", name)




print('Namaste! welcome to study buddy')
print("You can ask me a basic question, Type 'bye' to exit from the bot")


# Chat bot memory creation [Dictionary of response]

responses = {
    'hello' : 'Hi, How can i help you?',
    'how are you' : 'I am fine , whats about you?',
    'what is AI': 'AI is artificial intelligence',
    'who are you' : ' I am study buddy a chot bot created by Vrishabh VD',
    'motivate me': 'Quantity in hardwork but quality in execution by Virat Kohli ',
    'sorry' : 'Not need to tell me accept the mistake and learn from them',
    'thanks' : 'you also',
}

# Method function to get Response 

def getResponseOfBout(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return " I am unable to give answer ,I will learn this "

#Take use input

while True:
    userInput = input("Please ask your question:")
    reply= getResponseOfBout(userInput)
    print('Bot Response:',reply)

    if "bye" in userInput.lower():
        break



