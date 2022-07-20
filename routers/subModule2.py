from fastapi import APIRouter

router = APIRouter(
    prefix="/sub2",
    tags=["sub2"]
)


@router.get("/test1/")
async def test1():
    return {"message": "sub2 test1"}