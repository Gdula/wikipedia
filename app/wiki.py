import wikipedia
import sys


def choose_language(language):
    wikipedia.set_lang(language)


def show_languages():
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


def suggest():
    quary = input("Co chcesz wyszukać?: ")
    print(wikipedia.suggest(quary))


def summary():
    quary = input("Co chcesz wyszukać?: ")
    print(wikipedia.summary(quary))


def print_main_menu():
    print("[1]. Wyszukaj\n[2]. Streszczenie artukułu\n[3]. Zaproponuj\n[4]. Wyjście\n")


def main():
    show_languages()
    language = input("Wybierz język:")
    choose_language(language)

    print_main_menu()
    user_input: str = input("Wybierz co chcesz zrobić: ")

    if (user_input == '1'):
        search()
    elif (user_input == '2'):
        summary()
    elif (user_input == '2'):
        suggest()
    elif (user_input == '3'):
        sys.exit()


if __name__ == "__main__":
    main()
