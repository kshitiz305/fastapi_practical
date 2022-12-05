from fastapi import FastAPI



app = FastAPI()


BOOKS = {1:"FIRST",2:"SECOND"
         }


@app.get('/')
async def get_book():
    return "Hello User"

@app.get('/{bookname}')
async def read_book(bookname:int):
    return BOOKS[bookname]



# run using uvicorn main:app -- reload

