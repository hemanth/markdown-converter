# Markdown Converter

A Flask-based web service to convert any document/url to Markdown.

## Installation

```bash
pip install markdown-converter
```

## Usage

### As a web service

Start the server:

```bash
markdown-converter serve
```

Options:
- `--host`: Host to bind to (default: 0.0.0.0)
- `--port`: Port to bind to (default: 5000)
- `--debug`: Enable debug mode

### API Endpoints

#### Convert URL to Markdown

```bash
curl -X POST -F "url=https://example.com" http://localhost:5000/convert
```

#### Convert File to Markdown

```bash
curl -X POST -F "file=@document.pdf" http://localhost:5000/convert
```

## Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the development server: `python -m markdown_converter.cli serve --debug`

## License

MIT License
