from typing import Union

from fastapi import Depends, FastAPI, Cookie, Header, HTTPException

app = FastAPI()


# async def common_parameters(
#         q: Union[str, None] = None, skip: int = 0, limit: int = 100
# ):
#     return {"q":q, "skip": skip, "limit": limit}
#
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
#
# class CommonQueryParams:
#     def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
#         self.q = q
#         self.skip = skip
#         self.limit = limit
#
#
# @app.get("/items/")
# async def read_items(commons: CommonQueryParams = Depends()):
#     return commons
#
#
# @app.get("/users/")
# async def read_users(commons: CommonQueryParams = Depends()):
#     return commons
#
#
# def query_extractor(q: Union[str, None] = None):
#     return q
#
#
# def query_or_cookie_extractor(
#         q: str = Depends(query_extractor),
#         last_query: Union[str, None] = Cookie(default=None),
# ):
#     if not q:
#         return last_query
#     return q
#
#
# @app.get("/items/")
# async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
#     return {"q_or_cookie": query_or_default}


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key

app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


# async def dependency_a():
#     dep_a = generate_dep_a()
#     try:
#         yield dep_a:
#     finally:
#         dep_a.close()
#
#
# async def dependency_b(dep_a=Depends(dependency_a)):
#     dep_b = generate_dep_b()
#     try:
#         yield dep_b:
#     finally:
#         dep_b.close(dep_a)
#
#
# async def dependency_c(dep_b=Depends(dependency_b)):
#     dep_c = generate_dep_c()
#     try:
#         yield dep_c:
#     finally:
#         dep_c.close(dep_b)

