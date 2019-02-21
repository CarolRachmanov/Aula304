class Bolo:
    tamanho = 'grande'
    #Isso diz que qualquer bolo que eu vá criar terá um tamanho grande, Assim posso tirá-la da função construtora e do parâmetro. 
    #O padrão do python para receber uma instância é referênciá-la através da palavra self. Ésó trocar todo o que tem "instância" por self.
    #Um objeto pode fazer coisas ou pode ter coisas sendo feitas com ele, pode ser manipulado. 

    def __init__ (instancia, sabor, cobertura): #tamanho:
        instancia.sabor = sabor
        instancia.cobertura = cobertura
        # instancia.tamanho  = tamanho 

    def assar(self):
     print('O bolo está assando.')
     return True

    def comer(self):
        pass 

    def esta_estragado(self):
        pass 
#Esses defs DEVEM estar identados dentro da classe!
#Caso a pessoa não saiba qual parâmetro ela vai ter, posso usar os kwargs: (Mas esse método é mais complicado e eu vou ter que declarar todos os argumentos da mesma forma )
# def _init_(instancia, **kwargs)
    #sabor = kwargs.get('sabor')
    # tamanho = kwargs.get('tamanho')  ----> Aqui ele vai ver se a pessoa vai passar um tamanho
    #   if sabor is not None: 
            #instancia.sabor = sabor
        
# Se o tamanho ainda estivesse ali dentro, eu podia passar aqui em seguida mais um argumento, o do tamanho. Assim o programa vai me responder sempre o mesmo tamanho. 
    # Atributos que eu quero que mudem eu coloco sempre dentro do construtor. 


#Sempre chamo a instância numa variável, por esse motivo bolo1 e bolo2 foram criadas.

bolo1 = Bolo('Chocolate', 'Morango') #, 'médio') 
bolo2 = Bolo('Baunilha', 'Chocolate') #,'pequeno')

if bolo1.assar():
     print ('Você colocou o bolo pra assar')
else: 
     print('Você se esqueceu de colocar o seu bolo para assar.')

print(bolo1.sabor)
print(bolo1.tamanho)

print(bolo2.sabor)
print(bolo2.tamanho)

if bolo1.sabor == bolo2.sabor:
    print('Você tem dois bolos com o mesmo sabor.')
else:
    print('Seus bolos têm sabores diferentes.')

