from pyfirebase import Firebase
import click

firebase = Firebase('https://bc-9-jibiza-test.firebaseio.com/')
ref = firebase.ref('questions')
online_quizes = ref.get()

quiz_titles = []


def firebase_data():
    for quiz in online_quizes:
        quiz_titles.append(quiz)
        click.echo('> ' + quiz)
    return quiz_titles
