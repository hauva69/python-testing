#!/usr/bin/env python3

"""A simple HTTP reverse proxy in Python."""

from http.server import BaseHTTPRequestHandler,HTTPServer
import argparse, logging, os, random, sys, requests

from socketserver import ThreadingMixIn
import threading

logging.basicConfig(level=logging.DEBUG)

hostname = 'en.wikipedia.org'

def merge_two_dicts(x, y):
    return x.update(y)

def set_header():
    headers = {
        'Host': hostname
    }

    return headers

class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.0'
    def do_HEAD(self):
        self.do_GET(body=False)
        return

    def do_GET(self, body=True):
        logging.debug('self.path=%s', self.path)
        sent = False
        try:
            url = 'https://{}{}'.format(hostname, self.path)
            req_header = self.parse_headers()

            logging.debug('req_header=%s', req_header)
            logging.debug('url=%s', url)
            resp = requests.get(url,
                                headers=merge_two_dicts(req_header, set_header()),
                                verify=False)
            logging.debug('resp=%s', resp)
            sent = True

            self.send_response(resp.status_code)
            self.send_resp_headers(resp)
            msg = resp.text
            logging.debug('msg=%s', msg)
            if body:
                self.wfile.write(msg.encode(encoding='UTF-8',errors='strict'))
            return
        finally:
            if not sent:
                self.send_error(404, 'error trying to proxy GET')

    def do_POST(self, body=True):
        sent = False
        try:
            url = 'https://{}{}'.format(hostname, self.path)
            content_len = int(self.headers.getheader('content-length', 0))
            post_body = self.rfile.read(content_len)
            req_header = self.parse_headers()

            resp = requests.post(url,
                                 data=post_body,
                                 headers=merge_two_dicts(req_header, set_header()),
                                 verify=False)
            sent = True

            self.send_response(resp.status_code)
            self.send_resp_headers(resp)
            if body:
                self.wfile.write(resp.content)
            return
        finally:
            if not sent:
                self.send_error(404, 'error trying to proxy POST')

    def parse_headers(self):
        req_header = {}
        for line in self.headers:
            line_parts = [o.strip() for o in line.split(':', 1)]
            if len(line_parts) == 2:
                req_header[line_parts[0]] = line_parts[1]
        return req_header

    def send_resp_headers(self, resp):
        respheaders = resp.headers
        logging.debug('Response Header')
        for key in respheaders:
            if key not in [
                'Content-Encoding',
                'Transfer-Encoding',
                'content-encoding',
                'transfer-encoding',
                'content-length',
                'Content-Length']:
                logging.debug(key, respheaders[key])
                self.send_header(key, respheaders[key])
        self.send_header('Content-Length', len(resp.content))
        self.end_headers()

def parse_args(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Proxy HTTP requests')
    parser.add_argument('--port', dest='port', type=int, default=9999,
                        help='serve HTTP requests on specified port (default: random)')
    parser.add_argument('--hostname', dest='hostname', type=str, default=hostname,
                        help=f'hostname to be processd (default: {hostname})')
    args = parser.parse_args(argv)
    return args

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

def _main():
    global hostname
    port = 8000
    logging.info('http server is starting on {} port {}...'.format(hostname, port))
    server_address = ('127.0.0.1', port)
    httpd = ThreadedHTTPServer(server_address, ProxyHTTPRequestHandler)
    logging.info('http server is running as reverse proxy')
    httpd.serve_forever()

def main(argv=sys.argv[1:]):
    global hostname
    logging.debug('hostname=aseqa.poliisi.fi')
    args = parse_args(argv)
    hostname = args.hostname
    logging.info('http server is starting on {} port {}...'.format(args.hostname, args.port))
    server_address = ('127.0.0.1', args.port)
    httpd = ThreadedHTTPServer(server_address, ProxyHTTPRequestHandler)
    logging.info('http server is running as reverse proxy')
    httpd.serve_forever()

if __name__ == '__main__':
    try:
        _main()
    except KeyboardInterrupt:
        logging.info('KeyboardInterrupt, exiting')
        sys.exit(0)
