# COMO SABER AS COORDENADAS DO MEU MOUSE :
#
#import pyautogui 
#print(pyautogui.position())


import pyautogui
import pyautogui as p
import time


print("[ + ] Iniciando script ...")
time.sleep(10)

# Movendo Dado para Área de click
# Primeira vez que a aplicação irá mover o mouse para a coordenada do botão de passar a página
pyautogui.moveTo(1334, 414, duration = 1)
time.sleep(0.5)


# Setar a Página que começa o livro ou a que você deseja
name = "start Page"
# Página em que irá terminar o livro
while name < "Finish Page":
	# Tirando print do Desktop
	ss = p.screenshot()
	# Salvando print
	ss.save("Pagina"+str(name)+".png")

	name += 1
	print("[ + ] Print salvo ~"+"Página-"+name)
	time.sleep(4)
	
	print("[ + ] Movendo mouse ...")
	# Movendo mouse para reaparecer opção de click
	# Inserir as coordenadas do local onde a aplicação irá clicar para passar de página
	# A primeira movimentação serve para reaparecer o botão de click caso o site esconda ele ...
	# A segunda serve para retornar para cima do botão para haver o click
	pyautogui.moveTo(1333, 414, duration = 1)
	pyautogui.moveTo(1334, 414, duration = 1)
	# Clicando no alvo
	pyautogui.click(1334, 414)
	time.sleep(1)