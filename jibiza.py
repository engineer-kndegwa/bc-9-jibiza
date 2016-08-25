import cmd
import click
import utils
from firebase import firebase_data
import ui
import warnings

warnings.filterwarnings("ignore")

ui.header()
ui.menu()


class JibizaApp(cmd.Cmd):
    prompt = click.style("Ask@Jibiza>>", fg='white', bg='cyan', bold=True)

    def do_allquizzes(self, *args):  # ok
        '''This funcion gets all the lists within the Application'''
        try:
            click.secho("{:>40}".format('AVAILABLE QUIZZES.'),
                        fg='yellow', bold=True)  # formats appearance of the quizzes
            for quiz in utils.local_quizzes():
                click.secho("_" * 75, fg='cyan')
                click.secho(" Quiz Title: " + str(quiz.title()),
                            fg='yellow', bold=True)
                click.secho("_" * 75, fg='cyan')
        except:
            pass

    def do_showlibraryquizzes(self, *args):  # ok
        '''This funcion gets all the lists within the Library'''
        try:
            click.secho("{:>40}".format('LIBRARY QUIZZES.'),
                        fg='yellow', bold=True)
            for quiz in utils.library_quizzes():
                click.secho("_" * 75, fg='cyan')
                click.secho(" Quiz Title :" + str(quiz.title()),
                            fg='yellow', bold=True)
                click.secho("_" * 75, fg='cyan')
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
        '''This function should download a quiz from firebase'''
        try:
            utils.download_quiz(quiz_name)
        except:
            pass

    def do_uploadquiz(self, quiz_name):
        '''This function should upload a quiz to firebase'''
        try:
            utils.upload_quiz(quiz_name)
        except:
            pass

    def do_clr(self, arg):
        '''This function should upload a quiz to firebase'''
        click.clear()
        ui.title_jibiza()
        ui.welcome_message()

    def do_help(self, arg):
        '''This function should show a table with all the commands'''
        ui.help_screen()
        ui.persistent_menu()

    def default(self, arg):
        pass

    def do_EOF(self, line):
        return True


if __name__ == "__main__":
    try:
        JibizaApp().cmdloop()
    except KeyboardInterrupt:
        print("Bye!")
