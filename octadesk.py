import requests
import json


def Cadastro(inicio, fim, cpf, celular):
    url = "https://api.octadesk.services/persons/"
    headers = {
        'Content-Type':'application/json',
        'Authorization': 'Bearer OCTADESK.eyJuYmYiOjE2NTY0MzgxMDAsImV4cCI6MTk3Nzg0NjEwMCwiaXNzIjoiaHR0cDovL2lkZW50aXR5LXNlcnZlci5vY3RhZGVzay5zZXJ2aWNlcyIsImF1ZCI6WyJodHRwOi8vaWRlbnRpdHktc2VydmVyLm9jdGFkZXNrLnNlcnZpY2VzL3Jlc291cmNlcyIsImdlbmVyYWwiXSwiY2xpZW50X2lkIjoiZHdNVGVDNTlYS3ZYIiwic3ViIjoiMmEzMDZmMWQtODVhZC00N2JkLWJhYzItNzdlOWJjNWU2ZDMyIiwiYXV0aF90aW1lIjoxNjU2NDM4MTAwLCJpZHAiOiJsb2NhbCIsInN1YmRvbWFpbiI6InNlZ21lZGljIiwicm9sZSI6Im93bmVyIiwidHlwZSI6Im5vbmUiLCJzY29wZSI6WyJnZW5lcmFsIl0sImFtciI6WyJCZWFyZXIiXX0.lsMxACreYpMRwB78Y5HjRU0te4gipmeMy8gMsclSdYdMf5NGfLs1W7GUVU_fbPU3LpdxWrn2y7-no2RvTfTmufAiRFsowjryxnp530U4WaSmEmbLg8HzAMty3Q8YFCOd-SDYmLkCi4NFV8PBXf1EGPP-zVxriRUTUS72L-qaaPQD6DhPYpOs3bZQX13kEZrHQib9Vbh_2Hz5q9Z88dugc0UvoSAZOZQKKPBLd6Wfpcj8eFlx8oiC1Cb7wmjTPQ0T4Qu3Uuo_VF9l72dfHa1JgynniyeoNNDsnYDjp-AzAGd0yBFDQHFj6Yw_Ro8-Fs5z0YekRYdPW7CrUkWeSOM6pQ',
        "username": "antoniooliveira@segmedic.com.br"
    }

    payload = json.dumps({
  "email": f"{cpf}@gmail.com",
  "thumbUrl": None,
  "customerCode": None,
  "isLocked": True,
  "othersEmail": None,
  "type": 0,
  "permissionView": 1,
  "participantPermission": 0,
  "roleType": 0,
  "permissionType": 0,
  "othersCustomerCode": None,
  "idContactStatus": "string",
  "contactStatus": "string",
  "customField": {
"dt_inicial_text": f"{inicio}",
        "dt_final_text": f"{fim}",
        "cpf": cpf,
        "celular": celular
},
  "phoneContacts": [
    {
      "number": str(celular),
      "countryCode": "55",
      "type": 1
    }
  ],
  "organization": {
    "default": True,
    "name": "string",
    "description": "string",
    "domains": [
      "string"
    ],
    "idGroup": "string",
    "idProducts": [
      "string"
    ],
    "customField": {}
  }
})

    response = requests.post(url, data=payload, headers=headers)
    print(response.status_code, response.json())

def SendText(number, message):
    # SECURITY
    jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEsImlhdCI6MTY1NjU5OTcwNCwiZXhwIjoxNjU2NjM1NzA0fQ.dJ3pNp1XCdn5VtCITh2dgwhTqEYCdG7PM4LlNPrPBko'
    rota = 'send'
    # REQUEST
    url = f"http://18.229.96.2:5000/{rota}"
    headers = {'Content-Type': 'application/json', 'x-access-token': jwt}

    payload = json.dumps(
        {
            'number': number,
            'message': f"{message}"
        })

    response = requests.post(url, headers=headers, data=payload)
    print(f" STATUS TENTATIVA || {response.status_code} || {response.text}")


inicio = '16/08/2022'
fim = '16/08/2022'

dt_inicio = '2022-08-16'
dt_fim = '2022-08-16'

loop = [5]

for i in loop:
    url = f"https://api.feegow.com/v1/api/reports/generate?DATA_INICIO={inicio}&DATA_FIM={fim}&EXECUCAO_ITEM[]=S&ESPECIALIDADE_IDS[]={i}&report=schedule-appointments"
    header = {'Content-Type': 'application/json',
              'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmZWVnb3ciLCJhdWQiOiJwdWJsaWNhcGkiLCJpYXQiOiIwOS0wMS0yMDIwIiwibGljZW5zZUlEIjoiODI4OSJ9.sJU57cGbJq-wMPQbm5gCH1HtrnV7xMsh6RVfH5m1DtE'
              }

    r = requests.post(url,data=header)
    l = r.json()
    if not l['data']:
      continue

    for item in l["data"]:
        Cadastro(inicio=dt_inicio,fim=dt_fim,cpf=item["CPF"],celular=item["Cel1"])
#         # print('ID PACIENTE: '+ str(item["PacienteID"]) + ' CELULAR: ' + str(item["Cel1"]) +' CPF: ' + str(item["CPF"]))
# celular1 = "21985010838"
# #Cadastro(inicio=dt_inicio,fim=dt_fim,cpf=15625865728,celular=celular1)
# SendText(celular1, 'hope')