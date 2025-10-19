from sqlalchemy import MetaData, Table, Column, Text
from sqlalchemy import create_engine, insert

engine = create_engine("sqlite:///book.db")
meta = MetaData()

book_table = Table(
    "book",
    meta,
    Column("name", Text, primary_key=True),
    Column("author", Text),
    Column("description", Text),
)

insert(book_table).values(
    name="Angels and Demons",
    author="Dan Brown",
    description="A book about Angels and Demons",
)
