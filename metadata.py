import json
import re

class Metadata:
    def __init__(self, payload_path: str = None, headers_path: str = None):
        self.payload = {}
        self.headers = ""
        if payload_path:
            self.load_json(payload_path)
        if headers_path:
            self.load_txt(headers_path)
    
    def load_json(self, payload_path: str):
        """Loads JSON metadata into payload."""
        with open(payload_path, 'r', encoding='utf-8') as f:
            self.payload = json.load(f)
    
    def load_txt(self, headers_path: str):
        """Loads TXT file and stores headers as a raw string."""
        with open(headers_path, 'r', encoding='utf-8') as f:
            self.headers = f.read()
    
    def get_header(self) -> str:
        """Returns stored headers as a raw string."""
        return self.headers.replace('\n', ' ')
    
    def get_payload(self) -> dict:
        """Returns stored JSON payload."""
        return self.payload.copy()
    
    def update_header(self, key: str, value):
        """Updates or adds a header property in the raw text format."""
        header_lines = self.headers.splitlines()
        updated = False
        for i, line in enumerate(header_lines):
            if line.startswith(f"{key}:"):
                header_lines[i] = f"{key}: {value}"
                updated = True
                break
        if not updated:
            header_lines.append(f"{key}: {value}")
        self.headers = "\n".join(header_lines)
    
    def update_property(self, key: str, value):
        """Updates or adds a property in payload."""
        self.payload[key] = value

    def delete_header(self, key: str):
        """Deletes a header property by key."""
        header_lines = self.headers.splitlines()
        self.headers = "\n".join(line for line in header_lines if not line.startswith(f"{key}:"))
    
    def delete_property(self, key: str):
        """Deletes a property from the payload by key."""
        self.payload.pop(key, None)
    
    def get_header_json(self) -> dict:
        """Returns headers as a JSON-compatible dictionary."""
        # return dict(re.findall(r'([^:]+):\s*(.*)', self.headers.replace('\n', ' ')))
        header_lines = self.headers.splitlines()
        header_dict = {}
        for line in header_lines:
            # Split each header line into key and value and clean up any extra spaces
            match = re.match(r'([^:]+):\s*(.*)', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip()
                header_dict[key] = value
        return header_dict

    def __repr__(self):
        return f"Metadata(headers={len(self.headers)} chars, payload={len(json.dumps(self.payload))} chars)"