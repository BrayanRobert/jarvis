cel = [16,17,18,19,23,24,25,26,27,28,29,30,31,32,33,34]
vetor = ['C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
lista = [
    '/html/body/aside/section/section/aside/div/div[6]/div/form/div[1]/div[3]/div/ul/li[14]/a/label',
    '/html/body/aside/section/section/aside/div/div[6]/div/form/div[1]/div[3]/div/ul/li[25]/a/label',
    '/html/body/aside/section/section/aside/div/div[6]/div/form/div[1]/div[3]/div/ul/li[45]/a/label',
    '/html/body/aside/section/section/aside/div/div[6]/div/form/div[1]/div[3]/div/ul/li[48]/a/label'
]

for i in range(len(lista)):
    aux1 = lista[i]
    print(lista[i-1])
