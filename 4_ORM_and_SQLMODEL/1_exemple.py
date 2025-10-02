from pydantic import BaseModel

class User(BaseModel):
    nome: str
    email: str
    idade: int
    
dados_usuario = {
    "nome": 'Brendon',
    "email": 'brendon@example.com', # caso houver um int aqui, ele acontece um erro
    "idade": 26
}

val_user = User(**dados_usuario)

print(val_user.json())

