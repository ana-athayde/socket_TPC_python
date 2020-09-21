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
    data1 = (data.decode('utf-8'))
    if (data1 != "Fechamento da conexao") and (data1 != "Invalid Command!!!"):
        data1 = json.loads(data1)
    print(data1)
