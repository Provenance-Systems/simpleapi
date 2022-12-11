from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from .api_wrapper import APIWrapper

class CorsAPI(APIWrapper):
    def __init__(self, 
        origins: List[str]=['*'], 
        methods: List[str]=['*'], 
        headers: List[str]=['*'], 
        middleware: List[Dict]=[], 
        **kws
    ):
        super().__init__(middleware=[
            {
                "middleware_class": CORSMiddleware,
                "allow_origins": origins,
                "allow_credentials": '*' not in origins,
                "allow_methods": methods,
                "allow_headers": headers
            }, *middleware
        ], **kws)