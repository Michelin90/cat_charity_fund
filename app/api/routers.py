from fastapi import APIRouter

from app.api.endpoints import (charity_poject_router, donation_router,
                               user_router)

main_router = APIRouter()
main_router.include_router(user_router)
main_router.include_router(charity_poject_router)
main_router.include_router(donation_router)