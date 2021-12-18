import json
import re

BOOKS_FILE = "books.md"
POSITION = r'(?P<position>\d+)'
BOOK = r'\[(?P<book>.*?)\]'
BOOK_URL = r'(?P<book_url>.*?)'
AUTHOR = r'(?P<author>.*?)\s'
RECOMMENDED = r'((?P<recommended>.d{1,3)\.\d+%) recommended\)'
COVER = r'(?P<cover_url>https.+?)\)'
DESCRIPTION = r'"(?P<description>.+?)\"'
#BOOK_REGEX = r"""#### (?P<position>\w+)\. \[(?P<book>.*?)]\((?P<book_url>.*?)\) by (?P<author>.*?) \((?P<recommended>.*?)\%.*?(?P<cover_url>https.*?)\).*?"(?P<description>.*?)"""

BOOK_REGEX = f"{POSITION}\.\s+{BOOK}{BOOK_URL}\s+by\s+{AUTHOR}{RECOMMENDED}\s+!\[.*?\]\s+{COVER}\s+{DESCRIPTION}"


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки
    result = list()
    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            result.append(book.groupdict())
    result.sort(key = lambda dict_elem : int(dict_elem.position))

    with open('result.json','w'):
        json.dump(result, f, indent = 4, ensure_ascii=False)

if __name__ == '__main__':
    task()
