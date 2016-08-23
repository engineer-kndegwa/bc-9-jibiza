import cmd
import click

menu = """
===============JIBIZA================
=====================================
==========Type start to Begin=========
"""


class JibizaApp(cmd.Cmd):
    click.clear()
    prompt = "(Jibiza)> "
    click.echo(menu)


if __name__ == "__main__":
    try:
        JibizaApp().cmdloop()
    except KeyboardInterrupt:
        print("Bye!")
