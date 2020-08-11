import RPi.GPIO as GPIO
import os

gpio_pin_number=21
#Replace YOUR_CHOSEN_GPIO_NUMBER_HERE with the GPIO pin number you wish to use
#Make sure you know which rapsberry pi revision you are using first
#The line should look something like this e.g. "gpio_pin_number=7"

GPIO.setmode(GPIO.BCM)

GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
    os.system("sudo shutdown -h now")

except:
    pass

GPIO.cleanup()