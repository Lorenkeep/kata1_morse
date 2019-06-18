import morse
import time
for docx import Document

mensaje = input("Dime algo: ")

telegrama = morse.toMorse(mensaje)
print(telegrama)
original = morse.toPlain(telegrama)
print(original)

print(time.strftime("%d/%m/%y", time ))