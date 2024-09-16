import click
from cli.prng.command import prng

@click.group()
def cli():
    """CLI de operaciones criptograficas"""
    pass

@cli.command()
def hello():
    """Imprime '¡Hola Mundo!'"""
    click.echo('¡Hola Mundo!!')

cli.add_command(prng)


if __name__ == '__main__':
    cli()
