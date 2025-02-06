from machine import ADC, Pin, I2C
import i2c_lcd
import dht
from time import sleep_ms

class AWCS():
    def __init__(self, pipeTempPin, dhtPin):
        self.lcdSize = (2, 16)

        i2c = I2C(0, sda=Pin(17), scl=Pin(16), freq=400000)
        self.lcd1 = i2c_lcd.I2cLcd(i2c, 0x27, *self.lcdSize)
        self.lcd2 = i2c_lcd.I2cLcd(i2c, 0x26, *self.lcdSize)

        self.pipeTemp = ADC(Pin(pipeTempPin))
        self.pipeTemp.atten(ADC.ATTN_11DB)

        self.dht_sensor = dht.DHT11(Pin(dhtPin))

        self.lcd1.putstr("LCD Setup completed")
        self.lcd2.putstr("LCD Setup completed")
        print("LCD Setup completed")
        sleep_ms(1000)
        self.lcd1.clear()
        self.lcd2.clear()



    def get_DHT_data(self):
        self.dht_sensor.measure()
        return self.dht_sensor.temperature(), self.dht_sensor.humidity()


    def display_data(self):
        dht_temp, dht_hum = self.get_DHT_data()

        line1 = f"Pipe Temp: {dht_temp}"
        line2 = f"Pipe Humidity: {dht_temp}C {dht_hum}%"

        self.write_lcd(line1, line2)

    def write_lcd(self, text_line_1, text_line_2):
        """Displays text on both LCD screens."""
        self.lcd1.clear()
        self.lcd2.clear()
        self.lcd1.putstr(text_line_1)
        self.lcd2.putstr(text_line_1)
        self.lcd1.move_to(0, 1)
        self.lcd2.move_to(0, 1)
        self.lcd1.putstr(text_line_2)
        self.lcd2.putstr(text_line_2)
        self.lcd1.move_to(0, 0)
        self.lcd2.move_to(0, 0)
