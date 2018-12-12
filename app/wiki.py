import wikipedia
import sys
import os
from bs4 import BeautifulSoup


def choose_language():
    user_input = input("[1]. Wpisz kod WP swojego języka(en, pl, de, etc.)\n"
                       "[2]. Wybierz język z listy\n")
    language_choosen = False
    languages = wikipedia.languages()

    if user_input == '1':
        while not language_choosen:
            wp_code = input("Wpisz kod: ")
            if wp_code in languages:
                wikipedia.set_lang(wp_code)
                language_choosen = True
            else:
                print("Nie istnieje taki kod!")
    else:
        show_languages(languages)
        while not language_choosen:
            search_language = input("Podaj język: ")
            if search_language in languages.values():
                for wp, lang in languages.items():
                    if lang == search_language:
                        wikipedia.set_lang(wp)
                        language_choosen = True
            else:
                print("Nie ma takiego języka")
    os.system('clear')

def show_languages(languages):
    i = 1

    for key, value in languages.items():
        print("{}. {}".format(i, value))
        i += 1


def search():
    quary = input("Co chcesz wyszukać?: ")
    elements = wikipedia.search(quary)
    i = 1

    for element in elements:
        print("{}. {}".format(i, element))
        i += 1
    print("\n\n")


def summary():
    i = 1
    quary = input("Wpisz nazwę strony jakiej streszczenie chcesz otrzymać: ")
    try:
        text = wikipedia.summary(quary)
        print(text)
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options
        print("Twój wybór nie jest jednoznaczny, wybierz jedną z możliwosći: ")
        for element in options:
            print("{}. {}".format(i, element))
            i += 1
        choosen_article = input("Podaj numer do wyświetlenia")
        print(wikipedia.summary(options[int(choosen_article) - 1]))


def print_random_page():
    random_page = wikipedia.random(pages=1)
    soup1 = BeautifulSoup(random_page, 'html.parser')
    page = wikipedia.page(random_page)
    print("Wylosowałeś: {}".format(soup1))
    while True:
        user_input = input("Co chcesz zobaczyć na stronie?:\n"
                           "[1]. Pokaż kategorię\n"
                           "[2]. Wyświetl streszczenie\n"
                           "[3]. Powrót")
        if user_input == '1':
            os.system('clear')
            categories = page.categories
            for category in categories:
                print(category + '\n')
        elif user_input == '2':
            os.system('clear')
            summary = BeautifulSoup(page.summary, 'html.parser')
            print(summary)
        elif user_input == '3':
            os.system('clear')
            break


def print_main_menu():
    print("[1]. Wyszukaj strone\n"
          "[2]. Pokaż streszczenie strony\n"
          "[3]. Losowa strona\n"
          "[0]. Wyjście\n")


def main():
    os.system('clear')
    choose_language()

    while True:
        print_main_menu()
        user_input: str = input("Wybierz co chcesz zrobić: ")

        if user_input == '1':
            os.system('clear')
            search()
        elif user_input == '2':
            os.system('clear')
            summary()
        elif user_input == '3':
            os.system('clear')
            print_random_page()
        elif user_input == '0':
            sys.exit()


if __name__ == "__main__":
    main()

