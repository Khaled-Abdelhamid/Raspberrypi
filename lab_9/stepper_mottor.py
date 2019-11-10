
import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)
# Define GPIO signals to use Pins 18,22,24,26 GPI024,GPI025,GPI08,GPI07
StepPins = [ 24,25,8,7]
# Set all pins as output
for pin in StepPins:
    print "Setup pins"
    GPIO. setup ( pin,GPIO. OUT )
    GPIO. output ( pin, False)
# Define some settings
WaitTime = 0.005
# Define advanced half
StepCount2 = 8
Seq2 = [ ]
Seq2 = range ( 0, StepCount2 )
Seq2 [ 0 ] = [1,0,0,0 ]
Seq2 [1] = [1,1,0,0 ]
Seq2 [ 2 ] = [ 0,1,0,0 ]
Seq2 [ 3 ] = [ 0,1,1,0 ]
Seq2 [ 4 ] = [ 0,0,1,0 ]
Seq2 [ 5 ] = [ 0,0,1,1]
Seq2 [ 6 ] = [ 0,0,0,1]
Seq2 [ 7 ] = [1,0,0,1]
# Choose a sequence to use
Seq = Seq2
StepCount = StepCount2
def steps(nb):
    StepCounter = 0
    sign =1
    if nb<0:sign=l
    else:sign= -1
    nb=abs(sign*nb*2) #times
    print("nbsteps {} and sign {}".format(nb,sign))
    for i in range(nb):
        for pin in range(4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin]!=0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin , False)
        StepCounter += sign
# If we reach the end of the sequence
# start again
        if (StepCounter==StepCount):
            StepCounter = 0
        if (StepCounter<0):
            StepCounter = StepCount -1
# Wait before moving on
        time.sleep(WaitTime)
# Start main loop
nbStepsPerRev=2048
hasRun=False
while not hasRun :
    steps(nbStepsPerRev)
    time.sleep(1)
    steps( - nbStepsPerRev)
    time.sleep(1)
    hasRun=True
print "Stop motor"
for pin in StepPins:
    GPIO.output(pin, False)


GPIO.cleanup()