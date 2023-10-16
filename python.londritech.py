import pyautogui #biblioteca para identificação de eventos no computador, baixe com pip install pyautogui
import keyboard #biblioteca para identificar eventos no teclado, baixe com pip install keyboard
altura = 600 #do jogo
largura = 500 #do jogo
captura =(360, 320, altura, largura) #para saber onde começa
ecra = pyautogui.screenshot(region=captura) #tira um print desta area da tela

def identifica_vermelho(imagem):#não vai analisar o lado direito enquanto tenham pixels vermelhos do lado esquerdo
altura_imagem , largura_imagem = imagem.size
for x in range(0, altura_imagem):
for y in range(0, largura_imagem): #percorre todo o x e depois vai para o proximo y e percorre todo o x
if imagem.getpixel((x, y)) == (255, 0, 0): #(255,0,0)-identifica a cor vermelha [R,G,B]
return x, y

while not keyboard.is_pressed('m'): #fica esecuntando enquanto o m não é pressionado
pixel_vermelho = identifica_vermelho(ecra) #identifica se á pixels vermelhos na area da tela definida - puxa a função (def identifica_vermelho)
if pixel_vermelho:
pyautogui.moveTo(pixel_vermelho[0]+captura[0], pixel_vermelho[1]+captura[1])#tem que somar com a captura para o mouse não ir para uma cordenada da tela inteira do computador
pyautogui.mouseDown() #função de segurar o mouse
pyautogui.sleep(0.016) #faz o algoritimo "dormir" para recomeçar
ecra = pyautogui.screenshot(region=captura) #tira outra captura para recomeçar
#pyautogui.moveTo(largura,altura, duration=0.1)