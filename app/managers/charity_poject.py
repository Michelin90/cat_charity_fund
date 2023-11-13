from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.managers.base import CRUDBase
from app.models import CharityProject


class CahrityProjectCRUD(CRUDBase):

    async def get_charity_project_by_name(
        self,
        charity_project_name,
        session: AsyncSession
    ) -> CharityProject:
        charity_project = await session.execute(
            select(CharityProject).where(
                CharityProject.name == charity_project_name
            )
        )
        charity_project = charity_project.scalars().first()
        return charity_project


charity_project_crud = CahrityProjectCRUD(CharityProject)
