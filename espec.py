def modalidade(i):
        if i == 3:
          nome = "MAMOGRAFIA"
          return nome
        if i == 4:
          nome = "TOMOGRAFIA"
          return nome
        if i == 5:
          nome = "CARDIOLOGIA"
          return nome
        if i == 6:
          nome = "PEDIATRIA"
          return nome
        if i == 7:
          nome = "ENDOCRINOLOGIA"
          return nome
        if i == 10:
          nome = "ALERGOLOGIA"
          return nome
        if i == 11:
          nome = "ANGIOLOGIA"
          return nome
        if i == 13:
          nome = "OTORRINOLARINGOLOGIA"
          return nome
        if i == 14:
          nome = "GERIATRIA"
          return nome
        if i == 15:
          nome = "DERMATOLOGIA"
          return nome
        if i == 16:
          nome = "GASTROENTEROLOGIA"
          return nome
        if i == 18: 
          nome = "PNEUMOLOGIA"
          return nome
        if i == 21: 
          nome = "GINECOLOGIA"
          return nome
        if i == 22: 
          nome = "NUTRIÇÃO"
          return nome          
        if i == 23: 
          nome = "NEUROLOGIA"
          return nome
        if i == 24: 
          nome = "UROLOGIA"
          return nome        
        if i == 25: 
          nome = "PROCTALOGIA"
          return nome
        if i == 26: 
          nome = "REUMATOLOGIA"
          return nome
        if i == 27: 
          nome = "MAPA"
          return nome
        if i == 28: 
          nome = "HOLTER"
          return nome
        if i == 29: 
          nome = "TESTE ERGOMETRICO"
          return nome
        if i == 31: 
          nome = "NEFROLOGIA"
          return nome
        if i == 33: 
          nome = "PSICOLOGIA"
          return nome
        if i == 34: 
          nome = "DENSITOMETRIA OSSEA"
          return nome
        if i == 37: 
          nome = "PSIQUIATRIA"
          return nome
        if i == 38: 
          nome = "MASTOLOGIA"
          return nome
        if i == 41: 
          nome = "ECOCARDIOGRAMA"
          return nome
        if i == 46: 
          nome = "ELETROCENFALOGRAMA"
          return nome
        if i == 59: 
          nome = "HEMATOLOGIA"
          return nome
        if i == 68: 
          nome = "CIRURGIA GERAL"
          return nome
        if i == 71: 
          nome = "AUDIOMETRIA"
          return nome
        if i == 74: 
          nome = "MEDICINA DA FAMÍLIA"
          return nome
  
def request_e(notific, celular, nome_paciente):

  import json
  import requests 

  url_escallo = f"https://segmedic.escallo.com.br/escallo/api/v1/campanha/texto/16/lista"
  headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Partner a7d45f88c03a2d1e1d77772d5c400c75'
              }

  payload = json.dumps({
                    "expiraLista": 6000,
                    "cancelarPendentes": False,
                    "contatos": [
                        {
                            "contato": celular,
                            "cliente": nome_paciente,
                            "idExterno": 1,
                            "notificacao": notific
                        }]
                })

  response = requests.post(url_escallo, headers=headers, data=payload)
  print(f'SUCESSO | PROCESSANDO |STATUS:{response.status_code}')

  
