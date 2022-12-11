from fastapi import APIRouter
from typing import List

class APIRouterList(APIRouter):
    def __init__(self, routes: List[APIRouter]=[], **kws):
        super().__init__(**kws)
        for route in routes:
            self.include_router(route)