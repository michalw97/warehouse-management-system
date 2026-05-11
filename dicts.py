#  System Zarządzania Magazynem — 7 wymagań:
#
#   1. Magazyn startuje z kilkoma produktami — każdy produkt ma nazwę jako klucz i ilość jako wartość.
#   2. Program wyświetla menu z opcjami i działa w pętli do momentu aż manager wybierze wyjście.
#   3. Manager może sprawdzić stan konkretnego produktu. Jeśli produkt nie istnieje — informacja bez crashu.
#   4. Manager może przyjąć dostawę — podaje nazwę i ilość do dodania. Jeśli produkt już jest — ilość się zwiększa. Jeśli nowy — zostaje dodany.
#   5. Manager może wysłać towar — podaje nazwę i ilość. Jeśli produktu nie ma lub jest za mało — odpowiedni komunikat. Jeśli wystarczy — ilość się zmniejsza. Jeśli po wysyłce zostaje 0 — produkt znika z magazynu.
#   6. Manager może wyświetlić pełny raport — wszystkie produkty posortowane alfabetycznie z ich stanami.
#   7. Na końcu każdej operacji wyświetl aktualną liczbę unikalnych produktów w magazynie.

items = {}

while True:

    print("------------.MENU.------------")
    print("1. Sprawdź stan produktu.")
    print("2. Dodaj dostawę.")
    print("3. Wyślij towar.")
    print("4. Wyświetl pełny raport.")
    print("5. Zakończ.")
    print("------------------------------")

    user_choice = int(input("Którą opcję chcesz wybrać?: "))

    if user_choice == 1:
        if len(items) > 0:
            print("Dostępne produkty:")
            for k in items.keys():
                print(f"> {k}")

            item_choice = input("Który produkt chcesz sprawdzić?: ")

            if item_choice in items:
                print("------------------------------")
                print(f"Liczba sztuk produktu {item_choice}: {items.get(item_choice)}")
                print("------------------------------")
            else:
                print("------------------------------")
                print("Nie ma takiego produktu.")
                print("------------------------------")
        else:
            print("------------------------------")
            print("Brak produktów")
            print("------------------------------")

        print(f"Liczba wszystkich przedmiotów: {len(items)}")

    elif user_choice == 2:
        delivery = input("Podaj nazwę produktu z dostawy: ")
        quantity_delivery = int(input("Podaj ilość produktów z dostawy: "))

        if delivery in items:
            items[delivery] += quantity_delivery
            print(f"Produkt {delivery} był już w bazie. Nadpisano pomyślnie.")
        else:
            items[delivery] = quantity_delivery
            print("------------------------------")
            print("Dodano pomyślnie.")
            print("------------------------------")

        print(f"Liczba wszystkich przedmiotów: {len(items)}")

    elif user_choice == 3:
        shipping = input("Podaj nazwę produktu do wysyłki: ")
        quantity_shipping = int(input("Podaj ilość produktów do wysyłki: "))

        if shipping not in items:
            print("------------------------------")
            print("Brak produktu w magazynie.")
            print("------------------------------")
        elif quantity_shipping > items[shipping]:
            print("------------------------------")
            print("Brak wymaganej ilości sztuk na magazynie.")
            print("------------------------------")
        else:
            items[shipping] -= quantity_shipping
            print("------------------------------")
            print("Pomyślnie wysłano produkt.")
            print("------------------------------")

            if items[shipping] == 0:
                del items[shipping]

        print(f"Liczba wszystkich przedmiotów: {len(items)}")

    elif user_choice == 4:
        if len(items) == 0:
            print("------------------------------")
            print("Nie można uzyskać raportu. Brak przedmiotów na magazynie")
            print("------------------------------")
        else:
            print("------------.PEŁNY RAPORT.------------")
            for k, v in sorted(items.items()):
                print("------------------------------")
                print(f"Produkt: {k}")
                print(f"Ilość: {v}")
                print("------------------------------")

        print(f"Liczba wszystkich przedmiotów: {len(items)}")

    elif user_choice == 5:
        break

