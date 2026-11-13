# 1. ZADATAK

U ovom zadatku je potrebno ispitati koji filter uspešno može da filtrira šum na slici. Možete koristiti bilo koji filter, ali jedan od filtera koji se obrađivao na računskim vežbama uspešno filtrira.

Ukoliko nađete filter koji to radi, a nije obrađivan na vežbama, dobićete 1 bonus poen.

U okviru materijala za ovu laboratorijsku vežbu (u folderu `Zadatak 1`) nalaze se 3 slike sa različitim šumom. Potrebno je napisati program koji će učitati sliku po sliku i filtrirati šum na svakoj od njih (ne istim filterom, naravno).

# 2. ZADATAK

U ovom zadatku je potrebno filtrirati sliku Gausovim filtrom, ali umesto u prostornom domenu (konvolucijom), potrebno je to uraditi u frekventnom domenu i vratiti sliku nazad.

U okviru materijala za ovu laboratorijsku vežbu (u folderu `Zadatak 2`) nalazi se slika koju treba iskoristiti kao ulaz u program.

Sliku i Gausov kernel transformisati u frekventni domen i filtrirati sliku koristeći Teoremu o konvoluciji, zatim vratiti sliku u prostorni domen i prikazati je.

# 3. ZADATAK

U ovom zadatku je potrebno transformisati sliku tako da se zamene amplituda i faza frekventnog domena.

U okviru materijala za ovu laboratorijsku vežbu (u folderu `Zadatak 3`) nalazi se slika koju treba iskoristiti kao ulaz u program.

Sliku najpre transformisati u frekventni domen, zameniti njenu amplitudu i fazu i vratiti sliku u prostorni domen. Prikazati transformisanu sliku na kraju.

# 4. ZADATAK

U ovom zadatku je potrebno filtrirati periodični šum na slici.

U okviru materijala za ovu laboratorijsku vežbu (u folderu `Zadatak 4`) nalazi se 5 slika, gde možete bilo koju iskoristiti kao ulaz.

Standardni način rešavanja je primenom Furijeove transformacije prebaciti sliku u frekventni domen, zatim sa amplitude pronaći svetle tačke koje generišu šum na slici.

Ukloniti šum obradom tih tačaka (postaviti na 0 je dovoljno) i vratiti sliku u prostorni domen i prikazati je.

Rešenje koje koristi algoritam koji uspešno filtrira šum kod svih 5 slika biće ocenjeno većim brojem poena.