import pigpio
import rgb1602
import time

def input_frequency(frequency):
    previousValue
    prev_time = time.time()
    while(GPIO.input(encoder.sw) != 0):
        current_time = time.time()
        if previousValue != GPIO.input(encoder.clk):            #this is to poll the rotary encoder to check if anything is changed so it is not always running through the code.
            if GPIO.input(encoder.clk) == 0:                    #if encoder.clk is open prior to dt than you know the knob is being spun anti clockwise and can update values accordingly
                if GPIO.input(encoder.dt) == 0:
                    direction = "anti-clockwise"
                    speed = current_time - prev_time
                    if speed < .2:                      #speed is to test how fast the knob is spinning this is just recorded from current time to last time the knob was spun
                        if (frequency - 1000) > 1000:    
                            frequency -= 1000
                        else:
                            frequency = 1000
                    elif (frequency - 100) > 1000:
                        frequency -= 100
                    else:
                        frequency = 1000
                    #print(f"Direction: {direction}, frequency: {frequency}, Speed: {speed}")      #this shows what direction the user spun the knob the new frequency value and how fast the spin was this if for debugging
                    lcd.clear()
                    lcd.setCursor(0, 0)                     #cursor requires a row and column number for the display this just says start from top right
                    lcd.printout(f"Select with knob")       #print to display
                    lcd.setCursor(0, 1)                     #cursor points to second row
                    lcd.printout(f"{frequency} Hz")      #print to display
                    time.sleep(.1)                          #This is for a debounce so the rotary encoder is not double reading or reading backwards. 
                    prev_time = current_time                #update time
                else:                                       #this is to show dt was before clk meaning this part of the function is for clock wise everything below is the same as above but calculated for going clockwise instead of anti clockwise
                    direction = "clockwise"
                    speed = current_time - prev_time
                    if speed < .2:
                        if (frequency + 1000) < 10000:
                            frequency += 1000
                        else:
                            frequency = 10000
                    elif (frequency + 100) < 10000:
                        frequency += 100
                    else:
                        frequency = 10000
                    #print(f"Direction: {direction}, frequency: {frequency}, Speed: {speed}")
                    lcd.clear()
                    lcd.setCursor(0, 0)         
                    lcd.printout(f"Select with knob")
                    lcd.setCursor(0, 1)
                    lcd.printout(f"{frequency} Hz")
                    time.sleep(.1)
                    prev_time = current_time                
            previousValue = GPIO.input(encoder.clk)                 #update previous value for polling so you can retest if something has changed


def input_frequency(amplitude):
    previousValue
    prev_time = time.time()
    while(GPIO.input(encoder.sw) != 0):
        current_time = time.time()
        if previousValue != GPIO.input(encoder.clk):            #this is to poll the rotary encoder to check if anything is changed so it is not always running through the code.
            if GPIO.input(encoder.clk) == 0:                    #if encoder.clk is open prior to dt than you know the knob is being spun anti clockwise and can update values accordingly
                if GPIO.input(encoder.dt) == 0:
                    direction = "anti-clockwise"
                    speed = current_time - prev_time
                    if speed < .2:                      #speed is to test how fast the knob is spinning this is just recorded from current time to last time the knob was spun
                        if (amplitude - 1) > 0:    
                            amplitude -= 1
                        else:
                            amplitude = 0
                    elif (amplitude - .25) > 0:
                        amplitude -= .25
                    else:
                        amplitude = 0
                    #print(f"Direction: {direction}, frequency: {frequency}, Speed: {speed}")      #this shows what direction the user spun the knob the new frequency value and how fast the spin was this if for debugging
                    lcd.clear()
                    lcd.setCursor(0, 0)                     #cursor requires a row and column number for the display this just says start from top right
                    lcd.printout(f"Select with knob")       #print to display
                    lcd.setCursor(0, 1)                     #cursor points to second row
                    lcd.printout(f"{amplitude} v")      #print to display
                    time.sleep(.1)                          #This is for a debounce so the rotary encoder is not double reading or reading backwards. 
                    prev_time = current_time                #update time
                else:                                       #this is to show dt was before clk meaning this part of the function is for clock wise everything below is the same as above but calculated for going clockwise instead of anti clockwise
                    direction = "clockwise"
                    speed = current_time - prev_time
                    if speed < .2:
                        if (amplitude + 1) < 5:
                            amplitude += 1
                        else:
                            amplitude = 5
                    elif (amplitude + .25) < 5:
                        amplitude += .25
                    else:
                        amplitude = 5
                    #print(f"Direction: {direction}, frequency: {frequency}, Speed: {speed}")
                    lcd.clear()
                    lcd.setCursor(0, 0)         
                    lcd.printout(f"Select with knob")
                    lcd.setCursor(0, 1)
                    lcd.printout(f"{amplitude} v")
                    time.sleep(.1)
                    prev_time = current_time                
            previousValue = GPIO.input(encoder.clk)                 #update previous value for polling so you can retest if something has changed
