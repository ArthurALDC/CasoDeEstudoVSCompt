import pyxel as px
import random

# cria a tela
px.init(256, 256, "Gatinhos", 24, px.KEY_ESCAPE)
# tamanho da borda
tamCerca = 16


def Iniciar():
    px.tempoJogo = 60
    # propriedades player 1
    px.p1y = 128
    px.p1x = 64
    px.p1u = 0
    px.p1v = 0
    px.p1h = 29
    px.pontosP1 = 0

    # propriedades player 2
    px.p2x = 192
    px.p2y = 128
    px.p2u = 0
    px.p2v = 98
    px.p2h = 29
    px.pontosP2 = 0

    # caracteristicas peixes
    px.numPeixes = 8
    px.peixesX = []
    px.peixesY = []
    px.velPeixes = []
    for i in range(px.numPeixes):
        px.peixesX.append(random.randrange(20, 226))
        px.peixesY.append(10)
        px.velPeixes.append(random.randrange(2, 8))


Iniciar()
# sprites/sons
px.image(0).load(0, 0, 'Sprites.png')
px.image(1).load(0, 0, 'MapaGatinhos.png')


estadoGatoFinal = 0


def animaçãoGatoP1(v, h):
    px.p1h = h
    px.p1v = v
    px.p1u = px.p1u + 28
    if px.p1u >= 84:
        px.p1u = 0


def animaçãoGatoP2(v, h):
    px.p2h = h
    px.p2v = v
    px.p2u = px.p2u + 28
    if px.p2u >= 84:
        px.p2u = 0


def movimentaçãoP1():
    if px.btn(px.KEY_W) and (px.p1y) > tamCerca+10:
        px.p1y = px.p1y - 3
        animaçãoGatoP1(75, 24)
    if px.btn(px.KEY_S) and (px.p1y) < 240-tamCerca:
        px.p1y = px.p1y + 3
        animaçãoGatoP1(0, 29)
    if px.btn(px.KEY_A) and (px.p1x) > tamCerca+14:
        px.p1x = px.p1x - 3
        animaçãoGatoP1(29, 23)
    if px.btn(px.KEY_D) and (px.p1x) < 240 - tamCerca:
        px.p1x = px.p1x + 3
        animaçãoGatoP1(52, 23)


def movimentaçãoP2():
    if px.btn(px.KEY_UP) and (px.p2y) > tamCerca+10:
        px.p2y = px.p2y - 3
        animaçãoGatoP2(173, 24)
    if px.btn(px.KEY_DOWN) and (px.p2y) < 240-tamCerca:
        px.p2y = px.p2y + 3
        animaçãoGatoP2(98, 29)
    if px.btn(px.KEY_LEFT) and (px.p2x) > tamCerca+14:
        px.p2x = px.p2x - 3
        animaçãoGatoP2(127, 23)
    if px.btn(px.KEY_RIGHT) and (px.p2x) < 240 - tamCerca:
        px.p2x = px.p2x + 3
        animaçãoGatoP2(150, 23)


def colidiu(x, y, Ix, Iy):
    if y < Iy+10 and y > Iy-10 and x > Ix-10 and x < Ix+10:
        return True


def update():
    # att timer

    if px.frame_count % 24 == 0 and px.tempoJogo > 0:
        px.tempoJogo = px.tempoJogo - 1

    movimentaçãoP1()
    movimentaçãoP2()
   # if pyxel.btnp(pyxel.KEY_SPACE):
    #   dispara()

    # movimentação e colisão do inimigo
    for i in range(px.numPeixes):
        px.peixesY[i] = px.peixesY[i] + px.velPeixes[i]
        if colidiu(px.p1x, px.p1y, px.peixesX[i], px.peixesY[i]) and px.tempoJogo != 0:
            px.peixesY[i] = 0
            px.peixesX[i] = random.randrange(20, 236)
            px.pontosP1 = px.pontosP1 + 1

        if colidiu(px.p2x, px.p2y,  px.peixesX[i], px.peixesY[i]) and px.tempoJogo != 0:
            px.peixesY[i] = 0
            px.peixesX[i] = random.randrange(20, 236)
            px.pontosP2 = px.pontosP2 + 1

        if px.peixesY[i] >= 259:
            px.peixesY[i] = 0
            px.peixesX[i] = random.randrange(20, 236)
        # reinicia o jogo
        if px.tempoJogo == 0 and px.btn(px.KEY_R):
            Iniciar()


def draw():
    global estadoGatoFinal
    # mapa
    px.blt(0, 0, 1, 0, 0, 264, 264, 2)

    # peixes
    for i in range(px.numPeixes):
        px.blt(px.peixesX[i]-12, px.peixesY[i]-5, 0, 0, 198, 28, 11, 2)
    #blt (X,T,IMG(0-2),u,v,w,h,color)
    # gatos
    px.blt(px.p1x-13, px.p1y-12, 0,  px.p1u, px.p1v, 28, px.p1h, 2)
    px.blt(px.p2x-13, px.p2y, 0, px.p2u, px.p2v, 28, px.p2h, 2)

    # placar e tempo
    px.blt(6, 0, 0, 0, 209, 50, 40, 2)
    px.blt(209, 0, 0, 0, 209, 50, 40, 2)
    px.blt(104, 0, 0, 0, 209, 50, 40, 2)
    px.text(25, 4, str(px.pontosP1), 8)
    px.text(230, 4, str(px.pontosP2), 8)
    px.text(123, 4, str(px.tempoJogo), 8)

    if px.tempoJogo == 0 and px.pontosP1 > px.pontosP2:
        px.text(100, 180, "PLAYER 1 VENCEU", 8)
        px.blt(94, 89, 0, 104+(76*estadoGatoFinal), 0, 76, 85, 2)
        px.text(82, 200, "PRESSIONE R PARA REINICIAR", 8)
        if px.frame_count % 24 == 0 and estadoGatoFinal == 0:
            estadoGatoFinal = 1
        elif px.frame_count % 24 == 0 and estadoGatoFinal == 1:
            estadoGatoFinal = 0

    if px.tempoJogo == 0 and px.pontosP1 < px.pontosP2:
        px.text(100, 180, "PLAYER 2 VENCEU", 8)
        px.blt(94, 89, 0, 104+(76*estadoGatoFinal), 85, 76, 85, 2)
        px.text(82, 200, "PRESSIONE R PARA REINICIAR", 8)
        if px.frame_count % 24 == 0 and estadoGatoFinal == 0:
            estadoGatoFinal = 1
        elif px.frame_count % 24 == 0 and estadoGatoFinal == 1:
            estadoGatoFinal = 0

    if px.tempoJogo == 0 and px.pontosP1 == px.pontosP2:
        px.text(120, 120, "EMPATE", 8)
        px.text(82, 200, "PRESSIONE R PARA REINICIAR", 8)


px.run(update, draw)
