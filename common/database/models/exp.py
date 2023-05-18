from sqlalchemy import String
from sqlalchemy.orm import mapped_column

from common.database.models.db.base import Base


def get_only_def():
    return "only client side default"

def get_def():
    return "client side default"


class Dbg(Base):
    __tablename__ = "dbg"

    a = mapped_column(String(length=50),
                      default=get_only_def,
                      nullable=False)
    b = mapped_column(String(length=50),
                      server_default="only server side default",
                      nullable=False)
    c = mapped_column(String(length=50),
                      default=get_def,
                      server_default="server side default",
                      nullable=False)
