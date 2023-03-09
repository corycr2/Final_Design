import sys
sys.path.append('../')
import rgb1602
import RPi.GPIO as GPIO
import time
import ohmmeter
import adc
import square
import input_frequency

#This creates the interface to talk to the digital potentiometer
pi1 = pigpio.pi()
h = pi1.spi_open(0,97600)

#Class to set up values dedicated to the encoder
class encoder:
    clk = 18
    dt = 23
    sw = 24

adc = 6
ohm = 5

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(encoder.clk, GPIO.IN, pull_up_down=GPIO.PUD_UP) #clk
GPIO.setup(encoder.dt, GPIO.IN, pull_up_down=GPIO.PUD_UP) #dt
GPIO.setup(encoder.sw, GPIO.IN, pull_up_down=GPIO.PUD_UP) #sw
GPIO.setup(adc, GPIO.IN, pull_up_down=GPIO.PUD_UP) #adc
GPIO.setup(ohm, GPIO.IN, pull_up_down=GPIO.PUD_UP) #adc

#LCD setup
lcd=rgb1602.RGB1602(16,2)


frequency = 1000
pwm = GPIO.PWM(21, frequency) # 1 kHz frequency



# Define the UI options
options = {
    "main": ["Off", "Mode Select", "LCD Color"],
    "mode_select": ["Function gen", "Ohm Meter", "Voltmeter", "DC Reference", "Frequency Measurement", "Back", "Main"],
    "function_gen": ["Type", "Frequency", "Amplitude", "Output", "Back", "Main"],
    "type": ["Sine", "Square", "Back", "Main"],
    "frequency": ["Input Frequency", "Back", "Main"],
    "amplitude": ["Input Amplitude", "Back", "Main"],
    "output": ["On", "Off", "Back", "Main"],
    "output_dc": ["On", "Off", "Back", "Main"],
    "ohm_meter": ["Display Reading", "Back", "Main"],
    "voltmeter": ["External", "Internal Reference", "Back", "Main"],
    "dc_reference": ["Voltage Value Input", "Output", "Back", "Main"],
    "frequency_measurement": ["External", "Internal", "Back", "Main"],
    "LCD color": ["Change color", "Back", "Main"]
}

# Initialize the current UI level to "main"
current_level = "main"
current_option = "Off"

# Infinite loop for the UI
while True:
    # Get the rotary encoder state
    clk_state = GPIO.input(encoder.clk)
    dt_state = GPIO.input(encoder.dt)
    sw_state = GPIO.input(encoder.sw)

    # Handle the rotary encoder rotation
    if clk_state != dt_state:
        lcd.clear()
        if clk_state == 0:
            # Rotate clockwise
            current_option_index = options[current_level].index(current_option)
            current_option_index = (current_option_index + 1) % len(options[current_level])
            current_option = options[current_level][current_option_index]
            time.sleep(.1)
        else:
            # Rotate counterclockwise
            current_option_index = options[current_level].index(current_option)
            current_option_index = (current_option_index - 1) % len(options[current_level])
            current_option = options[current_level][current_option_index]
            time.sleep(.1)

    # Handle the rotary encoder button press
    if sw_state == 0:
        time.sleep(1)
        lcd.clear()
        # Get the selected option
        selected_option = options[current_level][current_option_index]

        # Handle the "Off" option
        if selected_option == "Off":
            # Exit the program
            exit()

        # Handle the "Mode Select" option
        elif selected_option == "Mode Select":
            # Go to the "mode_select" level
            current_level = "mode_select"
            current_option = options[current_level][0]
        
        elif selected_option == "LCD Color":
            # Go to the "mode_select" level
            current_level = "LCD color"
            current_option = options[current_level][0]

            
        # Handle the other options
        elif current_level == "mode_select":
            if selected_option == "Function gen":
                current_level = "function_gen"
                current_option = options[current_level][0]
            elif selected_option == "Ohm Meter":
                current_level = "ohm_meter"
                current_option = options[current_level][0]
            elif selected_option == "Voltmeter":
                current_level = "voltmeter"
                current_option = options[current_level][0]
            elif selected_option == "DC Reference":
                current_level = "dc_reference"
                current_option = options[current_level][0]
            elif selected_option == "Frequency Measurement":
                current_level = "frequency_measurement"
                current_option = options[current_level][0]
            elif selected_option == "Back":
                # Go back one level
                current_level = "main"
                current_option = options[current_level][0]
            elif selected_option == "Main":
                # Go to the "main" level
                current_level = "main"
                current_option = options[current_level][0]

        elif current_level == "function_gen":
            if selected_option == "Type":
                current_level = "type"
                current_option = options[current_level][0]
            elif selected_option == "Frequency":
                current_level = "frequency"
                current_option = options[current_level][0]
            elif selected_option == "Amplitude":
                current_level = "amplitude"
                current_option = options[current_level][0]
            elif selected_option == "Output":
                current_level = "output"
                current_option = options[current_level][0]
            elif selected_option == "Back":
                current_level = "mode_select"
                current_option = options[current_level][0]
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]

        elif current_level == "type":
            if selected_option == "Sine":
                #Handle the "Sine" option
                #sine()
                #time.sleep(2)
                current_level = "type"
                current_option = options[current_level][0]
                pass
            elif selected_option == "Square":
                #Handle the "Square" option
                square.square(frequency)
                time.sleep(2)
                current_level = "type"
                current_option = options[current_level][1]
                pass
            elif selected_option == "Back":
                current_level = "function_gen"
                current_option = options[current_level][0]
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]

        # Handle the other levels and options similarly
        elif current_level == "frequency":
            if selected_option == "Input Frequency":
                #Handle the "Input Frequency" option
                input_frequency.input_frequency(frequency)
                time.sleep(2)
                current_level = "frequency"
                current_option = options[current_level][0]
                pass
            elif selected_option == "Back":
                current_level = "function_gen"
                current_option = options[current_level][0]
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]
        
        
        elif current_level == "amplitude":
            if selected_option == "Input Amplitude":
                # Handle the "Input amplitude" option
                #amplitude()
                #time.sleep(2)
                current_level = "amplitude"
                current_option = options[current_level][0]
                pass
            elif selected_option == "Back":
                current_level = "function_gen"
                current_option = options[current_level][0]
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]

        elif current_level == "output":
            if selected_option == "On":
                # Handle the "On" option
                square.function_on()
                time.sleep(2)
                current_level = "output"
                current_option = options[current_level][0]
                pass
            elif selected_option == "Off":
                #Handle the "Off" option
                square.function_off()
                time.sleep(2)
                current_level = "output"
                current_option = options[current_level][1]
                pass
            elif selected_option == "Back":
                #Auto "Off" option
                square.function_off()
                time.sleep(2)
                current_level = "function_gen"
                current_option = options[current_level][0]
            elif selected_option == "Main":
                #Auto "Off" option
                square.function_off()
                square.function_time.sleep(2)
                current_level = "main"
                current_option = options[current_level][0]
        #end of Function Generator

        elif current_level == "ohm_meter":
            if selected_option == "Display Reading":
                ohmmeter.ohm()
                time.sleep(2)
                current_level = "ohm_meter"
                current_option = options[current_level][0]
                pass
            elif selected_option == "Back":
                current_level = "mode_select"
                current_option = options[current_level][0]
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]
        #end of ohmmeter

        elif current_level == "voltmeter":
            if selected_option == "External":
                #Handle the "External" option
                adc.ADC()
                time.sleep(2)
                current_level = "voltmeter"
                current_option = options[current_level][0]
                pass
            elif selected_option == "Internal Refrence":
                current_level = "dc_reference"
                current_option = options[current_level][0]
            elif selected_option == "Back":
                current_level = "mode_select"
                current_option = options[current_level][0]
            elif selected_option == "Main":
                #exit()
                #time.sleep(2)
                current_level = "main"
                current_option = options[current_level][0]
            

        elif current_level == "dc_reference":
            if selected_option == "Voltage Value Input":
                #Handle the "Voltage Value Input" option
                #voltage_value_input()
                #time.sleep(2)
                current_level = "dc_reference"
                current_option = options[current_level][0]
                pass
            elif selected_option == "Output":
                current_level = "output_dc"
                current_option = options[current_level][0]
            elif selected_option == "Back":
                current_level = "mode_select"
                current_option = options[current_level][0]
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]

        elif current_level == "output_dc":
            if selected_option == "On":
                #Handle the "On_dc" option
                #on_dc()
                #time.sleep(2)
                current_level = "output_dc"
                current_option = options[current_level][0]
                pass
            elif selected_option == "Off":
                #Handle the "Off_dc" option
                #off_dc()
                #time.sleep(2)
                current_level = "output_dc"
                current_option = options[current_level][1]
                pass
            elif selected_option == "Back":
                #Auto off
                #off_dc()
                #time.sleep(2)
                current_level = "dc_reference"
                current_option = options[current_level][0]
            elif selected_option == "Main":
                #Auto off
                #off_dc()
                #time.sleep(2)
                current_level = "main"
                current_option = options[current_level][0]
        #end of DC Reference

        elif current_level == "frequency_measurement":
            if selected_option == "External":
                # Handle the "external" option
                #external()
                #time.sleep(2)
                current_level = "frequecny_measurement"
                current_option = options[current_level][0]
                pass
            elif selected_option == "Internal":
                current_level = "function_generator"
                current_option = options[current_level][0]
            elif selected_option == "Back":
                current_level = "mode_select"
                current_option = options[current_level][0]
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]
        
        elif current_level == "LCD color":
            if selected_option == "Change color":
                # Handle the "Change color" option
                #LCD_Color()
                current_level = "LCD color"
                current_option = options[current_level][0]
                pass
            elif selected_option == "Back":
                current_level = "mode_select"
                current_option = options[current_level][0]
            elif selected_option == "Main":
                current_level = "main"
                current_option = options[current_level][0]

    # Draw the current option on the display
    lcd.setCursor(0,0)
    lcd.printout(current_level)
    lcd.setCursor(0,1)
    lcd.printout(current_option)