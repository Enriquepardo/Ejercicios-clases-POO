class Palindromo:
    @classmethod
    def esPalindromo(cls, cadena):
        cadena = ''.join(e for e in cadena if e.isalnum())
        return cadena.lower() == cadena[::-1].lower()

    def test(self):
        return Palindromo.esPalindromo(self.cadena)


p = Palindromo()
print(p.esPalindromo('radar')) 
print(p.esPalindromo('sonar')) 
print(p.esPalindromo('Arde ya la yedra'))
print(p.esPalindromo('Ardeyalayedra')) 
print(p.esPalindromo('!@#$% %$#@!')) 
print(p.esPalindromo('L O L')) 



