from ManejadorEmails import ManejadorEmail
from Email import Email

def ingresa_datos ():
        nombre = input ("Ingrese el nombre: ")
        contrasena = input ("Ingrese la contraseña: ")
        cuenta = input ("Ingrese la cuenta de mail: ")
        dominio = input ("Ingrese el dominio de la cuenta: ")
        tipodominio = input ("Ingrese el tipo de dominio de la cuenta: ")
        persona = Email(nombre, contrasena, cuenta, dominio, tipodominio)
        return persona

def ingresa_mail ():
    nuevomail= input ('Ingrese su mail: ')
    cuenta, dominio= nuevomail.split("@")
    dominio, tipodominio= dominio.split(".")
    mail = Email('Anónimo', 1234, cuenta, dominio, tipodominio)
    mail.mensaje_mail()
    return mail

if __name__ == '__main__':
    p=ingresa_datos()
    p.mensaje_mail()
    p.modificar_contrasena()
    solomail=Email()
    solomail=ingresa_mail()
    lmails=ManejadorEmail()
    lmails.dominio_email()