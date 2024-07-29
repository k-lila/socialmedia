import os
import subprocess


def application(environ, start_response):
    try:
        os.chdir("/home/klila/socialmedia")

        subprocess.run(["git", "pull"])
        subprocess.run(["touch", "/var/www/klila_pythonanywhere_com_wsgi.py"])

        status = "200 OK"
        output = b"Deploy completed successfully!"
    except Exception as e:
        status = "500 Internal Server Error"
        output = str(e).encode("utf-8")

    response_headers = [
        ("Content-type", "text/plain"),
        ("Content-Length", str(len(output))),
    ]
    start_response(status, response_headers)

    return [output]
