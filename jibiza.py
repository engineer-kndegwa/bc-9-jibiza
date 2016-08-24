import cmd
import click
import utils

menu = """
===============JIBIZA================
=====================================
=====================================
"""


class JibizaApp(cmd.Cmd):
    click.clear()
    prompt = "(Jibiza)> "
    click.echo(menu)

    def do_allquizzes(self, *args): #ok
        '''This funcion gets all the lists within the Application'''
        for quiz in utils.local_quizzes():
            click.echo(quiz)

    def do_importquiz(self, quiz_file):
        '''This function imports a quizz from a JSON File'''
        utils.import_quiz(quiz_file)

    def do_takequiz(self, quiz_file):
        '''This function allows the user to take a quiz'''
        utils.attempt_quiz(quiz_file)


    def do_downloadquiz(self, download_text):
        '''This function downloads a quiz to the local repo'''
        download_text = "Download"
        click.echo(download_text)

    def do_uploadquiz(self, upload_quiz):
        '''This function should upload a quiz to firebase'''

    def do_showdifferences(self, differences):
        '''This function should be able to show you the differences \
        between your local and online store'''
        pass

    def do_sync(self, sync):
        '''This should sync'''
        pass


if __name__ == "__main__":
    try:
        JibizaApp().cmdloop()
    except KeyboardInterrupt:
        print("Bye!")
