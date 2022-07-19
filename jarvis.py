import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

maquina = pyttsx3.init()

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:

        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:

        # Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')

        # Retorna a frase pronunciada
        print("Você disse: " + frase)

        if 'Jarvis' in frase:
            frase = frase.replace('Jarvis', '')
            print(frase)
            maquina.runAndWait()

    # Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")

    return frase

def comando_voz_usuario():
    comando = ouvir_microfone()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%HH:%MM')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say(f'Tocando: {musica} em Youtube de Brayan Robert')
        maquina.runAndWait()


comando_voz_usuario()
