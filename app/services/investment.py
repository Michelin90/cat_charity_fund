from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import InvestBase


async def make_investment(
    obj_in: InvestBase,
    db_obj: InvestBase,
    session: AsyncSession
) -> InvestBase:
    open_objects = await session.execute(
        select(db_obj).where(db_obj.fully_invested == 0)
    )
    open_objects = open_objects.scalars().all()
    for open_object in open_objects:
        donated_amount = min(
            open_object.full_amount - open_object.invested_amount,
            obj_in.full_amount - obj_in.invested_amount
        )
        open_object.invested_amount += donated_amount
        obj_in.invested_amount += donated_amount
        close_object(obj_in, open_object)
    await session.commit()
    await session.refresh(obj_in)
    return obj_in


def close_object(obj_in: InvestBase, db_object: InvestBase) -> None:
    for obj in [obj_in, db_object]:
        if obj.invested_amount == obj.full_amount:
            obj.fully_invested = True
            obj.close_date = datetime.now()
