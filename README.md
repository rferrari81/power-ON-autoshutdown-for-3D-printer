POWER ON & AUTOSHUTDOWN 3D PRINTER

This is power ON & autoshutdown dispositive.
the scheme is very easy, there is tro pin for connect two relays. First relay control power on and off the printer and the second relay shutdown respberry when is connected.

There is one RGB led, this indicate the status of printer.

LED BLUE: printer in standby, push button for power on.

LED GREEN: priner power on mode, push button for power off printer.

LED RED BLINK: start 10 sec. timer for power off, in this time if you push power button the 
                             led turn on GREEN and autoshutdown is reset.
                             
LED RED: autoshutdown process is started and the printer shutdown after 10 sec.

To control the device, there is two inputs one for GND and other for digital PIN from printer motherboards.

To control digital PIN in start gcode put this string before all command 

M42 M1 P(pin motherboard) S255 ;activate pin for autoshutdown

and in end gcode put this string after all command

M109 R50; Wait for the hotend to cool down to 50C

M42 M1 P(pin motherboard) S0 ;deactivate pin for autoshutdown

Write the firmware on arduino

RASPBERRY CONFIG FILE
