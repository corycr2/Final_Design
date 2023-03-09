#import all functions to be used
import sys
sys.path.append('../')
import rgb1602
import RPi.GPIO as GPIO
import time
import pigpio 

#This creates the interface to talk to the digital potentiometer
#pi1 = pigpio.pi()
#h = pi1.spi_open(1,97600)

value = 0
digi_input = 0

def digipot2_table():
    global value
    if value == 0:                      #0 ohms
        resistance = 103
        return resistance
    elif value == 1:
        resistance = 165
        return resistance
    elif value == 2:
        resistance = 240
        return resistance
    elif value == 3:
        resistance = 320
        return resistance
    elif value == 4:                    #500 ohms
        resistance = 397
        return resistance
    elif value == 5:
        resistance = 470
        return resistance
    elif value == 6:
        resistance = 545
        return resistance
    elif value == 7:
        resistance = 616
        return resistance
    elif value == 8:
        resistance = 693
        return resistance
    elif value == 9:
        resistance = 766
        return resistance
    elif value == 10:                   #1000 ohms
        resistance = 839
        return resistance
    elif value == 11:
        resistance = 911
        return resistance
    elif value == 12:
        resistance = 986
        return resistance
    elif value == 13:
        resistance = 1055
        return resistance
    elif value == 14:
        resistance = 1128
        return resistance
    elif value == 15:                   #1500 ohms
        resistance = 1200
        return resistance
    elif value == 16:
        resistance = 1271
        return resistance
    elif value == 17:
        resistance = 1348
        return resistance
    elif value == 18:
        resistance = 1432
        return resistance
    elif value == 19:
        resistance = 1493
        return resistance
    elif value == 20:                   #2000 ohms
        resistance = 1570
        return resistance
    elif value == 21:
        resistance = 1642
        return resistance
    elif value == 22:
        resistance = 1715
        return resistance
    elif value == 23:
        resistance = 1787
        return resistance
    elif value == 24:
        resistance = 1861
        return resistance
    elif value == 25:
        resistance = 1934
        return resistance
    elif value == 26:                   #2500 ohms
        resistance = 2007
        return resistance
    elif value == 27:
        resistance = 2080
        return resistance
    elif value == 28:
        resistance = 2155
        return resistance
    elif value == 29:
        resistance = 2228
        return resistance
    elif value == 30:
        resistance = 2301
        return resistance
    elif value == 31:                   #3000 ohms
        resistance = 2373
        return resistance
    elif value == 32:
        resistance = 2450
        return resistance
    elif value == 33:
        resistance = 2523
        return resistance
    elif value == 34:
        resistance = 2596
        return resistance
    elif value == 35:
        resistance = 2668
        return resistance
    elif value == 36:                   
        resistance = 2741
        return resistance
    elif value == 37:                   #3500 ohms
        resistance = 2814
        return resistance
    elif value == 38:
        resistance = 2887
        return resistance
    elif value == 39:
        resistance = 2959
        return resistance
    elif value == 40:
        resistance = 3036
        return resistance
    elif value == 41:
        resistance = 3109
        return resistance
    elif value == 42:                   #4000 ohms
        resistance = 3182
        return resistance
    elif value == 43:
        resistance = 3254
        return resistance
    elif value == 44:
        resistance = 3330
        return resistance
    elif value == 45:
        resistance = 3403
        return resistance
    elif value == 46:
        resistance = 3476
        return resistance
    elif value == 47:
        resistance = 3548
        return resistance
    elif value == 48:                   #4500 ohms
        resistance = 3620
        return resistance
    elif value == 49:
        resistance = 3693
        return resistance
    elif value == 50:
        resistance = 3766
        return resistance
    elif value == 51:
        resistance = 3839
        return resistance
    elif value == 52:
        resistance = 3911
        return resistance
    elif value == 53:                   #5000 ohms
        resistance = 3984
        return resistance
    elif value == 54:
        resistance = 4057
        return resistance
    elif value == 55:
        resistance = 4129
        return resistance
    elif value == 56:
        resistance = 4203
        return resistance
    elif value == 57:
        resistance = 4276
        return resistance
    elif value == 58:
        resistance = 4349
        return resistance
    elif value == 59:                   #5500 ohms
        resistance = 4422
        return resistance
    elif value == 60:
        resistance = 4500
        return resistance
    elif value == 61:
        resistance = 4573
        return resistance
    elif value == 62:
        resistance = 4646
        return resistance
    elif value == 63:
        resistance = 4719
        return resistance
    elif value == 64:                   #6000 ohms
        resistance = 4795
        return resistance
    elif value == 65:
        resistance = 4868
        return resistance
    elif value == 66:
        resistance = 4940
        return resistance
    elif value == 67:
        resistance = 5013
        return resistance
    elif value == 68:
        resistance = 5086
        return resistance
    elif value == 69:
        resistance = 5159
        return resistance
    elif value == 70:                   #6500 ohms
        resistance = 5232
        return resistance
    elif value == 71:
        resistance = 5304
        return resistance
    elif value == 72:
        resistance = 5380
        return resistance
    elif value == 73:
        resistance = 5453
        return resistance
    elif value == 74:
        resistance = 5526
        return resistance
    elif value == 75:
        resistance = 5598
        return resistance
    elif value == 76:                   #7000 ohms
        resistance = 5670
        return resistance
    elif value == 77:
        resistance = 5743
        return resistance
    elif value == 78:
        resistance = 5816
        return resistance
    elif value == 79:
        resistance = 5889
        return resistance
    elif value == 80:
        resistance = 5962
        return resistance
    elif value == 81:
        resistance = 6036
        return resistance
    elif value == 82:                   #7500 ohms
        resistance = 6109
        return resistance
    elif value == 83:
        resistance = 6181
        return resistance
    elif value == 84:
        resistance = 6255
        return resistance
    elif value == 85:
        resistance = 6328
        return resistance
    elif value == 86:
        resistance = 6401 
        return resistance
    elif value == 87:
        resistance = 6473 
        return resistance
    elif value == 88:                   #8000 ohms
        resistance = 6551
        return resistance
    elif value == 89:
        resistance = 6624
        return resistance
    elif value == 90:
        resistance = 6697
        return resistance
    elif value == 91:
        resistance = 6769 
        return resistance
    elif value == 92:
        resistance = 6843 
        return resistance
    elif value == 93:                   #8500 ohms
        resistance = 6916 
        return resistance
    elif value == 94:
        resistance = 6989 
        return resistance
    elif value == 95:
        resistance = 7062
        return resistance
    elif value == 96:
        resistance = 7137 
        return resistance
    elif value == 97:
        resistance = 7210 
        return resistance
    elif value == 98:
        resistance = 7283 
        return resistance
    elif value == 99:
        resistance = 7355
        return resistance
    elif value == 100:                   #9000 ohms
        resistance = 7426 
        return resistance
    elif value == 101:
        resistance = 7498
        return resistance
    elif value == 102:
        resistance = 7572 
        return resistance
    elif value == 103:
        resistance = 7644 
        return resistance
    elif value == 104:
        resistance = 7713
        return resistance
    elif value == 105:
        resistance = 7786 
        return resistance
    elif value == 106:                   #9500 ohms
        resistance = 7859 
        return resistance
    elif value == 107:
        resistance = 7931 
        return resistance
    elif value == 108:
        resistance = 8001
        return resistance
    elif value == 109:
        resistance = 8074 
        return resistance
    elif value == 110:
        resistance = 8146 
        return resistance
    elif value == 111:
        resistance = 8219
        return resistance
    elif value == 112:                  #10000 ohms
        resistance = 8292 
        return resistance
    elif value == 113:
        resistance = 8365 
        return resistance
    elif value == 114: 
        resistance = 8438 
        return resistance
    elif value == 115:
        resistance = 8510 
        return resistance
    elif value == 116:
        resistance = 8591
        return resistance
    elif value == 117:
        resistance = 8664
        return resistance
    elif value == 118:
        resistance = 8736 
        return resistance
    elif value == 119:
        resistance = 8809 
        return resistance
    elif value == 120:
        resistance = 8885
        return resistance
    elif value == 121:
        resistance = 8958 
        return resistance
    elif value == 122:
        resistance = 9031 
        return resistance
    elif value == 123:
        resistance = 9103 
        return resistance
    elif value == 124:
        resistance = 9175 
        return resistance
    elif value == 125:
        resistance = 9248 
        return resistance
    elif value == 126:
        resistance = 9321 
        return resistance
    elif value == 127:
        resistance = 9394 
        return resistance
    elif value == 128:
        resistance = 9463
        return resistance
    else:
        return 9500






offset_resistance = 0
height_voltage = 0
voltage = 0



GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

pwm = GPIO.PWM(21, 10000) # 1 kHz frequency
pwm.start(50) # 100% duty cycle


def digi_resistance():
    global range_digi_desire
    while value != 128:
        range_digi = digipot2_table()
        if range_digi < range_digi_desire:
            value += 1
        else:
            value -= 1
            digitest = digipot2_table()
            digitest = range_digi_desire - digitest
            range_digi = range_digi - range_digi_desire 
            if(range_digi < digitest):
                value += 1
                digiprintout = digipot2_table()
                print(f"The chosen resistance is {digiprintout}, While the desired resistance was{range_digi_desire}")
                return value
                
            else:
                digiprintout = digipot2_table()
                print(f"The chosen resistance is {digiprintout}, While the desired resistance was {range_digi_desire}")
                return value
                

                






    print("running")
    time.sleep(1)


def square_wave():
    global voltage
    global range_digi_desire
    global digi_input

    #you want voltage to be twice the highest desired voltage to make it usable for positive and negative
    range_digi_desire = (4755)/(2*voltage)        #inverting op amp with a 1400 ohm resistor and our digipot

    digi_input = digi_resistance()
    #input resistance to digipot with     pi1.spi_write(h, [0b0000_0000, digi_input])

    range_digi_desire = (9463*voltage)/(voltage - 5)
    digi_input = digi_resistance()
    #input resistance to digipot with     pi1.spi_write(h, [0b0001_0000, digi_input])


