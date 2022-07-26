# Socket_TPC_Python

###Servidor:

- servidor implementado utilizando socket TCP;
- deve tratar requisições oriundas de clientes da seguinte forma:
     - ao receber o comando get_date deve responder com um JSON contendo a
seguinte string “date”:”<data_atual>”, com formato DD/MM/YYYY;
     - ao receber o comando get_time deve responder com um JSON contendo a
seguinte string “time”:”<hora_atual>”, com formato HH:MM:SS;
     - caso receba qualquer outra requisição que não sejam os comandos anteriores
deve retornar a seguinte string: Invalid Command!!!
     - ao receber as requisições, o servidor deve imprimir na tela o ip:porta de origem
bem como o payload enviado;

###Cliente:

- cliente implementado utilizando socket TCP;
- deve se conectar ao servidor e ter um terminal o qual será utilizado para a
realização das requisições (especificação acima);
- ao receber as respostas do servidor as mesmas devem ser impressas na tela;
- além dos comandos listados anteriormente deve contemplar o comando <exit> o
qual fará fechamento da conexão estabelecida com o servidor;
