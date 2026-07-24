# Study Buddy - Rule-Based Chatbot (Python)

## Overview

Study Buddy is a simple rule-based chatbot built using Python. It greets the user based on the current time of the day and answers a few predefined questions related to studies and motivation. The chatbot uses Python dictionaries and conditional statements to provide responses.

This project is suitable for beginners who want to learn:

* Python basics
* Dictionaries
* Functions
* Loops and conditional statements
* User input handling
* Simple chatbot development

## Features

* Greets the user according to the current time.
* Accepts the user's name.
* Answers basic predefined questions.
* Provides motivational and study-related responses.
* Runs continuously until the user types `bye`.
* Uses a rule-based approach for generating responses.

## Technologies Used

* Python 3
* datetime module
* time module

## Supported Questions

The chatbot can answer questions such as:

* `hello`
* `how are you`
* `what is ai`
* `who are you`
* `motivate me`
* `sorry`
* `thanks`
* `bye` (to exit the chatbot)

> Note: The chatbot only responds to predefined questions. Any unknown question will return a default response.

## Project Structure

```text
Study-Buddy/
│
├── chatbot.py
└── README.md
```

## How to Run

1. Install Python 3 on your system.
2. Save the program as `chatbot.py`.
3. Open your terminal or command prompt.
4. Navigate to the project folder.
5. Run the following command:

```bash
python chatbot.py
```

## Example Output

```text
Welcome, Enter your name: Vrishabh

Good Morning

Namaste! Welcome to Study Buddy.
You can ask me basic questions.
Type 'bye' to exit the chatbot.

Ask me something: hello
Bot: Hi, How can I help you?

Ask me something: what is ai
Bot: AI means Artificial Intelligence.

Ask me something: motivate me
Bot: Quantity in hard work but quality in execution.

Ask me something: bye
Bot: Goodbye! Keep studying.
```

## Future Improvements

Some features that can be added in future versions include:

* More question-and-answer pairs.
* File-based memory storage.
* Voice input and output.
* Graphical User Interface (GUI) using Tkinter.
* Integration with APIs for intelligent responses.
* Natural Language Processing (NLP) support.

## Learning Outcomes

By building this project, you will understand:

* How rule-based chatbots work.
* How dictionaries can be used for storing responses.
* How to use loops for continuous interaction.
* How to organize Python programs using functions.
* Basic user interaction in command-line applications.

## Author

**Vrishabh VD**

A beginner-friendly Python project created for learning chatbot fundamentals and problem-solving using Python.
