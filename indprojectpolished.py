from googletrans import Translator

class TranslationSession:
    def __init__(self):
        self.translator = Translator()
        self.original_text = ""
        self.target_language = ""

    def get_text_request(self):
        self.original_text = input("Введите текст, который хотите перевести: ")

    def target_language_request(self):
        self.target_language = input("Введите код языка, на который сделать перевод(en,ru,es): ")

    def translate(self):
        try:
            result = self.translator.translate(self.original_text, dest=self.target_language)

            print("--- Результат перевода ---")
            print(f"Исходный язык: {result.src.upper()}")
            print(f"Перевод: {result.text}")
            print("-" * 26)

        except Exception as err:
            print(f"Произошла ошибка при переводе. Убедитесь, что вы ввели корректные данные.")
            print(f"Техническая информация: {err}")

    def run(self):
        print("Добро пожаловать в программу для перевода.")
        print("Для окончания сессии в любой момент введите: end_session")

        while True:
            self.get_text_request()
            if self.original_text == "end_session":
                print("Сессия завершена.")
                break

            if not self.original_text:
                print("Вы ничего не ввели. Попробуйте снова.")

            self.target_language_request()
            if self.target_language == "end_session":
                print("Сессия завершена.")
                break

            self.translate()

session = TranslationSession()

session.run()