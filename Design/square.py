import pigpio

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)


def square(squareIs, sineIs):
    squareIs = True
    sineIs = False

def sine(sineIs, squareIs):
    squareIs = False
    sineIs = True

def square_function_on(frequency,amplitude,squareIs, sineIs):
    if squareIs == True:
        pwm = GPIO.PWM(21, frequency) # 1 kHz frequency
        pwm.start(50)
    elif sineIs == True:
        #do things
        sineIs = True

def function_off(pwm):
    pwm.stop()
