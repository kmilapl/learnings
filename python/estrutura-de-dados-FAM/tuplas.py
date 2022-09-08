tupla = () #são representadas por parenteses
print("Tupla = ", tupla)
print("id    = ", id(tupla))
print()

tupla = (2, "um", 3, True) 
print("Tupla = ", tupla)
print("id    = ", id(tupla)) #endereço muda de acordo com os valores 
print()

t_1 = (1) #um único valor não é uma tupla
print(t_1)
print( type(t_1) )
print()

#Criar uma tupla com um único valor
#Avisa que é uma tupla colocando uma vírgula
t_1 = (1,)
print(t_1)
print( type(t_1) ) 
print()

t_2 = (1,2)
print(t_2)
print( type(t_2) ) 
print()
