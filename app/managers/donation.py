from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.managers.base import CRUDBase
from app.models import Donation, User


class DonationCRUD(CRUDBase):
    async def get_by_user(
        self, session: AsyncSession, user: User
    ) -> list[Donation]:
        donations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        donations = donations.scalars().all()
        return donations


donation_crud = DonationCRUD(Donation)
