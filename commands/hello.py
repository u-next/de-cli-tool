import click


@click.command()
@click.argument("name")
def hello(name="world"):
    """
    Description: Say hello to someone \n
    Usage: hello <NAME: str> \n
    Default: Hello, world! \n
    """
    click.echo(f"Hello, {name}!")
