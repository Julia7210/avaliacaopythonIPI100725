def mensagemOla ():
    input("Olá, seja bem-vindo. Por favor digite seu nome: ")

def senhaCriada ():
    senhaCriada = input ("Crie sua senha de acesso:")
    
def senhaDigitada ():
    senhaDigitada = input ("Digite a senha criada: ")
    
    
    if senhaCriada == senhaDigitada :
        print ("Cofre acessado com sucesso")
    else: 
        print ("Não é possivel acessar o cofre")
        
        
mensagemOla()
senhaCriada ()
senhaDigitada ()

