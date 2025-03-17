from flask import Flask, render_template, request, jsonify
import language_tool_python

app = Flask(__name__)

# Initialize grammar checker
tool = language_tool_python.LanguageTool("en-US")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_text():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data['text']

    # Perform grammar checking
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)

    # Extract grammar errors
    errors = [match.message for match in matches]

    return jsonify({
        "corrected_text": corrected_text,
        "grammar_errors": errors
    })

if __name__ == '__main__':
    app.run(debug=True)
