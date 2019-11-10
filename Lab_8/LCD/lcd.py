import time
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD

lcd = CharLCD(cols = 16, rows = 2, pin_rs = 37, pin_e = 35, pins_data = [40, 38,36,32,33,31,29,23], numbering_mode = GPIO.BOARD)

lcd.cursor_pos = (1,3)

while True:
    lcd.write_string(u"Hello world!")
    time.sleep(1)
    lcd.clear()
    time.sleep(1)


lcd.close()
GPIO.cleanup()
