"""utils/config.py — loads config from environment variables or config.yaml"""
import os
import yaml

class Config:
    def __init__(self, path="config/config.yaml"):
        self._data = {}
        if os.path.exists(path):
            with open(path) as f:
                self._data = yaml.safe_load(f) or {}

    def get(self, key, default=None):
        return os.getenv(key.upper(), self._data.get(key, default))
