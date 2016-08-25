from __future__ import division
import os
import json
import click
import time
from Questions.questions import QuestionStructure
from shutil import copy2
from tabulate import tabulate
from pyfirebase import Firebase


def local_quizzes():  # good to go
    '''This function lists all the files within the directory'''
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
    a = os.listdir('library/')
    extra_quizzes = [file.replace('.json', '')for file in a]
    b = os.listdir('Questions/json')
    quizzes = [file.replace('.json', '') for file in b]
    dst = os.path.join(os.path.abspath('.'), 'Questions/json')
    src_path = os.path.join(os.path.abspath('.'), 'library/')
    try:
        for quiz in extra_quizzes:
            if quiz not in quizzes:
                src = os.path.join(src_path, quiz + '.json')
                copy2(src, dst)
                click.echo('Quiz import successful!')
            else:
                click.echo('Already Exists')
    except IOError as e:
        print('That file is not within your library.')
        raise e
    return quizzes, extra_quizzes


def get_quiz_details(the_quiz_file):
    """Gets json file from folder Questions on file system and loads it"""
    quiz_path = 'Questions/json/' + the_quiz_file + '.json'
    quiz_file = open(quiz_path, 'r').read()
    the_quiz = json.loads(quiz_file)
    time_allocated = int(the_quiz["time_allocated"])
    quiz_breakdown = []
    for q in the_quiz['questions']:
        t = q['q_text']
        a = q['is_answer']
        options = q['options']
        quiz_breakdown.append(QuestionStructure(t, a, options))
    return {"time_allocated": time_allocated, "questions": quiz_breakdown}


def attempt_quiz(the_quiz_file):
    try:
        if the_quiz_file == "":
            click.echo('That File doesnt exist')
    except FileNotFoundError:
        click.echo('File doesnt exist')
    correct_count = 0
    wrong_count = 0
    quiz_dets = get_quiz_details(the_quiz_file)
    questions = quiz_dets['questions']
    time_given = quiz_dets['time_allocated']
    responses = []
    begin = time.time()
    game_over = False
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
    table = [['Time Allocated', time_given],
             ['Questions Attempted', len(responses)],
             ['Performance in %', performance],
             ['Correct Answers', correct_count],
             ['Wrong Answers', wrong_count],

             ]
    click.echo(tabulate(table))


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}'.format(secs)
        click.echo(timeformat + '\t')
        time.sleep(1)
        t -= 1
        if t == 0:
            click.echo('TIMES UP!')
            break

