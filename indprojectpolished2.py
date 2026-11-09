from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

class WebTranslationSession:
    def __init__(self):
        self.translator = Translator()

    def translate(self, original_text, target_language):
        try:
            result = self.translator.translate(original_text, dest=target_language)
            return result.text
        except Exception as err:
            return f"/Произошла ошибка при переводе: {str(err)}"

translator_instance = WebTranslationSession()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    user_text = request.form.get("text", "")

    translated_text = ""
    if user_text:
        translated_text = translator_instance.translate(user_text, target_language="en")
        print (translated_text)
    return render_template("result.html",
                           original=user_text,
                           translated=translated_text)

if __name__ == '__main__':
    app.run()

