string='54.509.762/0001-47'

def testecnpj(cnpj):
    testes=[False, False, False, False]
    testes[0]=True

    try:
        #quebra CNPJ em partes menores
        a=cnpj.split('.')
        #testa a primeira parte
        if len(a[0]) == 2:
            try:
                int(a[0])
                #verifica se não há nenhuma letra ao invés de número. 
                testes[0]=True
            except:
                print('Primeiros dois digitos não são números.')
        else:
            #Caso a primeira parte não tenha tamanho dois, formato será inválido
            print('Formato inválido')
            
        #repete o processo agora para a segunda parte do CNPJ
        if len(a[1]) == 3:
            try:
                int(a[1])
                testes[1]=True
            except:
                print('digitos não são números.')
        else:
            print('Formato inválido')
        #Além de testar, ele pega uma parte da parte após o /
        if len(a[2].split('/')[1].split('-')[0]) == 4:
            try:
                int(a[2].split('/')[1].split('-')[0])
                testes[2]=True
            except:
                print('digitos não são números.')

        #Repete o método acima, mas agora verificando a parte após o -
        if len(a[2].split('/')[1].split('-')[1]) == 2:
            try:
                int(a[2].split('/')[1].split('-')[1])
                testes[3]=True
            except:
                print('digitos não são números.')
        else:
            print('Formato inválido')
            

    

    except:
        print('formato Inválido')

    if False in testes:
        return False
    else:
        return True




