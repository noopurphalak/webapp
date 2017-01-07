def application(environ, response):
    status = "200 OK"
    response_headers = [('Content-type', 'text/plain')]
    response(status, response_headers)
    return ['Hello World!\n']
