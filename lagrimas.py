#!/usr/bin/env python
# -*- coding: utf-8 -*-

from universe import*


(LARGURA, ALTURA) = (300,600)
JANELA = pg.display.set_mode ((LARGURA,ALTURA))

try:

	IMG_PASSARO = pg.image.load('img/passaro.png')


except:

	IMG_PASSARO = pg.Surface ((50,50),pg.SRCALPHA)

## CONSTANTES



PAREDE_ESQUERDA = 0
PAREDE_DIREITA = LARGURA

PAREDE_BAIXO = ALTURA
PAREDE_CIMA = 0 

X_PASSARO = PAREDE_ESQUERDA + 10 
VY = 3 


from namedlist import namedlist

## OBJETO
IMG_PASSARO = pg.transform.scale(IMG_PASSARO, (50, 50))

Passaro = namedlist ("Passaro","y, vy")

PASSARO_INICIAL = Passaro (PAREDE_BAIXO//2, VY)

## DEFINICOES PADROES

Jogo = namedlist("Jogo", "passaro")

JOGO_INICIAL = Jogo (PASSARO_INICIAL)


def passaro_caindo (passaro): 
	if passaro.y > PAREDE_BAIXO: 
		print ("passaro sumiu")
	else:  
		passaro.y = passaro.y + VY 

		if passaro.y >= PAREDE_BAIXO: 
			passaro.y = PAREDE_BAIXO

		return passaro 


def mover_jogo (jogo): 
	passaro_caindo (jogo.passaro)
	return jogo 

def desenha_passaro (passaro):
	JANELA.blit(IMG_PASSARO, (X_PASSARO, passaro.y))

def desenha_jogo (jogo):
	desenha_passaro (jogo.passaro)

	return jogo 


def main (inic):
	big_bang (inic,tela=JANELA,
		quando_tick=mover_jogo,
		desenhar=desenha_jogo)


main(JOGO_INICIAL)
