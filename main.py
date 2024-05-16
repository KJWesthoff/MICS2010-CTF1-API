from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
app = FastAPI()


@app.get('/')
def read_root():
    return {"Hello": "Fast Api World Test"}



@app.get('/math', response_class=PlainTextResponse )
def read_simplemaths(op,x:int,y:int):
    if op == "plus":
        res = x+y
    if op == "mult":
        res = x*y 
    
    return(str(res))
    
    
    
    
    
    
    