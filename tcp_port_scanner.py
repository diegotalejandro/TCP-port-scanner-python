from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

ip_destino = "192.168.100.1"  # IP local
lista_puerto_destino = [21,22,23,24,80,443]#59096 #Puerto destino

def scanner(puerto_destino):
    puerto_origen = RandShort()  # Puerto random
    print("Puerto de destino:",puerto_destino)
    respuesta_paquete_tcp = sr1(IP(dst=ip_destino)/TCP(sport=puerto_origen,
    dport=puerto_destino, flags="S"), timeout=10) #Envio Paquete TCP con el flag S y un timeout de 10
    #En caso de no recibir respuesta, definimos que el puerto esta filtrado al no recibir un RST
    if(str(type(respuesta_paquete_tcp)) == "<class 'NoneType'>"):
        print("Filtrado")    
    #Se revisa si es un paquete TCP
    elif(respuesta_paquete_tcp.haslayer(TCP)):
        #En este caso el flag es un SYN + ACK, los cuales corresponden a abierto
        if(respuesta_paquete_tcp.getlayer(TCP).flags == 0x12):        
            send_rst = sr(IP(dst=ip_destino)/TCP(sport=puerto_origen,
            dport=puerto_destino, flags="R"), timeout=10)
            print("Abierto")
        # Flag de paquete para un puerto cerrado
        elif (respuesta_paquete_tcp.getlayer(TCP).flags == 0x14):
            print( "Cerrado")
    #Tambien puede ocuerrir que el puerto filtrado mande un paquete ICMP
    elif(respuesta_paquete_tcp.haslayer(ICMP)):
        if(int(respuesta_paquete_tcp.getlayer(ICMP).type) == 3 and int(respuesta_paquete_tcp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]):
            print("Filtrado")

for i in lista_puerto_destino:
    scanner(i)
    print("\n\n")
