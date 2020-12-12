import socket
import re

socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


host = "127.0.0.1"
port = 8001
socket_client.connect((host,port))

while True: 
    mensaje = input("Cliente : ")           
    socket_client.send(mensaje.encode())        
    respuesta = socket_client.recv(1024) 
    respuesta = respuesta.decode()
    print(f"Servidor: {respuesta}")

socket_client.close()
