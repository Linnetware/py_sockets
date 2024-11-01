import socket

#PDU service request message structure:
# ID      = 0x0EF50CD4;
# LENGTH  = 0x03;
# PAYLOAD = 0x22 0xF1 0xB0;

#pdu_service_request  = "0EF50CD40322F1B0"
#pdu_service_response = "0CD40EF50462F1B0D4"
#pdu_service_response = [0x0C, 0xD4, 0x0E, 0xF5, 0x04, 0x62, 0xF1, 0xB0, 0xD4]
#pdu_service_rqst     = [0x0E, 0xF5, 0x0C, 0xD4, 0x03, 0x22, 0xF1, 0xB0]

pdu_id = [0x0E, 0xF5, 0x0C, 0xD4]
pdu_ln = [0x03]
pdu_pl = [0x22, 0xF1, 0xB0]
pdu_serv_ui = pdu_id + pdu_ln + pdu_pl
pdu_service_ui = map(str,pdu_serv_ui)
pdu_service_request = ", ".join(pdu_service_ui)


def client_program():
    host = socket.gethostname()
    port = 5000
    
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("Client socket info: " + str(client_socket))
    message = pdu_service_request

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        
        #data = client_socket.recv(1024)
        data = client_socket.recv(1024)
        print("Received from server: ")
        print(data)
        message = input(" -> ")
        if(message.lower().strip() == 'y'):
            message = pdu_service_request
    
    client_socket.close()

if __name__ == '__main__':
    client_program()