import click

@click.group()
def cli():
    """CLI de operaciones criptograficas"""
    pass

@cli.command()
def hello():
    """Imprime '¡Hola Mundo!'"""
    click.echo('¡Hola Mundo!!')

# cli.add_command(add)

if __name__ == '__main__':
    cli()
