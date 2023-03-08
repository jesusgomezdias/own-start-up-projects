# python script that on each run adds to a text file called log.log a new line showing the date and time of the system. and time of the system.

# we import the library
import datetime
# create/edit document
nuevo_doc = open("registro.txt", "a", encoding="utf-8")
# we take the current time
actual = datetime.datetime.now()
# we convert to string
date_time = actual.strftime("%m/%d/%Y, %H:%M:%S")
try:
 agregar_hora = nuevo_doc.write(date_time + "\n")
 print(agregar_hora)
except:
 print("error")
# close
nuevo_doc.close()
