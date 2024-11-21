import click
from commands import hello


@click.group()
def cli():
    """Cute CLI tool for U-NEXT DE members"""
    pass


cli.add_command(hello.hello)

if __name__ == "__main__":
    cli()
