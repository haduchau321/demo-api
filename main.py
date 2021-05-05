from fastapi import FastAPI
# import uvicorn
from pydantic import BaseModel

class myghi(BaseModel):
    name:str
    passwrod:str
    trangthai:str = False

app = FastAPI()

@app.get('/home')
async def home():
    data = {'name':'haduchau','password':'yeutaodi123'}
    return data

@app.post('/dangki')
async def submit(out:myghi):
    name = out.name
    passwrod = out.passwrod
    trangthai = out.trangthai
    print(name,passwrod,trangthai)
    return out,True


# if __name__ == '__main__':
#     uvicorn.run(app)
