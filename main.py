import click
from commands import hello
from commands import gke


@click.group(help="A Python-based CLI tool, for U-NEXT DE members")
def cli():
    pass


cli.add_command(hello.hello)
cli.add_command(gke.show_external_ip)

if __name__ == "__main__":
    cli()
