"""
===================   TASK 5   ====================
* Name: Del Boy Millionaire
*
* Help Del Boy become a millionaire. Del Boy is
* trading bitcoins on crypto-exchanges with simple
* algorithm. He is buying where the price of bitcoin
* is the lowest and selling where the bitcoin is
* the most expensive. Write a function `get_profit`
* which will take a list of bitcoin prices in USD as
* argument. The function should return what is the
* maximum possible profit for given bitcoin prices
* on different exchanges.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def get_profit(lista):


    def min(lista):

        min_lista = lista[0]

        for i in range(len(lista) - 1):

            if min_lista > lista[i + 1]:
                min_lista = lista[i + 1]

        return min_lista


    def max(lista):

        max_lista = lista[0]

        for i in range(len(lista) - 1):

            if max_lista < lista[i + 1]:
                max_lista = lista[i + 1]

        return max_lista


    return max(lista) - min(lista)


def main():
    lista = [156.7,45.7,19.0,567.8]
    print("Najveci ostvareni profit je: ", get_profit(lista))
    pass


main()

