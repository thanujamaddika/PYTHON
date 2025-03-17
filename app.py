import language_tool_python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
tool = language_tool_python.LanguageTool("en-US")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_text():
    data = request.get_json()
    text = data.get('text', '')

    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)

    errors = [match.message for match in matches]

    return jsonify({
        "corrected_text": corrected_text,
        "grammar_errors": errors
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
