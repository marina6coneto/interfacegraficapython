class Pessoa:
    'Isto é uma classe nova chamada Pessoa'
    
    idade = 15
    def saudacao(self):
        print('Olá Pessoas!')

Marina = Pessoa() 
# Output: 15
print
(Marina.idade)
# Output: <function Pessoa.saudacao>
print
(Marina.saudacao)
# Output: “Isto é uma classe nova chamada Pessoa”
print(Marina.__doc__)
Marina.saudacao()

# class Pessoa:
#     'Isto é uma classe nova chamada Pessoa'
#     idade = 15
#     def saudacao(self):
#         print('Olá Pessoas!')
# # create a new object of Person class
# matheus = Pessoa()
# # Output: 15
# print(matheus.idade)
# # Output: <bound method Person.greet of <__main__.Person object>>
# print(matheus.saudacao)
# # Chamando o método saudacao()
# # Output: “Olá Pessoas!”
# matheus.saudacao()