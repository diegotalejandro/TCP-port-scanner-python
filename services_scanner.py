import socket as sc
    
def obtenerBanner(ip,puerto):
        sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        try:   
            sock.connect((ip, puerto))
            result = sock.recv(1024)
            sock.close()
            print 'Respuesta:', result
        except Exception, e:
            print 'Error en %s:%d \nException type is %s' % (ip, puerto, `e`)

if __name__ == '__main__':
    ip_destino = "10.0.2.4"
    lista_puerto_destino = [21,22,1524,2121,3306]
    for puerto_destino in lista_puerto_destino:
	print("Puerto: " + str(puerto_destino))
    	obtenerBanner(ip_destino,puerto_destino)
