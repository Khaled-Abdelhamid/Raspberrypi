import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
pwm=GPIO.PWM(22, 50)
pwm.start(2)







def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(22, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(22, False)
	pwm.ChangeDutyCycle(0)

SetAngle(90)

pwm.stop()
GPIO.cleanup()
