from starlette.applications import Starlette
from starlette.routing import Route

import uvicorn

import handlers

app = Starlette(
    debug=True,
    routes=[
        Route('/', handlers.homepage, methods=["GET"]),
        Route('/user', handlers.get_user_by_id, methods=["GET"]),
        Route('/user', handlers.create, methods=["POST"]),
    ]
)

uvicorn.run(app)
