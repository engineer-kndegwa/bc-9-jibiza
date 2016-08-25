import click
import sys
import time
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from tabulate import tabulate
# ui section


def title_jibiza():
    click.secho('=' * 75, fg='cyan')
    click.secho('*' * 75, fg='yellow')
    click.secho('=' * 75, fg='cyan')
    init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
    cprint(figlet_format('JIBIZA', font='poison'),
           'cyan', attrs=['bold'])
    click.secho('=' * 75, fg='cyan')
    click.secho('*' * 75, fg='yellow')
    click.secho('=' * 75, fg='cyan')


def welcome_message():
    click.secho(
        """
=====================WELCOME====================
QUICK GUIDE:
1.allquizzes - list all
2.showonlinequizzes - list all online
3.showlibraryquizzes - list all in separate path
4.downloadquiz <quiz_name>
5.takequiz <quiz_name> 
************************************************
TYPE HELP ANYTIME TO VIEW HELP SECTION
================================================
    """, bold=True, fg="yellow")


def header():
    click.clear()
    title_jibiza()
    click.echo(' ' * 60)
    click.echo(' ' * 60)
    with click.progressbar(range(200000),
                           label=click.secho(
                               '\t\t\t\tLOADING JIBIZA ...', blink=True, bold=True),
                           fill_char=click.style('  ', bg='cyan')) as prog_bar:
        for i in prog_bar:
            pass
    with click.progressbar(range(200000),
                           label=click.secho(
                               '\t\t\t\tLOADING QUIZZES ...', blink=True, bold=True),
                           fill_char=click.style('  ', bg='red')) as prog_bar:
        for i in prog_bar:
            pass
    with click.progressbar(range(200000),
                           label=click.secho(
                               '\t\t\t\tPREPARING TERMINAL ...', blink=True, bold=True),
                           fill_char=click.style('  ', bg='white')) as prog_bar:
        for i in prog_bar:
            pass
    with click.progressbar(range(200000),
                           label=click.secho(
                               '\t\t\t\tFINALIZING ...', blink=True, bold=True),
                           fill_char=click.style('  ', bg='green')) as prog_bar:
        for i in prog_bar:
            pass
    click.secho("{:>40}".format('DONE!'), bold=True, fg='yellow')


def menu():
    time.sleep(1)
    table = [["allquizzes", 'No Arguments', '\'allquizzes\' returns a list of all locally imported quizzes to the app.', "allquizzes"],
             ["importquiz", '<quiz_name>',
                 "\'importquiz\' imports a quiz from the local library. ", "importquiz olympics"],
             ["takequiz", '<quiz_name>',
                 "\'takequiz\' allows a user to attempt a quiz and get a score based on answers given.", "takequiz olympics"],
             ["help", 'No Arguments',
                 "\'help\' help section to decode terms and how they are used in Jibiza App.", "help"]
             ]
    headers = ["COMMAND", "ARGUMENT", "DETAILS", "EXAMPLE USE"]
    click.secho(tabulate(table, headers, tablefmt="grid"),
                fg='cyan', bold=True)
    time.sleep(6)
    click.clear()
    title_jibiza()
    welcome_message()


def help_screen():
    click.clear()
    click.secho('~' * 50, fg='cyan')
    click.secho('~' * 50, fg='cyan')
    click.secho('WELCOME TO THE HELP SECTION.', bold=True, fg='cyan')
    click.secho('Definition of terms.', fg='yellow', bold=True)
    def_terms = """
    1. Local Quizzes - These are the available quizzes that can be taken.
    2. Library Quizzes - These are a second group of quizzes stored on your file system
    and that are imported to your local quizzes section. This serves as a better alternative to 
    typing the full path. Online quizzes on firebase once downloaded come here.
    3. Online quizzes - These are the quizzes stored on the firebase application. Once downloaded, they go to the library.
    """
    click.secho(def_terms, fg='yellow')
    click.secho('~' * 50, fg='cyan')
    click.secho('~' * 50, fg='cyan')


def persistent_menu():
    time.sleep(1)
    table = [["allquizzes", 'No Arguments', '\'allquizzes\' returns a list of all locally imported quizzes to the app.', "allquizzes"],
             ["importquiz", '<quiz_name>', "\'importquiz\' imports a quiz from the local library. ", "importquiz olympics"],
             ["showlibraryquizzes", 'No Arguments', "lists all the quizzes in the library that need be imported before use.",'showlibraryquizzes'],
             ["showonlinequizzes", 'No Arguments', "lists all the quizzes on firebase that need be downloaded before use.",'showonlinequizzes'],
             ["takequiz", '<quiz_name>', "\'takequiz\' allows a user to attempt a quiz and get a score based on answers given.", "takequiz olympics"],
             ["downloadquiz", '<quiz_name>',"This allows you to download a quiz from firebase.", "downloadquiz beginner"],
             ["uploadquiz", '<quiz_name>',"This allows you to upload a quiz to firebase.", "downloadquiz beginner"],
             ["help", 'No Arguments',"\'help\' help section to decode terms and how they are used in Jibiza App.", "help"]
             ]
    headers = ["COMMAND", "ARGUMENT", "DETAILS", "EXAMPLE USE"]
    click.secho(tabulate(table, headers, tablefmt="grid"),
                fg='cyan', bold=True)

