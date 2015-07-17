# A basic program for the Raspberry Pi Robot
#
# Put together by Brian Corteil for the Raspberry Pi
# This is free software, enjoy!!!! if you improve it, please share it
# 
# The robot uses the Pibrella library for Pimoroni, because it uses the Pibrella broad for control and sensing 


# import the pibrella library

import pibrella

# import time functions

from time import sleep

# functions

# move forward for 'n' seconds

def forward(seconds):
    
    pibrella.output.e.on()
    pibrella.output.f.on()
    sleep(seconds)
    pibrella.output.e.off()
    pibrella.output.f.off()
            
def left(seconds):
    
    pibrella.output.e.on()
    sleep(seconds)
    pibrella.output.e.off()
    
def right(seconds):
    
    pibrella.output.f.on()
    sleep(seconds)
    pibrella.output.f.off()

def button_pressed():

	for i in range(0,4):
		forward(0.5)
		left(0.9)



    
# main program

while True:
	if pibrella.button.read():
		button_pressed()
