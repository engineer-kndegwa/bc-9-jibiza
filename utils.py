from __future__ import division
import os
import json
import click
import time
from Questions.questions import QuestionStructure
from shutil import copy2
from tabulate import tabulate
from pyfirebase import Firebase
import warnings

warnings.filterwarnings("ignore")


def local_quizzes():  # good to go
    '''This function lists all the files within the local scope directory'''
    try:
        a = os.listdir('Questions/json')
        quizzes = [file.replace('.json', '') for file in a]
        return quizzes  # Add styles here
    except FileNotFoundError:
        os.mkdir('Questions/json')
        return []


def library_quizzes():  # library quizzes
    '''This function lists all the files within the library'''
    try:
        a = os.listdir('library/')
        ex_quizzes = [file.replace('.json', '') for file in a]
        return ex_quizzes  # Add styles here
    except FileNotFoundError:
        os.mkdir('library/')
        return []


def import_quiz(quiz_file):  # working
    '''The first step that creates a and b 
    lists the files within the directory'''
    a = os.listdir('library/')  # list the files in the library
    extra_quizzes = [file.replace('.json', '')for file in a]

    b = os.listdir('Questions/json')  # list the files in the Questions/json
    quizzes = [file.replace('.json', '') for file in b]

    dst = os.path.join(os.path.abspath('.'), 'Questions/json')
    src_path = os.path.join(os.path.abspath('.'), 'library/')
    # creates an absolute path for shutils
    try:
        # check all quizzes within the extra quizzes string
        for quiz in extra_quizzes:
            if quiz not in quizzes:
                # confirm first if it exists within our quizzes listed in
                # Questions/json folder
                src = os.path.join(src_path, quiz + '.json')
                copy2(src, dst)
                click.secho("=" * 45, fg='green')
                click.secho("=" * 45, fg='green')
                click.secho(
                    "Quiz import successful!Proceed to take quiz.", fg='green')
                click.secho("=" * 45, fg='green')
                click.secho("=" * 45
                    , fg='green')
                break
        else:
            click.secho("=" * 45, fg='red')
            click.secho("=" * 45, fg='red')
            click.secho('ERROR: That File already Exists', bg='red')
            click.secho("=" * 45, fg='red')
            click.secho("=" * 45, fg='red')
    except IOError as e:
        click.secho('That file is not within your library.', bg='red')
        raise e
    return quizzes, extra_quizzes  # return both for purposes of reassignment


def get_quiz_details(the_quiz_file):
    """Gets json file from folder Questions on file system and loads it"""
    quiz_path = 'Questions/json/' + the_quiz_file + '.json'
    quiz_file = open(quiz_path, 'r').read()
    the_quiz = json.loads(quiz_file)
    time_allocated = int(the_quiz["time_allocated"])  # get time allocated
    quiz_breakdown = []
    for q in the_quiz['questions']:
        t = q['q_text']
        a = q['is_answer']
        options = q['options']
        quiz_breakdown.append(QuestionStructure(t, a, options))
    return {"time_allocated": time_allocated, "questions": quiz_breakdown}


def attempt_quiz(the_quiz_file):
    """ This function is the main function that allows user to
        attempt the question. 
    """
    try:
        if the_quiz_file == "":
            click.echo('That File doesnt exist')
    except IOError:  # exception if file does not exist
        click.echo('File doesnt exist')
    correct_count = 0  # create a correct answer counter
    wrong_count = 0  # create a wrong answer counter

    quiz_dets = get_quiz_details(the_quiz_file)  # get quiz details
    questions = quiz_dets['questions']
    time_given = quiz_dets['time_allocated']
    responses = []  # store the responses gotten in a list
    begin = time.time()  # set start or begin time
    game_over = False  # in case you dont't make it in time
    '''Get Through each question from the json file'''
    for q in questions:
        if time.time() - begin > time_given:
            game_over = True
            break
        click.echo(q.combine_string())
        answer_provided = raw_input("Enter Ans>>: ")
        print(answer_provided)
        responses.append(q.check_answer(answer_provided))
        if responses[-1] is False:
            click.echo('WRONG!')
            wrong_count += 1
        else:
            click.echo('RIGHT!')
            correct_count += 1
        raw_input("Press enter to proceed to the next question.")
    if game_over:
        return 'Times Up!'

    performance = (float(correct_count) / len(questions) * 100)
    # tabulate the results
    table = [['Time Allocated', time_given],
             ['Questions Attempted', len(responses)],
             ['Performance in %', performance],
             ['Correct Answers', correct_count],
             ['Wrong Answers', wrong_count],

             ]
    click.echo(tabulate(table))


def download_quiz(quiz_name):
    '''
    This function downloads quiz data from firebase.
    '''
    a = Firebase('https://bc-9-jibiza-test.firebaseio.com/')
    ref = a.ref('questions/' + quiz_name)
    quiz_gotten = ref.get()
    quiz_path = 'library/' + quiz_name + '.json'
    with open(quiz_path, 'w') as open_file:
        json.dump(quiz_gotten, open_file)
        click.secho('QUIZ DOWNLOAD SUCCESSFUL!', bold=True, fg='yellow')


def countdown(t):
    '''Time out counter.'''
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}'.format(secs)
        click.echo(timeformat + '\t')
        time.sleep(1)
        t -= 1
        if t == 0:
            click.echo('TIMES UP!')
            break
