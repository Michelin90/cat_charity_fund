from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.managers.charity_poject import charity_project_crud
from app.models import CharityProject


async def check_charity_project_name_is_not_unique(
    name: str, session: AsyncSession
) -> None:
    charity_project = await (
        charity_project_crud.get_charity_project_by_name(
            name,
            session
        )
    )
    if not charity_project:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проект с таким именем уже существует!'
        )


async def check_charity_project_exists(
    poject_id: int, session: AsyncSession
) -> CharityProject:
    charity_project = await charity_project_crud.get(
        poject_id, session
    )
    if not charity_project:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Проект не найден!'
        )
    return charity_project


def check_new_full_amount_greater_then_old(
    invested_amount: str, new_full_amount: str
) -> None:
    if new_full_amount < invested_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Нельзя установить требуемую сумму меньше уже вложенной!'
        )


def check_charity_project_is_closed(fully_invested: bool) -> None:
    if fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Закрытый проект нельзя редактировать!'
        )


def check_charity_project_is_invested(invested_amount: int) -> None:
    if invested_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='В проект были внесены средства, не подлежит удалению!'
        )
