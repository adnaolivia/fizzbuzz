class Fizzbuzz():

    def __init__(self) -> None:
        pass
    
    def _regras(self, numero: int) -> str:
        if numero % 3 == 0 and numero % 5 == 0:
            return "fizzbuzz"
        elif numero % 3 == 0:
            return "fizz"
        elif numero % 5 == 0:
            return "buzz"
        else:
            return str(numero)
    
    def main(self, numero: int):
        resultado = self._regras(numero)
        print(resultado)

fizzbuzz = Fizzbuzz()
numero = int(input("digite um numero: "))
fizzbuzz.main(numero)