import morse

mensaje = input("Dime algo: ")
codigomierda = morse.toPlain(codigo)
telegrama = morse.toMorse(mensaje)
print(telegrama)
print(codigomierda)