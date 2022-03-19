
import Modulos as mod #importamos archivo y cambiamos nombre a mod
print(mod.mascotas) #print objeto mascotas de archivo importado
mod.saludo('Ernesto') # entra a la funcion saludo del archivo importado
                      # y tiene Ernesto de Parametro

from Modulos import saludo #Importando objeto saludo desde Modulos
saludo('Grandy')