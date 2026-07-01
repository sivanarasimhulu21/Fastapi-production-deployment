from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

app = FastAPI(title="Book Catalog UI")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)


Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/", response_class=HTMLResponse)
def home():

    db = SessionLocal()

    books = db.query(Book).all()

    html = """
    <html>
    <head>
        <title>Book Catalog</title>
    </head>

    <body style="font-family: Arial; margin: 40px;">

        <h1>Book Catalog</h1>

        <form action="/add-book" method="post">

            <input type="text" name="title" placeholder="Book Title" required>

            <input type="text" name="author" placeholder="Author" required>

            <button type="submit">Add Book</button>

        </form>

        <hr>

        <h2>Books List</h2>

        <ul>
    """

    for book in books:
        html += f"""
        <li>
            <b>{book.title}</b> by {book.author}

            <form action="/delete-book/{book.id}" method="post" style="display:inline;">
                <button type="submit">Delete</button>
            </form>
        </li>
        """

    html += """
        </ul>

    </body>
    </html>
    """

    return html


@app.post("/add-book")
def add_book(
    title: str = Form(...),
    author: str = Form(...)
):

    db = SessionLocal()

    new_book = Book(
        title=title,
        author=author
    )

    db.add(new_book)
    db.commit()

    return RedirectResponse("/", status_code=303)


@app.post("/delete-book/{book_id}")
def delete_book(book_id: int):

    db = SessionLocal()

    book = db.query(Book).filter(Book.id == book_id).first()

    if book:
        db.delete(book)
        db.commit()

    return RedirectResponse("/", status_code=303)
