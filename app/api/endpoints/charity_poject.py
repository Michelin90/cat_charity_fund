from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_charity_project_exists,
                                check_charity_project_is_closed,
                                check_charity_project_is_invested,
                                check_charity_project_name_is_not_unique,
                                check_new_full_amount_greater_then_old)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.managers.charity_poject import charity_project_crud
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)

router = APIRouter(
    prefix='/charity_project',
    tags=['Charity_Project']
)


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_charity_project(
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session)
):
    """Только для суперюзеров."""
    await check_charity_project_name_is_not_unique(
        charity_project.name, session
    )
    new_charity_project = await charity_project_crud.create(
        charity_project, session
    )
    return new_charity_project


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session)
):
    charity_projects = await charity_project_crud.get_multi(session)
    return charity_projects


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    charity_project = await check_charity_project_exists(project_id, session)
    check_charity_project_is_closed(charity_project.fully_invested)
    if obj_in.name is not None:
        await check_charity_project_name_is_not_unique(obj_in.name, session)
    if obj_in.full_amount is not None:
        check_new_full_amount_greater_then_old(
            invested_amount=charity_project.invested_amount,
            new_full_amount=obj_in.full_amount,
        )
    charity_project = await charity_project_crud.update(
        db_obj=charity_project,
        obj_in=obj_in,
        session=session
    )
    return charity_project


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def delete_charity_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    charity_project = await check_charity_project_exists(project_id, session)
    check_charity_project_is_invested(charity_project.invested_amount)
    charity_project = await charity_project_crud.remove(
        charity_project, session
    )
    return charity_project
