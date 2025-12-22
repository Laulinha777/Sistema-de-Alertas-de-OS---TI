import requests
import time
import mysql.connector

TOKEN_TEL = "TOKEN_TELEGRAM"
CHAT_ID = "SEU_CHAT_ID"


def enviar_mensagem(msg):
    url = f"https://api.telegram.org/bot{TOKEN_TEL}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})


db = mysql.connector.connect(
        host = "localhoost",
        user = "user",
        password = "password",
        database = "name_database"
    )
    
cursor = db.cursor(dictionary = True)
    
def carregar_ultimo_id():
    try:
        with open("ultimo_id.txt", "r") as f:
            return int(f.read()TOKEN_TELEGRCHAT_ID):
        return 0
    

def salvar_ultimo_id(id_os):
    with open("ultimo_id.txt", "w") as f:
        f.write(str(id_os))

def buscar_os():
    sql = """
      SELECT 
            os.id,
            os.data_abertura,
            a.assunto AS assunto
        FROM su_oss_chamado os
        JOIN su_oss_assunto a
            ON a.id = os.id_assunto
        WHERE os.setor = id_setor
            AND os.status = 'A'
        ORDER BY os.id DESC;
"""
    cursor.execute(sql)
    return cursor.fetchone()


def verificar_novas_os():
    ultimo_id = carregar_ultimo_id()
    os = buscar_os()

    if not os:
        return 
    if os["id"] <= ultimo_id:
        return


    msg = (
         "🚨 *Nova OS para TI!* \n\n"
        f"ID: {os['id']}\n"
        f"Assunto: {os['assunto']}\n" 
        f"Abertura: {os['data_abertura']}\n"
        )
    
    enviar_mensagem(msg)
    salvar_ultimo_id(os["id"])

def main():
    print("Monitorando novas OS...\n")
    while True:
        verificar_novas_os()
        time.sleep(300)

if __name__ == "__main__":
    print("Script Iniciado!")
    main()
