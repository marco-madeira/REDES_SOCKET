<h1 align="center"> Redes Socket </h1>

## 📖 Sobre   

Este projeto tem como objetivo a prática da programação para redes de computadores, utilizando Sockets em Python. 
O servidor será responsável por enviar três arquivos de tamanhos diferentes para o cliente. Os arquivos estão no formato 'txt' e a transmissão será realizada linha por linha, sendo remontados e salvos como arquivos de texto no lado do cliente. O envio dos arquivos deverá ser implementado tanto via TCP quanto UDP. Após o envio de cada arquivo, o servidor informará ao cliente o tempo total gasto na transmissão, em milissegundos.

## 🔧 Como executar o projeto

Estarei rodando o protocolo TCP mas para o UDP o processo é o mesmo sendo necessário apenas entrar nas pastas próprias

```bash
# Clone o repositório
git clone https://github.com/marco-madeira/REDES_SOCKET

# Entre no diretório
cd REDES_SOCKET

# Entre na pasta do Servidor
cd ServTcp

# Execute o servidor
python server_tcp.py

# Entre na pasta do Cliente
cd Client

# Execute o cliente
python Client.py

Será aberta uma interface em que você poderá qual arquivo deseja copiar, sendo permitido o envio de mais de um arquivo.
```
Lembrando que é necessario ter o python instalado em sua maquina local

!!**Por padrão estamos utilizando o comando para abrir o documento do Windows, caso utilize outro OS como Linux é necessário fazer as devidas alterações:**!!

  Dentro da pasta do Client e na pasta functions, abra o arquivo transfer_data.py com um editor de texto ou IDE, haverá uma função open_document, é necessario trocar o *'explorer'* para *'xdg-open'*. de forma que a linha de codigo ficará: 
  ```bash
subprocess.Popen(['xdg-open', f"{file_name}.txt"])
```
Faça o mesmo processo tanto para o TCP e UDP.

---
