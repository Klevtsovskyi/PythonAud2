

from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def on_receive(self, line: str):
        pass


class FileReader:

    def __init__(self, filename):
        self.filename = filename
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def send(self, line: str):
        for observer in self.observers:
            observer.on_receive(line)

    def read(self):
        with open(self.filename, encoding="utf-8") as f:
            for line in f:
                self.send(line.rstrip())


class FilePrinter(Observer):

    def on_receive(self, line: str):
        print(line)


class WordCounter(Observer):

    def __init__(self):
        self.count = 0

    def on_receive(self, line: str):
        self.count += len(line.split())

    def get_count(self):
        return self.count


class ContainsWord(Observer):

    def __init__(self, word):
        self.word = word
        self.contains = False

    def on_receive(self, line: str):
        words = line.split()
        if self.word in words:
            self.contains = True

    def get_word(self):
        return self.word

    def get_result(self):
        return self.contains


if __name__ == '__main__':
    file_reader = FileReader("input.txt")

    file_printer = FilePrinter()
    file_reader.add_observer(file_printer)

    word_counter = WordCounter()
    file_reader.add_observer(word_counter)

    contains_word_1 = ContainsWord("клас")
    file_reader.add_observer(contains_word_1)

    contains_word_2 = ContainsWord("привіт")
    file_reader.add_observer(contains_word_1)

    file_reader.read()

    print()
    print("Кількість слів у файлі: ", word_counter.get_count())

    print()
    print("Слово \"{}\" {}міститься в тексті."
          .format(contains_word_1.get_word(),
                  "" if contains_word_1.get_result() else "не "))

    print()
    print("Слово \"{}\" {}міститься в тексті."
          .format(contains_word_2.get_word(),
                  "" if contains_word_2.get_result() else "не "))
