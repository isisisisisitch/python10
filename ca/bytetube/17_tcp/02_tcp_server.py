import socket

if __name__ == '__main__':
  #1.创建服务端端套接字对象
  tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #2.绑定端口号
  tcp_server_socket.bind(("",9090))
  #3.设置监听
  tcp_server_socket.listen(128)
  #4.等待接受客户端的连接请求
  #4.1每次当客户端成功与服务器连接时，新创建当套接字
  #绝对的注意事项：tcp_server_socket 只负责等待客户端的连接请求，收发信息不使用该套接字
  new_client, ip_port = tcp_server_socket.accept()
  #5.接收数据
  recv_data = new_client.recv(1024)
  recv_content = recv_data.decode("utf-8")
  print("recv_content from client:", recv_content)
  #6.发送数据
  send_content = "hello,client"
  send_data = send_content.encode("utf-8")
  new_client.send(send_data)
  #7.关闭套接字
  new_client.close()
  tcp_server_socket.close()