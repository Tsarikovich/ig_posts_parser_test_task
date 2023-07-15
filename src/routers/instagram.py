from fastapi import APIRouter
from ..dependencies import instagramParserAPI

router = APIRouter(prefix='/api/v1', tags=['/api/v1'])


@router.get(
    '/getPhotos',
    response_model=dict[str, list[str]],
)
async def get_photos(
        username: str, max_count: int
) -> dict[str, list[str]]:
    return instagramParserAPI.get_photos(username, max_count)
