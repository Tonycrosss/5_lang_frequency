import re
import sys
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    lower_words = text.lower()
    words = re.findall(r'\w+', lower_words)
    words_count = 10
    counted_words = Counter(words).most_common(words_count)
    return counted_words


def print_counted_words(counted_words):
    for word, quantity in counted_words:
        print('Слово "{}" повторяется {} раз'.format(word, quantity))

if __name__ == '__main__':
    document = load_data(sys.argv[1])
    counted_words = get_most_frequent_words(document)
    print_counted_words(counted_words)
