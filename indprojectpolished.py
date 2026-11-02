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

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    user_text = ""
    lang = "en"

    if request.method == "POST":
        user_text = request.form.get("text", "")
        lang = request.form.get("lang", "en")

        if user_text.strip():
            translated_text = translator_instance.translate(user_text, lang)

    return render_template("indprojectinterface.html",
                           translated_text=translated_text,
                           user_text=user_text,
                           lang=lang)

if __name__ == '__main__':
    app.run()
