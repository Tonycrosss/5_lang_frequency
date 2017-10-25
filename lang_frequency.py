import re
import sys
from collections import Counter


def load_and_read_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return file_handler.read().lower()


def get_most_frequent_words(text):
    words = re.findall(r'\w+', text)
    print(Counter(words).most_common(10))

if __name__ == '__main__':
    document = load_and_read_data(sys.argv[1])
    get_most_frequent_words(document)