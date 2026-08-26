"""SPACE-READ minimal external read API.

Read-only reference implementation over the existing publication contract.
No Core credentials, imports, sockets, or write-back path are used here.
"""
from __future__ import annotations
import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "PUBLICATION_INDEX.json"
MANIFEST = ROOT / "manifest.json"

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def publication_items():
    if not INDEX.exists(): return []
    data = load_json(INDEX)
    return data if isinstance(data, list) else data.get("publications", [])

def find_item(publication_id):
    return next((x for x in publication_items() if x.get("id") == publication_id), None)

class ReadHandler(BaseHTTPRequestHandler):
    server_version = "SPACE-READ/1.0"
    def send_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"
        qs = parse_qs(parsed.query)
        if path == "/health": return self.send_json({"status":"ok","api":"SPACE-READ","mode":"read-only"})
        if path == "/manifest": return self.send_json(load_json(MANIFEST))
        if path == "/publications": return self.send_json({"publications":publication_items()})
        if path == "/search":
            q = qs.get("q", [""])[0].lower()
            return self.send_json({"query":q,"results":[x for x in publication_items() if q in json.dumps(x,ensure_ascii=False).lower()]})
        if path.startswith("/publications/"):
            item = find_item(path.split("/",2)[2])
            return self.send_json(item if item else {"error":"not_found"}, 200 if item else 404)
        return self.send_json({"error":"not_found"},404)
    def do_POST(self): self.send_json({"error":"read_only"},405)
    def do_PUT(self): self.send_json({"error":"read_only"},405)
    def do_DELETE(self): self.send_json({"error":"read_only"},405)
    def log_message(self,*_args): return

def serve(host="127.0.0.1", port=8080):
    ThreadingHTTPServer((host,port),ReadHandler).serve_forever()

if __name__ == "__main__": serve()
