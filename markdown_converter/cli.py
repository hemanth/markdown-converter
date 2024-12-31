import click
from .app import create_app

@click.group()
def cli():
    """Markdown Converter CLI"""
    pass

@cli.command()
@click.option('--host', default='0.0.0.0', help='Host to bind to')
@click.option('--port', default=5000, help='Port to bind to')
@click.option('--debug', is_flag=True, help='Enable debug mode')
def serve(host, port, debug):
    """Start the Markdown Converter server"""
    app = create_app()
    app.run(host=host, port=port, debug=debug)

def main():
    cli()

if __name__ == '__main__':
    main()
