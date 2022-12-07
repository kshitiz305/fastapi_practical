from typing import Optional
from uuid import UUID
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

BOOKS = []


class Books(BaseModel):
    id: UUID
    title: str = Field(min_length=1,max_length=100)
    author: str
    description: Optional[str] = Field(min_length=1,max_length=100,description="Mentioend the description here")
    rating: int

    class Config:
        schema_extra = {"example": {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "title": "New BoOK",
            "author": "Me",
            "description": "Whats teh description",
            "rating": 60
        }}


@app.get("/")
async def get_all_books():
    return BOOKS


@app.post("/")
async def get_book(book: Books):  # books is a class so the fast api know that it is a request bofy
    BOOKS.append(book)
    return book
