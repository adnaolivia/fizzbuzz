class Fizzbuzz():

    def __init__(self) -> None:
        pass
    
    def _regras(self, numero: int):
        for numero in range(1, 101):
            if numero % 3 == 0 and numero % 5 == 0:
                print("fizzbuzz")
            elif numero % 3 == 0:
                print("fizz")
            elif numero % 5 == 0:
                print("buzz")
            else:
                print(numero)
    
    def main(self, numero: int):
        input("digite um numero entre 1 e 100: ", numero)
        resultado = self._regras(numero)
        print(resultado)

fizzbuzz = Fizzbuzz()
fizzbuzz.main()