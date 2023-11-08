# Import necessary libraries
from flask import Flask, render_template, request
import openai

# Initialize your OpenAI API key
openai.api_key = "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"  # Replace with your OpenAI API key

# Create a Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the selected language and user's question from the form
        language = request.form.get('language')
        question = request.form.get('question')

        # Define language codes for translation
        language_codes = {
            'English': 'en',
            'Chinese': 'zh',
        }

        # Generate a response from ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Translate the following {language_codes[language]} to English: {question}",
            max_tokens=150
        )

        # Get the translated question in English
        translated_question = response.choices[0].text.strip()

        # Generate a response from ChatGPT based on the translated question
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Answer the following question: {translated_question}",
            max_tokens=150
        )

        # Get the answer from ChatGPT
        answer = response.choices[0].text.strip()

        return render_template('index.html', answer=answer)

    return render_template('index.html', answer='')

if __name__ == '__main__':
    app.run(debug=True)
