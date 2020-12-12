import socket
import re
socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)




ip = "127.0.0.1"
port = 8001
socket_server.bind((ip,port))
socket_server.listen(5)
print(f"\n\nServer Listening on {ip}:{port}")



salir = False
while salir == False:
    conexion, address = socket_server.accept()
    print ("la conexion se establecio con exito")
    archi1=open("mensaje.txt","r")
    contenido=archi1.read()
    print(contenido)
    test_str = contenido
    archi1.close()            



    while True:
        message = conexion.recv(1024)
        message = message.decode()
        print(message)    



        if message == 'adios':
            message = 'Adios...'
            conexion.send(message.encode())
            print("\n")
            salir = True
            break



        elif message == 'buenas':                                         
            message = ("¡QUE TAL! , soy FELIPE LOPEZ MENDEZ. Seleccione una opcion  :\n\n1. Variables válidas."
                        "\n2. Enteros y decimales.\n3. Operadores aritméticos.\n4. Operadores relacionales.\n"
                        "5. Palabras reservadas.\n\n")
            conexion.send(message.encode())
        



        elif message == '1':
            regex = r'(?s)^((?!hede)[^ ^$1-9])'                             
            matches = re.finditer(regex, test_str, re.MULTILINE)


            for matchNum, match in enumerate(matches, start=1):
                    

                    message = ("Resultados encontrados --> {matchNum} resultados. ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                           
            if message == '1':
                 message = ("Resultados encontrados--> 0 resultados. ")                                                           
            conexion.send(message.encode())            

        elif message == '2':
            regex = r"([0-9]{1,3$}$|[0-9]{1,3}\.[0-9]{1,9})"            
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    message = ("Resultados encontrados --> {matchNum} resultados ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                                      
            if message == '1'  or message == '2':
                 message = ("Resultados encontrados --> 0 resultados ")                                                           
            conexion.send(message.encode())





        elif message == '3':
            regex = r'([+]|[]^[]|[*]|-|//|/|%)'                                   
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    message = ("Resultados encontrados --> {matchNum} resultados ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                       
            if message == '1'  or message == '3':
                 message = ("Resultados encontrados --> 0 resultados ")                                                           
            conexion.send(message.encode()) 


        elif message == '4':
            regex = r'(!=|>=|<=|==|<|=|>|<)'                                      
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    message = ("Resultados encontrados --> {matchNum} resultados ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                                        
            if message == '1'  or message == '4':
                 message = ("Resultados encontrados --> 0 resultados ")                                                           
            conexion.send(message.encode())


        elif message == '5':
            regex = r'(?i)(\W|^)(False|await|else|import|pass|None|break|except|in|raise|True|class|finally|is|return|and|continue|for|lambda|try|as|def|from|nonlocal|while|assert|del|global|not|with|async|elif|if|or|yield)(\W|$)'                                 
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    message = ("Resultados encontrados --> {matchNum} resultados. ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                        
            if message == '1' or message == '5':
                 message = ("Resultados encontrados --> 0 resultados. ")                                                           
            conexion.send(message.encode())                            

        else:
            message = 'elije una opcion'            
            conexion.send(message.encode())

conexion.close()
print("Servidor Finalizado")