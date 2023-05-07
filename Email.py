class Email:
    __nombre = ''
    __contrasena = ''
    __cuenta = ''
    __dominio = ''
    __tipodominio = ''

    def __init__(self, nom, contra, ide, dom, tipdom):
        self.__nombre = nom
        self.__contrasena = contra
        self.__cuenta = ide
        self.__dominio = dom
        self.__tipodominio = tipdom

    def mensaje_mail(self):
        print('Estimado', self.__nombre, 'te enviaremos tus mensajes a la dirección',
              self.__cuenta + '@' + self.__dominio + '.' + self.__tipodominio)

    def modificar_contrasena(self):
        con= input('Ingrese contraseña actual: ')
        if con==self.__contrasena:
            self.__contrasena= input("Ingrese contraseña nueva: ")
        else:
            print ('Contraseña incorrecta')
            self.modificar_contrasena()

    def retornar_dominio(self):
        return self.__dominio.lower()
    