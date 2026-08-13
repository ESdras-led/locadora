#teste 123
from fastapi import FastAPI
from database import conectar

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "api funcionando"}

@app.get("/diretores")
def listar_diretores():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM diretores")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

@app.post("/diretores")
def adicionar_diretores(nome: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("insert into diretores (nome) values (%s)", (nome,))
    conexao.commit()
    cursor.close()
    conexao.close()

@app.delete("/diretores/{id}")
def deletar_diretores(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("delete from diretores where id = %s ", (id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return {"mensagem": f"diretor {id} excluido com sucesso"}

@app.put("/diretores/{id}")
def update_diretores(id: int, nome: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("update diretores set nome = %s where id = %s", (nome,id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return {"mensagem": f"mudança salva"}
