import random
import tkinter as tk


WORDS = {
    "apple": "яблоко",
    "house": "дом",
    "book": "книга",
    "water": "вода",
    "friend": "друг",
    "school": "школа",
    "beautiful": "красивый",
    "journey": "путешествие",
    "answer": "ответ",
    "dream": "мечта",
    "knowledge": "знание",
    "window": "окно",
    "garden": "сад",
    "weather": "погода",
    "family": "семья",
    "morning": "утро",
    "country": "страна",
    "language": "язык",
    "success": "успех",
    "adventure": "приключение",
}


class EnglishQuiz:
    """Викторина для изучения английских слов на Tkinter."""

    def __init__(self, window):
        """Настраивает окно и создаёт элементы интерфейса."""
        self.window = window
        self.window.title("English Quiz")
        self.window.geometry("500x470")
        self.window.configure(bg="#ECF0F1")
        self.window.resizable(False, False)

        self.quiz_words = []
        self.question_index = 0
        self.score = 0
        self.current_word = ""
        self.answered = False

        self.title_label = tk.Label(
            window,
            text="English Quiz",
            font=("Arial", 22, "bold"),
            bg="#ECF0F1",
        )
        self.title_label.pack(pady=10)

        self.question_label = tk.Label(
            window,
            text='Нажми «Начать игру»',
            font=("Arial", 12),
            bg="#ECF0F1",
        )
        self.question_label.pack(pady=5)

        self.word_label = tk.Label(
            window,
            text="",
            font=("Arial", 24, "bold"),
            bg="#ECF0F1",
        )
        self.word_label.pack(pady=15)

        self.option_buttons = []
        for _ in range(3):
            button = tk.Button(
                window,
                text="Вариант ответа",
                font=("Arial", 12),
                width=25,
                state="disabled",
            )
            button.pack(pady=3)
            self.option_buttons.append(button)

        self.feedback_label = tk.Label(
            window,
            text="",
            font=("Arial", 12),
            bg="#ECF0F1",
            wraplength=440,
        )
        self.feedback_label.pack(pady=5)

        self.score_label = tk.Label(
            window,
            text="Правильных ответов: 0",
            font=("Arial", 11),
            bg="#ECF0F1",
        )
        self.score_label.pack(pady=5)

        self.start_button = tk.Button(
            window,
            text="Начать игру",
            font=("Arial", 12, "bold"),
            command=self.start_quiz,
        )
        self.start_button.pack(pady=5)

        self.next_button = tk.Button(
            window,
            text="Следующий вопрос",
            font=("Arial", 12),
            command=self.next_question,
            state="disabled",
        )
        self.next_button.pack(pady=5)

    def start_quiz(self):
        """Подготавливает и запускает новую игру."""
        self.quiz_words = list(WORDS.keys())
        random.shuffle(self.quiz_words)

        self.question_index = 0
        self.score = 0
        self.answered = False

        self.start_button.config(state="disabled", text="Игра началась")
        self.next_button.config(state="disabled")
        self.show_question()

    def show_question(self):
        """Показывает текущий вопрос и три варианта ответа."""
        if self.question_index >= len(self.quiz_words):
            self.finish_quiz()
            return

        self.current_word = self.quiz_words[self.question_index]
        correct_answer = WORDS[self.current_word]

        wrong_answers = [
            translation
            for translation in WORDS.values()
            if translation != correct_answer
        ]
        options = random.sample(wrong_answers, 2)
        options.append(correct_answer)
        random.shuffle(options)

        self.question_label.config(
            text=f"Вопрос {self.question_index + 1} из {len(self.quiz_words)}"
        )
        self.word_label.config(text=self.current_word)
        self.feedback_label.config(text="")
        self.score_label.config(text=f"Правильных ответов: {self.score}")
        self.answered = False

        for button, option in zip(self.option_buttons, options):
            button.config(
                text=option,
                state="normal",
                command=lambda answer=option: self.check_answer(answer),
            )

        self.next_button.config(state="disabled")

    def check_answer(self, selected_answer):
        """Проверяет ответ и обновляет счёт."""
        if self.answered:
            return

        self.answered = True
        correct_answer = WORDS[self.current_word]

        if selected_answer == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Правильно! Отличная работа.")
        else:
            self.feedback_label.config(
                text=f"Неверно. Правильный ответ: {correct_answer}"
            )

        self.score_label.config(text=f"Правильных ответов: {self.score}")

        for button in self.option_buttons:
            button.config(state="disabled")

        self.next_button.config(state="normal")

    def next_question(self):
        """Переходит к следующему вопросу."""
        if not self.answered:
            return

        self.question_index += 1
        self.show_question()

    def finish_quiz(self):
        """Показывает итоговый результат."""
        total = len(self.quiz_words)
        percentage = self.score / total * 100 if total else 0

        self.question_label.config(text="Викторина завершена!")
        self.word_label.config(text=f"Результат: {self.score} из {total}")
        self.feedback_label.config(
            text=f"Правильных ответов: {percentage:.0f}%"
        )

        for button in self.option_buttons:
            button.config(state="disabled")

        self.next_button.config(state="disabled")
        self.start_button.config(state="normal", text="Играть снова")


def main():
    """Создаёт окно приложения и запускает главный цикл Tkinter."""
    window = tk.Tk()
    EnglishQuiz(window)
    window.mainloop()


if __name__ == "__main__":
    main()
