from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP 
from os import environ

def enviar_correo(destinatarios,  titulo, cuerpo):
    mensaje = MIMEMultipart()
    email_emisor = environ.get('EMAIL_SENDER')
    password_email_emisor = environ.get('PASSWORD_SENDER')

    # Agregando el titulo a nuestro mensaje
    mensaje['Subject'] = titulo
    
    # Agregando el cuerpo a nuestro mensaje
    mensaje.attach(MIMEText(cuerpo))

    emisor = SMTP('outlook.office365.com', 587)

    emisor.starttls()

    emisor.login(user= email_emisor, password=password_email_emisor)

    emisor.sendmail(from_addr= email_emisor, to_addrs= destinatarios, msg=mensaje.as_string())

    # cerrar la conexion con mi servidor de correos
    emisor.quit