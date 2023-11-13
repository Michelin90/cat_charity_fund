from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.invest_base import InvestBase


class Donation(InvestBase):
    comment = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
