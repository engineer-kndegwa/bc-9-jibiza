import click
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from blessings import Terminal
from tabulate import tabulate
# ui section
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
cprint(figlet_format('JIBIZA APP', font='starwars'),
       'white', attrs=['bold'])


def header():
    click.clear()
    init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
    cprint(figlet_format('JIBIZA APP', font='starwars'),
           'white', attrs=['bold'])
    click.echo(' ' * 60)
    click.echo(' ' * 60)
    click.echo('==' * 40)
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
                               '\t\t\t\tPREPARING CANVAS ...', blink=True, bold=True),
                           fill_char=click.style('  ', bg='white')) as prog_bar:
        for i in prog_bar:
            pass
    with click.progressbar(range(200000),
                           label=click.secho(
                               '\t\t\t\tFINALIZING ...', blink=True, bold=True),
                           fill_char=click.style('  ', bg='green')) as prog_bar:
        for i in prog_bar:
            pass
    click.echo('==' * 40)
    term = Terminal()
    print('I am ' + term.blink + 'bold' + term.blink + '!')


def menu():
    table = [["allquizzes", 'None', 'The lowercase \'allquizzes\' command returns a list of all locally imported quizzes to the app.'], ["Command", 451, 44], ["Argument", 0, 44],
             ["Value", 42, 44], ["Command", 451, 44], ["Argument", 0, 44]]
    headers = ["Command", "Argument", "Details"]
    click.secho(tabulate(table, headers, tablefmt="grid"), fg='cyan',bold=True)
