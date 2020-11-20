from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

#crea la instancia del objeto de mensaje
msg = MIMEMultipart()
#configura los parametros del mensaje
password = "epas2817epas"
msg['From'] ="erickpasache0@gmail.com"
msg['To'] = "epasache_28@hotmail.com"
msg['Subject'] = "Photo"
#adjunta imagen en el cuerpo del mensaje
msg.attach(MIMEImage(file("image.jpg").read()))
#crear servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
#Ingresa credenciales para enviar email
server.login(msg['From'], password)
#envia el mensaje al servidor
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print ("Envio de email exitoso a %s:" % (msg['To']))