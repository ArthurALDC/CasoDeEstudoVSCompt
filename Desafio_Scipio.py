import cv2
import numpy as np

#Carregar a imagem
img = cv2.imread("meteor_challenge_01.png")

#Converter a imagem para o espaço de cores HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Ajustar os intervalos da cor branca em HSV
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 25, 255])

#Ajustar os intervalos da cor vermelha em HSV
lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 70, 50])
upper_red2 = np.array([180, 255, 255])

#Criar máscaras para as cores branca e vermelha
mask_white = cv2.inRange(hsv, lower_white, upper_white)
mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask_red = cv2.bitwise_or(mask_red1, mask_red2)

#Detectar os contornos dos pontos brancos e vermelhos
contours_white, _ = cv2.findContours(mask_white, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Contar a quantidade de pontos de cada cor
num_white_points = len(contours_white)
num_red_points = len(contours_red)

print(f'Número de pontos brancos: {num_white_points}')
print(f'Número de pontos vermelhos: {num_red_points}')

#Converter a imagem de máscara para BGR
mask_white_bgr = cv2.cvtColor(mask_white, cv2.COLOR_GRAY2BGR)
mask_red_bgr = cv2.cvtColor(mask_red, cv2.COLOR_GRAY2BGR)

#Faz os pontos brancos ficarem brancos e os vermelhos em vermelho na saída
for contour in contours_white:
    cv2.drawContours(mask_white_bgr, [contour], 0, (255, 255, 255), -1)
for contour in contours_red:
    cv2.drawContours(mask_red_bgr, [contour], 0, (0, 0, 255), -1)

#Definir o intervalo de cor para a cor azul
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

#Criar uma máscara para selecionar apenas os pixels azuis na imagem
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

#Encontrar as coordenadas dos pixels azuis na imagem
y_coords, _ = np.where(mask_blue > 0)

#Calcular a média das coordenadas Y dos pixels azuis
nivel_agua = int(np.mean(y_coords))

print(f'Nível da água: {nivel_agua}')

#Conta os pontos vermelhos que estão perpendicularmente acima da linha da água
pontos_vermelhos_na_agua = 0
for contour in contours_red:
    x, y, w, h = cv2.boundingRect(contour)
    ponto_medio_x = x + w // 2
    ponto_medio_y = y + h // 2
    
    #Verificar se o ponto está acima do nível da água
    if ponto_medio_y < nivel_agua:
        #Calcular a diferença de altura entre o ponto e a linha da água
        diff_altura = nivel_agua - ponto_medio_y
        #Calcular a diferença de largura entre o ponto e a linha da água
        diff_largura = abs(ponto_medio_x - x)
        # enta ver a diferença de largura é menor que a diferença de altura, indicando que está perpendicular
        if diff_largura < diff_altura:
            pontos_vermelhos_na_agua += 1

print(f'Pontos vermelhos que vão cair na água: {pontos_vermelhos_na_agua}')

#Mostra as máscaras
cv2.imshow('Máscara Branca', mask_white_bgr)
cv2.imshow('Máscara Vermelha', mask_red_bgr)
cv2.imshow('Imagem Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
