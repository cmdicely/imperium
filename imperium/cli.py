import click

@click.group()
def cli():
    pass

@cli.command()
def new_game():
    click.echo("New game!")

if __name__ == "__main__":
    cli()
