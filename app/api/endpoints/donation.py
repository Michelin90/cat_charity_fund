from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.managers.donation import donation_crud
from app.models import CharityProject, User
from app.schemas.donation import (DonationDBSuperuser, DonationDBUser,
                                  DontationCreate)
from app.services.investment import make_investment

router = APIRouter(
    prefix='/donation',
    tags=['Donation']
)


@router.post(
    '/',
    response_model=DonationDBUser,
    response_model_exclude_none=True
)
async def create_donation(
    donation: DontationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Создает пожервтование.

    Только для авторизованных пользователей.

    """
    new_donation = await donation_crud.create(donation, session, user)
    new_donation = await make_investment(new_donation, CharityProject, session)
    return new_donation


@router.get(
    '/my',
    response_model=list[DonationDBUser],
    response_model_exclude_none=True
)
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Получает список моих пожертвований.

    Только для авторизованных пользователей.

    """
    donations = await donation_crud.get_by_user(session, user)
    return donations


@router.get(
    '/',
    response_model=list[DonationDBSuperuser],
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True
)
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
):
    """Получает список всех пожертвований.

    Только для суперюзеров.

    """
    donations = await donation_crud.get_multi(session)
    return donations
