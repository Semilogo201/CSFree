from uuid import uuid4

class  BaseModel:
    def __init__(self): #private instance attribute and if _ it is protected and if nothing, it is public.
        sef..id = str(uuid()) #json only works with strings