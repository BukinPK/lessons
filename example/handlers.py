import starlette.responses
import starlette.requests
import starlette.exceptions
import core


async def homepage(request):
    return starlette.responses.JSONResponse({'hello': 'world'})


async def get_user_by_id(request: starlette.requests.Request):
    _id = request.query_params.get("id")
    if not _id:
        raise starlette.exceptions.HTTPException(400, "id is not provided")
    _id = int(_id)
    result = core.User().get_by_id(_id=_id)
    return starlette.responses.JSONResponse(result)


async def create(request: starlette.requests.Request):
    name = request.get("name")
    result = core.User().create(name=name)
    return starlette.responses.JSONResponse(result)
