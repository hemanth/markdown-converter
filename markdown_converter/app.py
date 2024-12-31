from flask import Flask, request, jsonify
from flask_cors import CORS
from markitdown import MarkItDown
import tempfile
import os

def create_app(test_config=None):
    app = Flask(__name__)
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_mapping(
            SECRET_KEY='dev',
        )
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # Enable CORS for all domains on all routes
    CORS(app, resources={r"/*": {"origins": "*"}})

    md = MarkItDown()

    @app.route('/convert', methods=['POST'])
    def convert_to_markdown():
        try:
            # Check if URL is provided
            if 'url' in request.form:
                url = request.form['url']
                result = md.convert(url).text_content
                return jsonify({'markdown': str(result)})

            # Check if file is provided
            elif 'file' in request.files:
                file = request.files['file']
                # Create a temporary file to store the uploaded content
                with tempfile.NamedTemporaryFile(delete=False) as temp:
                    file.save(temp.name)
                    result = md.convert(temp.name).text_content
                os.unlink(temp.name)
                return jsonify({'markdown': result})

            else:
                return jsonify({
                    'error': 'No URL or file provided'
                }), 400

        except Exception as e:
            return jsonify({
                'error': f'Conversion failed: {str(e)}'
            }), 500

    return app
