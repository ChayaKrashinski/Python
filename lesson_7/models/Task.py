import pydantic import BaseModel

class Task(BaseModel):
    name:constr(min_lenth=2, max_lenth=25)
    descreption:str
    @validator('descreption')
    def check_descreption(self, d):
        if d not in ['test', 'remined']:
            raise ValueError('invalid descreption')
        return d
    id:int
    @validator('id')
    def check_descreption(self, i):
        if i>200:
            raise ValueError('you can save until 200 tasks')
        return i
    status:bool
