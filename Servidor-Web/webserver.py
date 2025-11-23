# Importa o módulo socket 
from socket import * 
import sys  # Necessário para encerrar o programa 
 
# Cria o socket TCP (orientado à conexão) 
serverSocket = socket(AF_INET, SOCK_STREAM)

# INFO: Prepara o socket do servidor 
# INFO: Start para o servidor

serverPort = 3000
serverSocket.bind(('', serverPort))
print('Porta sendo usada: ', serverPort)
# INFO: Isso aqui vai abrir 1 conexão.
serverSocket.listen(1)

#Fill in end 
 
while True: 
    # Estabelece a conexão 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()
 
    try: 
        # Recebe a mensagem do cliente (requisição HTTP) 
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]   
        f = open(filename[1:]) 
        outputdata = f.read 
 
        # Envia a linha de status do cabeçalho HTTP 
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
 
        # Envia o conteúdo do arquivo ao cliente 
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send("\r\n".encode()) 
 
        # Fecha a conexão com o cliente 
        connectionSocket.close() 
 
    except IOError: 
        # Envia mensagem de erro 404 se o arquivo não for encontrado 
        #Fill in start 
        #Fill in end 
 
        # Fecha o socket do cliente 
        #Fill in start 
        #Fill in end 
 
serverSocket.close() 
sys.exit()  # Encerra o programa