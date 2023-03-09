def square(frequency):
    pwm = GPIO.PWM(21, frequency) # 1 kHz frequency

def function_on():
    pwm.start(50)

def function_off():
    pwm.stop()