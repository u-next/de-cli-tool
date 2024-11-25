import click
from utils.run_shell import run_shell


@click.command()
@click.argument("names", nargs=-1)
def hello(names):
    """
    Print a greeting message to the specified names \n

    \b
    示例:
      hello Alice Bob
    """
    if not names:
        names = ("DE member",)
    names_combined = ",".join(names)
    run_shell(f"echo Hello, {names_combined}!")
