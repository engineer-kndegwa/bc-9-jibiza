import cmd
import click

menu = """
===============JIBIZA================
=====================================
==========Type start to Begin=========
"""
click.echo(menu)


class JibizaApp(cmd.Cmd):
    prompt = "(Jibiza)> "

    def do_something(self):
        click.echo(menu)


if __name__ == "__main__":
    try:
        JibizaApp().cmdloop()
    except KeyboardInterrupt:
        print("Bye!")
