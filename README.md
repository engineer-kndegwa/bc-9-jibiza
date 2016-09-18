[![Build Status](https://travis-ci.org/Kimanicodes/bc-9-jibiza.svg?branch=dev)](https://travis-ci.org/Kimanicodes/bc-9-jibiza)

#BC-9-JIBIZA

**A project done in fullfillment of the application process for Andela Cohort 9**

>Why Jibiza? 
Jibiza is a swahili word meaning 'answer back' as translated into English. This formed the basis for why it was the name I settled for in regards to the **Quiz Application** project that I was assigned to accomplish.

Jibiza is a ***console*** based application that should be used to present questions with multiple choice questions that need be answered 

The required commands for the application were:

Command| Argument| Explanation
--- | --- | ---
|`quiz list`| None | List of all the available quizzes in your library
|`quiz import`| `<path_to_quiz_JSON>` | Import a new quiz from a JSON file
|`quiz take` | `<quiz_name>`| Start taking a new quiz

**The following requirements were also highlighted**

1. When a user takes a quiz he gets a score based on the answers he got right

2. Timing can be added to quiz as a parameter in the JSON

3. As a user I can import quizzes from JSON files

4. Add in an online quiz repository using Firebase (extra credit)

5. List all the online quizzes

6. Download a quiz to your library

7. Publish a local quiz to the online library


> JSON Format for Quizzzes should contain the following keys: 

1. `questions` - List of questions in the quiz

2. `text` - Question text

3. `options` - List of options for the question

4. `.is_answer` - Parameter of an option that can be true or false. Indicates whether or not that option is the correct answer.

5. `quiz take <quiz_name>` - Start taking a new quiz


#Installation.

**To be able to get this project to your local machine**

1. First git clone this project at `https://github.com/Kimanicodes/bc-9-jibiza.git`

2. Navigate to the `bc-9-jibiza` folder.

3. Create a virtual environment using the `virtualenv` command and activate it.

4. Install the requirements via `pip install -r requirements.txt`

5. Run the application in your terminal via `python jibiza.py`

>Alternatively you can follow the steps through this video:

[![asciicast](https://asciinema.org/a/0fgyf129ur86y7046x6wmji6e.png)](https://asciinema.org/a/0fgyf129ur86y7046x6wmji6e?autoplay=1)


#Bugs

A few bugs were encountered during the creation of Jibiza.

1. The `uploadquiz` functionality is erratic.

2. The timer sometimes does not work as expected.(Fixed)


#Resources

1. The author @[Kimani Ndegwa](https://www.kimanindegwa.co.ke)

2. [Click Documentation](http://www.click.pocoo.org)

3. [Firebase](https://bc-9-jibiza-test.firebaseio.com/)



