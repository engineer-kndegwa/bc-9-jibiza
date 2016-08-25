from pyfirebase import Firebase
import click

firebase = Firebase('https://bc-9-jibiza-test.firebaseio.com/')
ref = firebase.ref('questions')
online_quizes = ref.get()

quiz_titles = []


def firebase_data():
    click.secho("{:>40}".format('ONLINE QUIZZES.'),
                        fg='yellow', bold=True)
    for quiz in online_quizes:
        click.secho("_" * 75, fg='cyan')
        quiz_titles.append(quiz)

        click.secho(" Quiz Title :" + str(quiz.title()),
                            fg='yellow', bold=True)
        click.secho("_" * 75, fg='cyan')

    return quiz_titles
