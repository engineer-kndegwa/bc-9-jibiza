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
==============WELCOME==============
**************       **************
*************START HERE************
=============        ==============
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
             ["context", 'No Arguments',
                 "\'context\' help section to decode terms and how they are used in Jibiza App.", "context"]
             ]
    headers = ["COMMAND", "ARGUMENT", "DETAILS", "EXAMPLE USE"]
    click.secho(tabulate(table, headers, tablefmt="grid"),
                fg='cyan', bold=True)
    time.sleep(6)
    click.clear()
    title_jibiza()
    welcome_message()
