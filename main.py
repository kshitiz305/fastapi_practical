from typing import Optional

from fastapi import FastAPI



app = FastAPI()


BOOKS = {1:"FIRST",2:"SECOND"
         }


@app.get('/assignment')
async def read_book(bookname:Optional[int]= None):
    if bookname:
        return BOOKS[bookname]
    return BOOKS


# @app.get('/')
# async def get_book():
#     return "Hello User"



# run using uvicorn main:app -- reload

