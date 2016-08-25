import cmd
import click
import utils
import urllib3
from firebase import firebase_data
import ui
urllib3.disable_warnings()

ui.header()
ui.menu()


class JibizaApp(cmd.Cmd):
    prompt = click.style("AskJibiza>>", fg='white', bg='cyan', bold=True)

    def do_allquizzes(self, *args):  # ok
        '''This funcion gets all the lists within the Application'''
        try:
            for quiz in utils.local_quizzes():
                click.echo(quiz)
        except:
            pass

    def do_showlibraryquizzes(self, *args):  # ok
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

    def do_showonlinequizzes(self, args):  # ok
        '''This function downloads a quiz to the local repo'''
        try:
            firebase_data()
        except:
            pass

    def do_downloadquiz(self, quiz_name):
        '''This function should downlaod a quiz to firebase'''
        try:
            utils.download_quiz(quiz_name)
        except:
            pass

    def do_help(self, option):
        '''This function should upload a quiz to firebase'''

    def default(self, arg):
        pass


if __name__ == "__main__":
    try:
        JibizaApp().cmdloop()
    except KeyboardInterrupt:
        print("Bye!")
