"""Przyklad zastosowania metod iteracyjnych do rozwiazania zadanego ukladu
    oraz pomiaru czasu wykonywania sie operacji dla losowego ukladu"""

import time, numpy as np
import sortowania, wykresy, uklad, zadanie
import gauss, gaussjordan, cholesky, banachiewicz
import iteracjaprosta, iteracjaseidela

def testy(typ):
    if typ == 1:
        """Przyklad sortowania tablic o zadanej dlugosci"""
        n = 100
        test1 = sortowania.Sortowania(n)
        test1.losuj()
        print(test1)
        stoper = time.time()
        test1.sortuj_przez_wstawianie()     
        czas1 = (time.time()-stoper)        
        stoper = time.time()
        test1.sortuj_przez_wybieranie()
        czas2 = (time.time()-stoper)
        print("------"*10)
        print("Sortowanie przez wstawianie:")
        print(test1.wyswietl_liste1())      
        print("Czas sortowania:", czas1)
        print("------"*10)
        print("Sortowanie przez wybieranie:")
        print(test1.wyswietl_liste2())
        print("Czas sortowania przez wybieranie:", czas2)
    elif typ == 2:
        """Badanie zlozonosci obliczeniowej obu metod sortowania"""
        test2 = sortowania.Sortowania(
            n = 1000,
            lprob = 7,
            ldlugosci = 77,
            najkrotsza = 100
        )
        # print("Sortowanie przez wstawianie:")
        # test2.badaj_zlozonosc(1)
        print("Sortowanie przez wybieranie:")
        test2.badaj_zlozonosc(2)
    elif typ == 3:
        """Porownujemy obie metody"""
        test3 = sortowania.Sortowania(
            n = 1000,
            lprob = 7,
            ldlugosci = 77
        )
        test3.porownaj_metody()
    elif typ == 4:
        """Miejsce na rozwiazanie - przygotowanie"""
        # tworzymy obiekt klasy Uklad
        n = 150

        # rozmiar n = 20, pokazywał czas 0.0, został zmieniony na n = 150

        test1  = uklad.Uklad(n)
        
        # losujemy odpowiedni uklad rownan

        test1.losuj_uklad()
        
        # tworzymy obiekt klasy odpowiadajacej metodzie
        # metoda gaussa
        proba1 = gauss.Gauss(test1)
        
        # uruchamiamy stoper
        stoper = time.time()
        # wywolujemy odpowiednie metody

        proba1.eliminacja()
        proba1.rozwiaz_trojkatny()
        
        # zatrzymujemy stoper
        czas = time.time() - stoper

        # wyswietlamy czas rozwiazywania ukladu
        proba1.wypisz_rozwiazanie()
        print(f"Czas rozwiazywania ukladu: {czas}")
        
    elif typ == 5:
        """Miejsce na rozwiazanie Zadania 1"""
        # tworzymy obiekt klasy Zadanie i podajemy odpowiednie parametry
        zad1 = zadanie.Zadanie()
        # badamy zlozonosc obliczeniowa wybranej metody
        zad1.badaj_zlozonosc(
            metoda = 1,
            opis = "Metoda Gaussa"
        )
    elif typ == 6:
        # porownujemy metody
        # tworzymy obiekt klasy Zadanie i podajemy odpowiednie parametry
        zad2 = zadanie.Zadanie()
        # badamy zlozonosc obliczeniowa wybranej metody
        zad2.porownaj_metody(
            nazwa_metody1 = "Metoda ...",
            nazwa_metody2 = "Metoda ..."
        )
        
if __name__ == '__main__':
    testy(5)

    #zad1 = zadanie.Zadanie()
    #print("Srednia dla M = 4: "+str(zad1.mierz_czas(1, 150)))
    