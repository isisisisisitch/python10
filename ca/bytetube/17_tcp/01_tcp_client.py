import socket

if __name__ == '__main__':
    # 1.创建客户端套接字对象
    #1.1ip的地址类型 AF_INET ipv4
    #1.2 ocket.SOCK_STREAM tcp协议
     tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2.和服务端套接字建立连接
     tcp_client_socket.connect(("",9090))
     #3.发送数据
     #3.1 准备数据
     send_content = "hello,bytetube"
     send_data = send_content.encode("utf-8")
     tcp_client_socket.send(send_data)
     #4.接收数据
     recv_data = tcp_client_socket.recv(1024)
     recv_content = recv_data.decode("utf-8")
     print(recv_content)
     #5.关闭客户端套接字
     tcp_client_socket.close()