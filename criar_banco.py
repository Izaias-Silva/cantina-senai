import sqlite3
from config import BANCO

con = sqlite3.connect(BANCO)

con.execute ("DROP TABLE IF EXISTS alunos")

con.execute("CREATE TABLE IF NOT EXISTS alunos (nome TEXT, saldo REAL)")

massa = [
    ("Ana", 0.0),
    ("Bia", 4.99),
    ("Caio", 5.0),
    ("Duda", 50.0),
    ("Edu", -2.0),
    ("Felipe", 5.01),
    ("Gabi", 0.01),
]

con.executemany("INSERT INTO alunos VALUES (?,?)", massa)
con.commit()

total = con.execute("SELECT COUNT(*) FROM alunos").fetchone()[0]

print("Alunos no banco:", total)

for nome, saldo in con.execute("SELECT nome, saldo FROM alunos"):
    print(nome, saldo)

con.close()