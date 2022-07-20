from fastapi import APIRouter

router = APIRouter(
    prefix="/sub1",
    tags=["sub1"]
)


@router.get("/test1")
async def test1():
    return {"message": "sub1 test1"}


@router.get("/test2")
async def test2():
    return {"message": "sub1 test2"}
