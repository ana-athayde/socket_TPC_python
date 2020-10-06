import socket
import json

HOST = '127.0.0.1'  
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    req = input("Digite sua requisicao")
    s.sendall(bytes(req,"utf-8"))
    
    #Pega informações recebidas e passa para a variavel data
    data = s.recv(1024)
    recieved_data = (data.decode('utf-8'))
    if (recieved_data != "Fechamento da conexao") and (recieved_data != "Invalid Command!!!"):
        recieved_data = json.loads(recieved_data)
    print(recieved_data)
