# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import socket
print("fuck")
# 创建 socket
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定 IP 和端口号
sk.bind(('127.0.0.1', 6000))
while True:
    # 接收数据报
    msg, addr = sk.recvfrom(1024)
    # 打印
    print('来自[%s:%s]的消息: %s' % (addr[0], addr[1], msg.decode('utf-8')))

    # 等待输入
    inp = input('>>>')
    # 发送数据报
    sk.sendto(inp.encode('utf-8'), addr)

# 关闭 socket
sk.close()
