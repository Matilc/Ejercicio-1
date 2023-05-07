from Email import Email
import csv

class ManejadorEmail:
    __listaemails=[]

    def __init__(self):
        self.__listaemails=[]
      
    def mails_archivo(self):
        listacorreo= open('Correos.csv')
        reader = csv.reader(listacorreo,delimiter=';')
        for fila in reader:
            if fila[0]!='':
                mail= Email(fila[4], fila[3], fila[0], fila[1].strip(), fila[2].strip())
                self.__listaemails.append(mail)
            else:
                print ('Dirección de mail incorrecta, de '+fila[4])
    def dominio_email (self):
        dom=input ("Ingrese el dominio a buscar ")
        a=0
        for mail in self.__listaemails:
            if mail.retornar_dominio()==dom:
                a+=1
        print ('Hay '+ str(a) ,'correos con el dominio '+dom)