import socket

#PDU service response message structure:
# ID      = 0x0CD40EF5;
# LENGTH  = 0x04;
# PAYLOAD = 0x62 0xF1 0xB0 0xD4;

#pdu_service_request = "0EF50CD40322F1B0"

pdu_service_rqst = [0x0E, 0xF5, 0x0C, 0xD4, 0x03, 0x22, 0xF1, 0xB0]
pdu_service_rqst = map (str, pdu_service_rqst)
pdu_service_request = ", ".join(pdu_service_rqst)

#pdu_service_response = "0CD40EF50462F1B0D4"
#pdu_service_response = [0x0C, 0xD4, 0x0E, 0xF5, 0x04, 0x62, 0xF1, 0xB0, 0xD4]

pdu_id = [0x0C, 0x4, 0x0E, 0xF5]
pdu_ln = [0x04]
pdu_pl = [0x62, 0xF1, 0x0, 0xD4]
pdu_rsp = pdu_id + pdu_ln + pdu_pl
pdu_rsp_ui = map(str,pdu_rsp)
pdu_service_response = ", ".join(pdu_rsp_ui)

def server_program():
    host = socket.gethostname()
    port = 5000
    
    server_socket = socket.socket()
    # bind() function takes tuple as argument
    server_socket.bind((host, port))
    # Number of clients server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  #accept new connection
    print("Connection from: " + str(address))
    print("Also to check: " + str(conn))
    while True:
        # receive data stream.
        # data packet no greater than 1024 bytes
        #data = conn.recv(1024).decode()
        data = conn.recv(1024)
        if not data:
            break
        print("Fron connected Client: ")
        print(data)
        data = data.decode()
        if data == pdu_service_request:
            data = pdu_service_response
            conn.send(data.encode())
        else:
            data = input(' -> ')
            conn.send(data.encode())
    conn.close()  # connection closed

if __name__ == '__main__':
    server_program()