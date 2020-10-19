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

      #对二进制数据进行解码
       recv_content = recv_data.decode("utf-8")
       #对数据按照空格切割
       request_list = recv_content.split(" ",maxsplit=2)
       #获取请求路径
       request_path = request_list[1]

       #判断请求是否是根目录，如果是根目录直接设计返回值
       if request_path == "/":
           request_path = "/index.html"

       try:
           #6.准备响应回复
           # 6.1打开文件读取文件中数据
           with open("static"+ request_path, "rb") as file:
               file_data = file.read()

       except Exception as e:
           response_line = "HTTP/1.1 404 NOT Found\r\n"
           response_header = "Server: Tengine\r\n"
           with open("static/error.html", "rb") as file:
               file_data = file.read()

               response_body = file_data
               # 7.把数据封装成http响应报文形式
               respnse = (response_line + response_header + "\r\n").encode("utf-8") + response_body

               new_client.send(respnse)

       else:
            #6.2 设置响应行
           response_line = "HTTP/1.1 200 OK\r\n"
            #6.3 设置响应头
           response_header = "Server: Tengine\r\n"
            #6.4 设置响应体
           response_body = file_data

           #7.把数据封装成http响应报文形式
           respnse = (response_line + response_header + "\r\n").encode("utf-8") + response_body

           #8.将respnse编码
           #respnse_data = respnse.encode("utf-8")

           #9.发送response响应报文给浏览器
           new_client.send(respnse)

           #10.关闭套接字
       finally:
           new_client.close()