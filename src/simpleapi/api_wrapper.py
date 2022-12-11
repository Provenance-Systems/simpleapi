from fastapi import FastAPI
from typing import List, Dict

class APIWrapper(FastAPI):
    def __init__(self, middleware: List[Dict]=[], **kws):
        super().__init__(**kws)
        for mware in middleware:
            self.add_middleware(**mware)

