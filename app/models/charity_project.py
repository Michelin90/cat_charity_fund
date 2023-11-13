from sqlalchemy import Column, String, Text

from app.models.invest_base import InvestBase


class CharityProject(InvestBase):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
