import socket

if __name__ == '__main__':
  #1.创建服务端端套接字对象
  tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #设置端口号复用：服务器端程序退出端口号时，立即释放
  #SOL_SOCKET:当前套接字
  #SO_REUSEADDR：表示复用端口号的选项
  #True：确定复用
  tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
  #2.绑定端口号
  tcp_server_socket.bind(("127.0.0.1", 9090))
  #3.设置监听 1
  #128表示最大的等待建立连接的个数
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