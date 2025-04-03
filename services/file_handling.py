import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 800

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    valid_end_simbols = ',.!:;?'
    text = text[start:size+start]  # обрезаем текст слева
    while len(text) > size or text[-1] not in valid_end_simbols:
        max_sybl = max(map(text.rfind, valid_end_simbols))
        text = text[:text.rfind(' ')] \
            if max_sybl+1 == len(text) else text[:max_sybl+1]
    return text, len(text)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            content = file.read().rstrip('\n')  # убираем пустую строку в конце текста
            page_num = 1
            start = 0
            while start < len(content):
                page, len_page = _get_part_text(content, start, PAGE_SIZE)
                book[page_num] = page.lstrip('\n\t\ufeff ')
                start += len_page
                page_num += 1
    else:
        print("Файл не найден")


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
