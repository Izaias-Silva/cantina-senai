import os

AMBIENTE = os.getenv("AMBIENTE", "dev")

BANCOS = {
    "dev": "cantina_dev.db",
    "teste": "cantina_teste.db",
    "homolog": "cantina_homolog.db",
    "prod": "cantina_prod.db",
}

if AMBIENTE not in BANCOS:
    print("ERRO: ambiente desconhecido:", AMBIENTE)
    print("Use um destes:", list(BANCOS))
    exit()


BANCO = BANCOS [AMBIENTE]
print("Rodando no ambiente:", AMBIENTE, "| banco:", BANCO)