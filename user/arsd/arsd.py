#!/usr/bin/env python3
import socket
import os
import time
from ars_core import ARSKernel

SOCK_PATH = '/run/ars.sock'

class ARSDaemon:
    def __init__(self):
        self.kernel = ARSKernel()
        # ensure runtime dir
        os.makedirs('/run', exist_ok=True)

    def start(self):
        # Simple unix socket server - accepts JSON commands
        if os.path.exists(SOCK_PATH):
            os.remove(SOCK_PATH)
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.bind(SOCK_PATH)
        s.listen(1)
        print('ARSD: listening on', SOCK_PATH)
        while True:
            conn, _ = s.accept()
            data = conn.recv(4096).decode('utf-8')
            if data.strip() == 'run':
                res = self.kernel.run_steps(10)
                conn.sendall(str(res).encode('utf-8'))
            else:
                conn.sendall(b'unknown')
            conn.close()

if __name__ == '__main__':
    ARSDaemon().start()