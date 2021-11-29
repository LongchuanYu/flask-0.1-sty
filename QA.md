## Flask是如何把 Flask App 传给werkzeug的？ 或者说如何与werkzeug产生连接的？
_request_ctx_stack

## socket用makefile代替sock.recv和sock.send的理由？

## socket发送http回复，如何发送body
参照HTTP协议消息体，报头后面跟空格，再跟body
例如：
```
HTTP/1.0 200 OK
Content-type: text/plain
Content-Length: 10
Response Body

ly test
```

## socket ctrl+c 关闭后再开，报错：Address already in use，如何优雅的关闭？