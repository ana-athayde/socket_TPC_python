# Comunicação Cliente-Servidor com Socket TCP

Este é um projeto que envolve um cliente e um servidor implementados em Python, usando sockets TCP para comunicação. O servidor trata solicitações de clientes de acordo com as seguintes regras:

- **get_date**: Retorna a data atual no formato "DD/MM/YYYY" em um JSON.
- **get_time**: Retorna a hora atual no formato "HH:MM:SS" em um JSON.
- Qualquer outra solicitação: Retorna a mensagem "Invalid Command!!!"

O servidor também exibe informações sobre o IP e a porta de origem dos clientes, bem como os dados enviados.

## Servidor (Server.py)

### Funcionalidade
O arquivo `Server.py` contém o código para um servidor que aceita conexões de clientes por meio de sockets TCP. Ele processa solicitações de clientes e responde de acordo com as regras definidas.

### Funções
1. **`import socket`**: Importa a biblioteca `socket` para trabalhar com comunicações de rede.

2. **`import json`**: Importa a biblioteca `json` para lidar com a formatação e análise de dados JSON.

3. **`import datetime`**: Importa a biblioteca `datetime` para obter informações de data e hora.

4. **`date` e `time`**: Obtêm a data e a hora atuais em formatos específicos.

5. **`HOST` e `PORT`**: Definem o endereço IP e a porta em que o servidor escutará conexões de clientes.

6. **`socket.socket(socket.AF_INET, socket.SOCK_STREAM)`**: Cria um objeto de soquete para comunicação TCP.

7. **`s.bind((HOST, PORT))`**: Liga o servidor a um endereço e uma porta específicos.

8. **`s.listen()`**: Aguarda a chegada de conexões de clientes.

9. **`conn, addr = s.accept()`**: Aceita uma conexão de um cliente e obtém informações sobre o cliente.

10. **Processamento de solicitações**: Com base nas solicitações recebidas, o servidor responde com a data atual, a hora atual ou uma mensagem de comando inválido. Ele também imprime o IP e a porta do cliente, bem como os dados enviados.

11. **Encerramento da conexão**: O servidor permite ao cliente encerrar a conexão usando o comando `exit`.

## Cliente (Client.py)

### Funcionalidade
O arquivo `Client.py` contém o código para um cliente que se conecta a um servidor por meio de sockets TCP. Ele permite ao usuário enviar comandos específicos ao servidor e receber respostas.

### Funções
1. **`import socket`**: Importa a biblioteca `socket` para trabalhar com comunicações de rede.

2. **`import json`**: Importa a biblioteca `json` para lidar com a formatação e análise de dados JSON.

3. **`HOST` e `PORT`**: Definem o endereço IP e a porta do servidor ao qual o cliente se conectará.

4. **`socket.socket(socket.AF_INET, socket.SOCK_STREAM)`**: Cria um objeto de soquete para comunicação TCP.

5. **`s.connect((HOST, PORT))`**: Estabelece uma conexão com o servidor usando o endereço IP e a porta especificados.

6. **`req = input("Digite sua requisicao")`**: Solicita que o usuário insira uma requisição.

7. **`s.sendall(bytes(req,"utf-8"))`**: Envia a requisição ao servidor após convertê-la em bytes.

8. **`data = s.recv(1024)`**: Recebe dados do servidor (até 1024 bytes).

9. **`recieved_data = (data.decode('utf-8'))`**: Decodifica os dados recebidos de volta em uma representação de string.

10. **Processamento de dados**: Verifica se os dados recebidos representam um JSON válido e os imprime.

Lembre-se de que essas explicações fornecem uma visão geral das funções em ambos os arquivos. Cada arquivo contém um conjunto de instruções que implementam essas funcionalidades.

## Autor

Ana Athayde
