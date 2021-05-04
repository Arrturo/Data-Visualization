"""
Paradygmaty Programowania, laboratorium 1
Zadanie: Sortowanie bąbelkowe, przez selekcję i przez wstawianie
"""

import random
import timeit
from matplotlib import pyplot as plt

"""Zwraca listę liczb całkowitych [0, 1, ..., seq_len-1]"""


def incr_seq(seq_len):
    return list(range(seq_len))


"""Zwraca listę liczb całkowitych [seq_len-1, seq_len-2, ..., 0]"""


def decr_seq(seq_len):
    return list(reversed(range(seq_len)))


"""Zwraca listę o długości seq_len, zawierającą niepowtarzające się
losowe liczby całkowite z zakresu [0, seq_len-1).
"""


def rand_seq(seq_len):
    return random.sample(range(seq_len), seq_len)


"""Kolejne wywołania zwracają listy liczb całkowitych
o długościach: min_len, 2*min_len, 4*min_len, ... max_len.
Poszczególne listy są tworzone przez funkcję przekazaną jako make_seq.
Zaleca się, by jako make_seq używać jednej z uprzednio
zdefiniowanych funkcji: incr_seq, decr_seq lub rand_seq.
"""


def seq_generator(min_len, max_len, make_seq):
    this_len = min_len
    while this_len <= max_len:
        yield make_seq(this_len)
        this_len *= 2


"""Sortowanie przez selekcję (wybór)"""


def selection_sort(tab):
    comp_cnt = 0
    for first_unsorted in range(len(tab)):
        min_so_far = first_unsorted
        for i in range(first_unsorted, len(tab)):
            comp_cnt += 1
            if tab[i] < tab[min_so_far]:
                min_so_far = i
        tab[first_unsorted], tab[min_so_far] = tab[min_so_far], tab[first_unsorted]
    return comp_cnt


"""Wykreśla zależność czasu wykonania i liczby porównań
algorytmu sortowania 'sort_alg' dla kolejnych list
o rozmiarze rosnącym od 'min_len' do 'max_len'.
Zawartość list jest generowana za pomocą funkcji 'seq_type'.
"""


def plot_complexity(sort_alg, min_len, max_len, seq_type):
    # Zaczątki tablic, w których zostaną zapamiętane:
    # - rozmiary kolejnych ciągów do posortowania,
    sizes = []
    # - czasy kolejnych sortowań,
    times = []
    # - liczby porównań wykonanych podczas sortowania kolejnych tablic.
    comparisons = []

    for tab1 in seq_generator(min_len, max_len, seq_type):
        # Sortowanie modyfikuje zawartośc listy.
        # Aby niezależnie zmierzyć czas i liczbę kopiowań,
        # potrzebujemy dwóch identycznych list.
        tab2 = tab1.copy()
        sizes.append(len(tab1))
        # Zliczamy porównania dokonane podczas sortowania każdej z list
        comparisons.append(sort_alg(tab1))
        # Do 'timeit' można przekazać funkcję, ale tylko taką, która nie zawiera argumentów.
        # Dlatego 'opakowujemy' wywołanie 'sort_alg(tab2)'
        def my_alg():
            return sort_alg(tab2)

        # Mierzymy czas wykonania 'pustej' instrukcji 'timeit'
        time_noop = timeit.timeit(number=1)
        # Mierzymy czas sortowania każdej z list
        times.append(
            timeit.timeit(stmt=my_alg, number=1, globals=globals()) - time_noop
        )

    # Należy dobrać taką skalę na obu osiach obu poniższych wykresów,
    # która pozwoli najlepiej oszacować złożoność obliczeniową i czasową algorytmu:
    # plot, semilogx, semilogy, loglog?
    plt.plot(sizes, comparisons, "b.-")
    plt.xlabel("Długość sortowanego ciągu", fontsize=12)
    plt.ylabel("Liczba porównań", fontsize=12)
    plt.grid(True)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig("sort_porównania.pdf", format="pdf")
    plt.show()

    plt.plot(sizes, times, "r.-")
    plt.xlabel("Długość sortowanego ciągu", fontsize=12)
    plt.ylabel("Czas sortowania (s)", fontsize=12)
    plt.grid(linestyle="dotted")
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig("sort_czas.pdf", format="pdf")
    plt.show()


if __name__ == "__main__":
    # Sortowanie ciągu losowego algorytmem przez selekcję.
    plot_complexity(selection_sort, 2, 2 ** 12, rand_seq)
