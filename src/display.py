#!/usr/bin/env python3

import pygame
from pygame.locals import *
from admin import copy_data, paste_data, pc

pygame.init()


screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Clipy')

font = pygame.font.SysFont('Ariel', 30)

#define colours
bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# #define global variable
clicked = False

copy_list = []
short = []

class button():
	#colours for button and text
	button_col = (255, 0, 0)
	hover_col = (255, 80, 50)
	click_col = (192, 192, 192)
	text_col = black
	width = 180
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		pos = pygame.mouse.get_pos()

		button_rect = Rect(self.x, self.y, self.width, self.height)

		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)

		pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action

class button1():
	#colours for button and text
	button_col = (255, 0, 0)
	hover_col = (255, 80, 50)
	click_col = (192, 192, 192)
	text_col = black
	width = 110
	height = 50

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button1(self):

		global clicked
		action = False

		pos = pygame.mouse.get_pos()

		button_rect = Rect(self.x, self.y, self.width, self.height)

		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)

		pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action


screen.fill(bg)
copy = button(75, 100, 'Copy')
paste = button(325, 100, 'Paste')
refresh = button1(440, 325, 'load data')

def write():
	try:
		# print(a)
		note = font.render('Latest : ', True, black)
		textRect2 = note.get_rect()
		textRect2.center = (160, 200)
		screen.blit(note, textRect2)

		x = len(copy_list) -1
		# while(i >= 0):
		for i in range(len(copy_list)):
			content = font.render(copy_list[x-i], True, black)
			textRect1 = content.get_rect()
			textRect1.center = (310, 250 + (30*i))
			screen.blit(content, textRect1)
			# i = i - 1
	except TypeError:
		err = font.render('Database is empty... Paste something', True, black)
		textRect = err.get_rect()
		textRect.center = (310, 260)
		screen.blit(err, textRect)

# write()
run = True
while run:

	screen.fill(bg)

	if copy.draw_button():
	    pc.copy(copy_list[-1])

	if paste.draw_button():
		paste_data()

	if refresh.draw_button1():
		copy_list = copy_data()

	write()


	event = pygame.event.wait()

	if event.type == pygame.QUIT:
		run = False
			# pygame.quit()

	pygame.display.update()


pygame.quit()
