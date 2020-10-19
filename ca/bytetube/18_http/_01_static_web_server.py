#version 1 返回固定页面
import socket

if __name__ == '__main__':
    #1.创建服务器端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2.设置端口号复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    #3.绑定端口号
    tcp_server_socket.bind(("127.0.0.1",8000))
    #4.设置监听
    tcp_server_socket.listen(128)
    #5。循环等待接受客户端的连接请求
    while True:
       new_client,ip_port = tcp_server_socket.accept()

       recv_data = new_client.recv(4096)

       print(recv_data)

       #6.准备响应回复
       # 6.1打开文件读取文件中数据
       with open("static/index.html", "r") as file:
           file_data = file.read()

        #6.2 设置响应行
       response_line = "HTTP/1.1 200 OK\r\n"
        #6.3 设置响应头
       response_header = "Server: Tengine\r\n"
        #6.4 设置响应体
       response_body = file_data

       #7.把数据封装成http响应报文形式
       respnse = response_line + response_header + "\r\n" + response_body

       #8.将respnse编码
       respnse_data = respnse.encode("utf-8")

       #9.发送response响应报文给浏览器
       new_client.send(respnse_data)

       #10.关闭套接字
       new_client.close()