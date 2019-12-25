import OPi.GPIO as GPIO

GPIO.setboard(GPIO.PCPCPLUS)

GPIO.setmode(GPIO.BOARD)
# for i in range (1, 25):
#     try:
#         GPIO.setup(i, 1)
#         print(i)
#     except:
#         pass
GPIO.setup(15, GPIO.OUT)
