#Importa as bibliotecas socket, json e datetime
import socket
import json
import datetime

x = datetime.datetime.now()
date = x.strftime('%d-%m-%Y') 
time = x.strftime("%X")

data_String = '{"date" : "'+ date +'"}'
time_String = '{"time": "'+ time +'"}'

HOST = '127.0.0.1'  
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    msg = ""
    while msg != "exit":
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)            
                if not data:
                    break

                #Esse a gente decodifica a mensagem recebida
                data_teste = (data.decode('utf-8'))

                #Pega mensagem recebidade, e entra em um if
                if data_teste == "get_date":
                    #Envia para o cliente a data em formato de String
                    conn.sendall(bytes(data_String,"utf-8"))
                    print("Payload:",data_String)

                elif data_teste == "get_time":
                    #Envia para o cliente o horario em formato de String
                    conn.sendall(bytes(time_String,"utf-8"))
                    print("Payload:",time_String)

                elif data_teste == "exit":
                    conn.sendall(bytes("Fechamento da conexao","utf-8"))
                    print("Payload:","Fechamento da conexao")
                    msg ="exit" 
                    s.close()

                else: 
                    conn.sendall(bytes("Invalid Command!!!","utf-8")) 
                    print("Payload:","Invalid Command!!!")
           
