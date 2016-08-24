import cmd
import click
import utils
import sys
import urllib3
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from firebase import firebase_data
urllib3.disable_warnings()

click.clear()
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
cprint(figlet_format('JIBIZA', font='univers'),
       'white', 'on_red', attrs=['bold'])

with click.progressbar(range(20000),
                       label="Loading Jibiza...",
                       fill_char=click.style('#',
                                             fg='red', bg='black')) as prog_bar:
    for i in prog_bar:
        pass


class JibizaApp(cmd.Cmd):
    prompt = "(Jibiza)> "

    def do_allquizzes(self, *args):  # ok
        '''This funcion gets all the lists within the Application'''
        try:
            for quiz in utils.local_quizzes():
                click.echo(quiz)
        except:
            pass

    def do_libraryquizzes(self, *args):  # ok
        '''This funcion gets all the lists within the Library'''
        try:
            for quiz in utils.library_quizzes():
                click.echo(quiz)
        except:
            pass

    def do_importquiz(self, quiz_file):  # ok
        '''This function imports a quizz from a JSON File'''
        utils.import_quiz(quiz_file)

    def do_takequiz(self, quiz_file):
        '''This function allows the user to take a quiz'''
        try:
            utils.attempt_quiz(quiz_file)
        except:
            pass

    def do_getonlinequizzes(self, args):
        '''This function downloads a quiz to the local repo'''
        try:
            firebase_data()
        except:
            pass

    def do_uploadquiz(self, upload_quiz):
        '''This function should upload a quiz to firebase'''

    def do_showdifferences(self, differences):
        '''This function should be able to show you the differences \
        between your local and online store'''
        pass

    def do_sync(self, sync):
        '''This should sync'''
        pass

    def default(self, arg):
        pass


if __name__ == "__main__":
    try:
        JibizaApp().cmdloop()
    except KeyboardInterrupt:
        print("Bye!")
