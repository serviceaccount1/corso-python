# tipi di dato

# i metodi o proprietà sono le funzionalità che si porta dietro un oggetto

stringa = "stringa"


# print(stringa.capitalize())
# print(stringa.upper())
# print(stringa.__contains__("e"))
# print(stringa.endswith("a"))
# print(stringa.isupper())

# print(stringa + " ciao")


# metodi numero

numero = 100.1111

round_numero = round(numero, 2) 
int(numero)


foo = False  # 0
bar = True  # 1


# metodi liste

lista = ["ciao", "ciao", True, "stringa"]

lista_numeri = [2, 1, 5, 0, 3, 4]

# indici # 0,1,2,3,4,5

# aggiungere dati
lista.append("altro dato")

# aggiungere dati in possizione
lista.insert(2, "dato2")

# rimuovere ultimo dato dalla lista
lista.pop()
lista.pop(1)

# lista.clear() # svuota lista

lista.remove("dato2")  # rimuovere da elemento preciso


# somma totale
sum(lista_numeri)

# vedere quanti elementi ci sono dello stesso tipo
lista_di_uno = [1, 1, 1, 1, 2]
lista_di_uno.count(1)


# sort lista
lista_numeri.sort()
sorted(lista_numeri)


# slicing
lista_esempio = [1,2,3,4,5]
print(lista_esempio[1:4])


# trovare indice da valore
# lista_numeri.index(1)


# metodi dict (chiave:valore)


x = {
    "chiave":"valore"
}

dizionario = {
    "nome":"Paolo",
    "eta":20,
    "cognome":"rossi",
    "indirizzo":{
        "via":"dei platani",
        "numero":2,
        "vicini":[
            {"nome":"carlo","cognome":"rossi"},
            {"nome":"giulio","cognome":"bianchi"}
        ]
    },
    "interessi":["joigging","nuoto","lettura"]
}

# prendere dati da un dict
print(dizionario["interessi"][-1])


# remove item
dizionario.pop("nome")
# dizionario["indirizzo"]["vicini"][1].pop("nome")

del dizionario["cognome"]


chiavi =  dizionario.keys()
valori = dizionario.values()

to_lista = list(chiavi)