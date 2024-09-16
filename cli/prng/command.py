import click
from cli.prng.main import generate_prng

@click.command()
@click.argument('prng_type', type=click.Choice(['bytes', 'int', 'uuid']))
@click.option('--size', default=16, help='Size in bytes for the "bytes" type.')
@click.option('--min', default=0, help='Minimum value for the "int" type.')
@click.option('--max', default=100, help='Maximum value for the "int" type.')
@click.option('--encoding', default='hex', help='Encoding for the "bytes" type.')
def prng(prng_type, size, min, max, encoding):
    """Generates pseudo-random data based on the provided type."""
    try:
        result = generate_prng(prng_type, size, min, max, encoding)
        click.echo(result)
    except ValueError as e:
        click.echo(f"Error: {e}")
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
