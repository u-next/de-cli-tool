import click
from utils.run_shell import run_shell


@click.command()
@click.argument("name")
def hello(name="world"):
    """
    Say hello to the user, default is 'world' \n
    Example: \n
        hello John
    """
    run_shell(f"echo Hello, {name}!")
