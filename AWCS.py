from machine import ADC, Pin, I2C
import i2c_lcd
import dht
from time import sleep_ms, sleep


class AWCS:
    def __init__(self, pipeTempPin, dhtPin):
        self.lcdSize = (2, 16)

        i2c = I2C(0, sda=Pin(17), scl=Pin(16), freq=400000)
        self.lcd1 = i2c_lcd.I2cLcd(i2c, 0x27, *self.lcdSize)
        self.lcd2 = i2c_lcd.I2cLcd(i2c, 0x26, *self.lcdSize)

        self.dht_sensor = dht.DHT11(Pin(dhtPin, Pin.IN, Pin.PULL_UP))

    def setup_completed(self):
        self.lcd1.putstr("LCD Setup completed")
        self.lcd2.putstr("LCD Setup completed")
        print("LCD Setup completed")
        sleep_ms(1000)
        self.lcd1.clear()
        self.lcd2.clear()

    def get_DHT_data(self):
        try:
            self.dht_sensor.measure()
            temp = self.dht_sensor.temperature()
            hum = self.dht_sensor.humidity()
            print("Temperature:", temp, "Humidity:", hum)
        except OSError as e:
            print("Sensor error:", e)
        sleep(2)
        return temp, hum

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

    def run(self):
        setup_completed()
        for i in range(100):
            temp, hum = get_DHT_data()
            # not completed.

