from sqlalchemy import MetaData, Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class Book(Base):
    __tablename__ = 'book'

    book_id = Column(Integer, primary_key=True)
    title = Column(String(256))
    author = Column(String(256))
    date_published = Column(Date, nullable=False, server_default='1999-01-01')
    created = Column(DateTime(timezone=False),nullable=False,default=func.now())


    def __repr__(self):
        return (f"<Book(book_id={self.book_id},"
                f"title={self.title},"
                f"author={self.author},"
                f"date_published={self.date_published},"
                f"created={self.created})>")
