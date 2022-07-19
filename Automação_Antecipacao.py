import requests
import pprint as pp
import espec


# Definindo as variáveis a serem usadas no código
inicio = "21/06/2022"
fim = "28/06/2022"
D1 = "15/06/2022"
D2 = "16/06/2022"
D3 = "17/06/2022"

LISTA_ENVIADOS = []

url_escallo = f"https://segmedic.escallo.com.br/escallo/api/v1/campanha/texto/16/lista"
# Print de confirmação da data de inicio e fim
print(inicio)
print(fim)



# Definindo meu vetor especialidades, onde cada número que está contido nele, representa a ID de uma ESPECIALIDADE
# 3,4,5,6,7,10,11,13,14,15,16,18,21,22,23,24,25,26,27,28,29,31,33,34,37,38,41,46,59,68,71,74
especialidades = [3,4,6,7,10,11,13,14,15,18,21,22,23,25,26,27,28,29,31,34,37,38,41,46,59,68,71,74]

# Criando a lógica para o disparo de campanhas de ANTECIPAÇÃO, que consiste em:
# Através do relatório de AGENDAMENTOS, buscar as informações de pacientes que estão agendados em datas futuras 
# Através do relatório de OCUPAÇÃO, fazer a verificação se há vagas disponíveis para a mesma ESPECIALIDADE que o paciente está agendado futuramente, para os próximos dias (D+1,D+2,D+3)
# Se houver vagas disponíveis, utilizar a API da ESCALLO para disparar uma mensagem a esse paciente perguntando se ele possui o interesse de ANTECIPAR esse agendamento, para uma data mais próxima.

# Lendo as informações da API da FEEGOW, na parte de AGENDAMENTOS:
for i in especialidades:
    url_feegow_agendamentos = f"https://api.feegow.com/v1/api/reports/generate?DATA_INICIO={inicio}&DATA_FIM={fim}&EXECUCAO_ITEM[]=S&ESPECIALIDADE_IDS[]={i}&report=schedule-appointments"
    header = {'Content-Type': 'application/json',
              'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmZWVnb3ciLCJhdWQiOiJwdWJsaWNhcGkiLCJpYXQiOiIwOS0wMS0yMDIwIiwibGljZW5zZUlEIjoiODI4OSJ9.sJU57cGbJq-wMPQbm5gCH1HtrnV7xMsh6RVfH5m1DtE'
              }

    r = requests.post(url_feegow_agendamentos, data=header)
    l = r.json()
    if not l['data']:
        continue

    pp.pprint(l)
    pp.pprint(i)

# Lendo as informações da API da FEEGOW, na parte de OCUPAÇÃO: 
    url_feegow_ocupacao = f"https://api.feegow.com/v1/api/reports/generate?report=occupation&DATA_INICIO={D1}&DATA_FIM={D3}&ESPECIALIDADE_IDS[]={i}"
    header = {'Content-Type': 'application/json',
    'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmZWVnb3ciLCJhdWQiOiJwdWJsaWNhcGkiLCJpYXQiOiIwOS0wMS0yMDIwIiwibGljZW5zZUlEIjoiODI4OSJ9.sJU57cGbJq-wMPQbm5gCH1HtrnV7xMsh6RVfH5m1DtE'
    }

    a = requests.post(url_feegow_ocupacao,data=header)
    b = a.json()
    if not b['data']:
        continue

    #pp.pprint(b)
    #pp.pprint(i)

# Chamando minha função modalidade, que é a função que relaciona EspecialidadeID com NomeEspecialidade  
    especi = espec.modalidade(i)                                             
# Coletando as informações lidas pelo json na url de AGENDAMENTOS e OCUPAÇÃO, e se, cumprindo todos os requisitos, realizar o disparo de MENSAGENS usando a API da ESCALLO
    for item in l["data"]:  
        for it in b["data"]:
            
        # Enviando mensagens ofertando vagas, cujo a mais próxima é D+1 (Amanhã)
            
            if(item['PacienteID'] in LISTA_ENVIADOS):
                
                continue 

            else:

                if(it['Data'] == D1) and (it['HLivres'] > 5):
                    notificacao = f"Olá! Estamos com alguns novos horários disponíveis para {especi} e como vimos que você possui um agendamento conosco, pensamos em você. Temos disponibilidade para {D1}. Qual o melhor horário para você?"
                    request_escallo = espec.request_e(notificacao, item['Cel1'], item['NomePaciente'])
                    LISTA_ENVIADOS.append(item['PacienteID'])

        # Enviando mensagens ofertando vagas, cujo a mais próxima é D+2 (Depois de amanhã)
                elif(it['Data'] == D2) and (it['HLivres'] > 5):
                    notificacao = f"Olá! Estamos com alguns novos horários disponíveis para {especi} e como vimos que você possui um agendamento conosco, pensamos em você. Temos disponibilidade para {D2}. Qual o melhor horário para você?"
                    request_escallo = espec.request_e(notificacao, item['Cel1'], item['NomePaciente'])
                    LISTA_ENVIADOS.append(item['PacienteID'])

        # Enviando mensagens ofertando vagas, cujo a mais próxima é D+3 (Daqui 3 dias)              
                elif(it['Data'] == D3) and (it['HLivres'] > 5):
                    notificacao = f"Olá! Estamos com alguns novos horários disponíveis para {especi} e como vimos que você possui um agendamento conosco, pensamos em você. Temos disponibilidade para {D3}. Qual o melhor horário para você?"
                    request_escallo = espec.request_e(notificacao, item['Cel1'], item['NomePaciente'])
                    LISTA_ENVIADOS.append(item['PacienteID'])
