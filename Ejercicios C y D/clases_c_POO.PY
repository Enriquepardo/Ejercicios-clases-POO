#Enunciado: adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible:
class A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A 
y = a.z 
print(y(a)) 
aa = a() 
print(aa is a()) 
z = aa.y 
print(z(())) 
print(a().y((a,))) 
print(A.y(aa, (a,z))) 
print(aa.y((z,1,'z')))

"Respuesta:"
#clase A
"En primer lugar tenemos la clase A, esta no tiene ningun atiubuto, solo tiene dos metodos, el metodo z, que devuelve el objeto que lo llama, y el metodo y, que devuelve la longitud de la tupla que le pasamos como parametro."

#variables creadas a partir de la clase A
"Luego tenemos a =A que es una variable creada a partir de la clase A" 

"y = a.z, que es una variable que  dentro de la clase A llama al metodo z, y lo guarda en la variable y"
"print(y(a)) imprime el objeto que se le pasa como parametro, en este caso el objeto a, que es una variable creada a partir de la clase A"

"aa = a() crea un objeto a partir de la clase A, y lo guarda en la variable aa"
"print(aa is a()) suponemos que imprime un booleano, que nos dice si el objeto que se le pasa como parametro es igual al objeto que se le pasa como parametro, en este caso el objeto a(), que es un objeto creado a partir de la clase A"

"z = aa.y, que es una variable que  dentro de la clase A llama al metodo y, y lo guarda en la variable z"
"print(z(())) imprime la longitud de la tupla que se le pasa como parametro, en este caso,  como le pasamos la tupla vacia que tiene longitud 0, devuelve 0"

"print(a().y((a,))) imprime la longitud de la tupla  que le pasamos , en este caso, la tupla solo tiene un elemento por lo que este metodo devuelve 1"
"print(A.y(aa, (a,z))) de nuevo se vuelve a imprimir la longitud de la tupla  que le pasamos , en este caso, tiene  dos elementos ,aa que es un objeto creado a partir de la clase A, y la tupla (a,z) , por lo que este metodo devuelve 2"
"print(aa.y((z,1,'z'))) este tendría que imprimir también la tupla que le estamos pasando . En este caso, tenemos tres elementos ,z que es una variable que  dentro de la clase Ay, 1 que es un entero y 'z' que es un string, este metódo devolverá un error, ya que z y el entero 1 no tienen el metodo len, por lo que no se puede calcular la longitud de la tupla"




