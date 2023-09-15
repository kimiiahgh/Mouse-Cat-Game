#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:38:10 2017

@author: apple
"""
import pygame

pygame.init()


screen = pygame.display.set_mode((1000, 1000))

c = pygame.time.Clock()
image = pygame.image.load('mouse.jpg')
image = pygame.transform.scale(image, (150, 150))

mouse = pygame.image.load('cat.jpeg')
mouse = pygame.transform.scale(mouse, (150, 150))
rect_mouse = mouse.get_rect()
rect_mouse.x, rect_mouse.y = 700, 700

rect = image.get_rect()
rect.x = 400
rect.y = 400


running = True


while running:
    c.tick(30)
    screen.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    move_x, move_y = 0, 0
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        move_x -= 10
    if key[pygame.K_RIGHT]:
        move_x += 10
    if key[pygame.K_UP]:
        move_y -= 10
    if key[pygame.K_DOWN]:
        move_y += 10


    rect = rect.move((move_x, move_y))
    screen.blit(mouse, rect_mouse)
    screen.blit(image, rect)

    if rect.colliderect(rect_mouse):
        break

    pygame.display.update()
    

pygame.quit()
