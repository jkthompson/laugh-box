#!/usr/bin/env python

import os
from subprocess import Popen
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)


def button_is_up():
  return (GPIO.input(23) == True)

def button_is_down():
  return (GPIO.input(23) == False)


def wait_for_press():
  while (button_is_up()):
    sleep(0.1)
  while (button_is_down()):
    sleep(0.1)
  return True 

def start_laughing():
  #os.system('mpg123 --loop -1 -q laugh.mp3 &')
  p = Popen(['mpg123','--loop','-1','-q','laugh.mp3','&'])
  print(p.pid)
  return p  

def stop_laughing(p):
  p.terminate()
  return

while True:
  wait_for_press()
  #os.system('mpg123 -q laugh.mp3 &')
  p = start_laughing()
  wait_for_press()
  stop_laughing(p)
  
