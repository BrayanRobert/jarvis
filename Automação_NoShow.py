import requests
import pprint as pp
import json

# Puxando relatório de ocupação das agendas do intervalo de 23 dias


str_hoje = '19/06/2022'
str_intervalo = '19/06/2022'

print(str_hoje)
print(str_intervalo)

loop = [3,4,5,6,7,10,11,13,14,15,16,18,21,22,23,24,25,26,27,28,29,31,34,37,38,41,46,59,68,71,74]
#3,4,5,6,7,10,11,13,14,15,16,18,21,22,23,24,25,26,27,28,29,31,33,34,37,38,41,46,59,68,71,74
# Obs: Geralmente aos Domingos só tem a especialidade 6
# Obs: 54 e 58 não têm agenda
# Especialidades não usadas em No-Show: 8,9,69,2,32,52,42,57,77,301

#&ESPECIALIDADE_IDS[]={i}
nome = "Brayan Robert Oliveira dos Santos"
noti = "Olá! " + nome + ", sentimos a sua falta no agendamento de ontem. Está tudo bem? Estou aqui pra te ajudar a REAGENDAR. Qual o melhor dia pra você?"

for i in loop:
    url = f"https://api.feegow.com/v1/api/reports/generate?DATA_INICIO={str_hoje}&DATA_FIM={str_intervalo}&EXECUCAO_ITEM[]=S&ESPECIALIDADE_IDS[]={i}&report=schedule-appointments"
    header = {'Content-Type': 'application/json',
              'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmZWVnb3ciLCJhdWQiOiJwdWJsaWNhcGkiLCJpYXQiOiIwOS0wMS0yMDIwIiwibGljZW5zZUlEIjoiODI4OSJ9.sJU57cGbJq-wMPQbm5gCH1HtrnV7xMsh6RVfH5m1DtE'
              }

    r = requests.post(url,data=header)
    l = r.json()
    if not l['data']:
      continue

    pp.pprint(l)
    pp.pprint(i)

    # print(url)

    # -------------------------------------------------------------------------

    url = f"https://segmedic.escallo.com.br/escallo/api/v1/campanha/texto/16/lista"
    for item in l["data"]:
        notificacao = "Olá! " + item['NomePaciente'] + ", sentimos a sua falta no agendamento de ontem. Está tudo bem? Estou aqui pra te ajudar a REAGENDAR. Qual o melhor dia pra você?"
        if item['StaConsulta'] == "Não compareceu":
            payload = json.dumps({
                "expiraLista": 60000,
                "cancelarPendentes": False,
                "contatos": [
                    {
                        "contato": item['Cel1'],
                        "cliente": item['NomePaciente'],
                        "idExterno": 1,
                        "notificacao": notificacao
                    }]
            })

            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Partner a7d45f88c03a2d1e1d77772d5c400c75'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.json())

url = f"https://segmedic.escallo.com.br/escallo/api/v1/campanha/texto/16/lista"

payload = json.dumps({
  "expiraLista": 60000,
  "cancelarPendentes": False,
  "contatos": [
    {
      "contato": "21985010838",
      "cliente": nome,
      "idExterno": 1,
      "notificacao": noti
    }]
})

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Partner a7d45f88c03a2d1e1d77772d5c400c75'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

