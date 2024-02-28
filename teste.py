from funcionalidades import *

tv = Televisor('SONY', 'SONY-123')
controle = ControleRemoto(tv)
controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')

print(tv.canal_atual)