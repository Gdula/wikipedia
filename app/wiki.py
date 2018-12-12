import wikipedia
import sys
import os


def choose_language():
    user_input = input("[1]. Wpisz kod WP swojego języka(en, pl, de, etc.)\n[2]. Wybierz język z listy\n")
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


def show_languages(languages):
    i = 1
    languages = wikipedia.languages()

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


def suggest():
    quary = input("Co chcesz dospasowac?: ")
    print(wikipedia.suggest(quary))


def summary():
    i = 1
    quary = input("Co chcesz wyszukać?: ")
    try:
        text = wikipedia.summary(quary)
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options
        print("Twój wybór nie jest jednoznaczny, wybierz jedną z możliwosći: ")
        for element in options:
            print("{}. {}".format(i, element))
            i += 1
        choosen_article = input("Podaj numer do wyświetlenia")
        print(wikipedia.summary(options[int(choosen_article) - 1]))


def print_random_page():
    print(wikipedia.random(pages=1))


def print_main_menu():
    print("[1]. Wyszukaj\n[2]. Streszczenie artukułu\n[3]. Dopasuj zapytanie\n[4]. Losowa strona\n[0]. Wyjście\n")


def main():
    choose_language()

    while True:
        print_main_menu()
        user_input: str = input("Wybierz co chcesz zrobić: ")

        if user_input == '1':
            os.system('clear')
            search()
        elif user_input == '2':
            summary()
        elif user_input == '3':
            suggest()
        elif user_input == '4':
            print_random_page()
        elif user_input == '0':
            sys.exit()


if __name__ == "__main__":
    main()
