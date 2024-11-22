import click
import subprocess


def run_shell(command):
    try:
        result = subprocess.run(
            command, text=True, shell=True, capture_output=True, check=True
        )
        click.echo(result.stdout)
    except subprocess.CalledProcessError as e:
        click.echo(f"Command failed: {e.stderr}", err=True)


if __name__ == "__main__":
    run_shell("echo \"Hello, world!\"")
