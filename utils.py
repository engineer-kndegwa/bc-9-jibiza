import os
import json
import click
import time
from Questions.questions import QuestionStructure
from shutil import copyfile
from tabulate import tabulate


def local_quizzes():
    '''This function lists all the files within the directory'''
    try:
        a = os.listdir('Questions/json')
        quizzes = [file.replace('.json', '') for file in a]
        return quizzes  # Add styles here
    except FileNotFoundError:
        os.mkdir('Questions/json')
        return []


def load_quiz(quiz_file):
    try:
        filename = 'Questions/json/' + quiz_file + '.json'
        fl = open(filename).read()
        f = json.loads(fl)
        f2 = f['name']
    except IOError or FileNotFoundError:
        return 'That file is not within your local repository.'
    return f2


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
    if the_quiz_file == "":
        click.echo('That File doesnt exist')
    quiz_dets = get_quiz_details(the_quiz_file)
    questions = quiz_dets['questions']
    time_given = quiz_dets['time_allocated']  # countdown timer
    responses = []
    begin = time.time()
    game_over = False
    '''Get Through each question from the json file'''
    for q in questions:
        if time.time() - begin > time_given:
            game_over = True
            break
        click.echo(q.combine_string())
        answer_provided = input("Enter Ans>>: ")
        responses.append(q.check_answer(answer_provided))
        if responses[-1] is False:
            click.echo('WRONG!')
        else:
            click.echo('RIGHT!')
        input("Press enter to proceed to the next question.")

    performance = int(responses.count(True) / len(questions) * 100)
    if game_over:
        return 'Times Up!'
    table = [['Questions Attemted', len(responses)],
             ['Passed', responses.check_answer(True)],
             ['Failed', responses.check_answer(False)],
             ['performance', performance]
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


