from machine import ADC, Pin, I2C
import i2c_lcd
import dht
from time import sleep_ms, sleep


class AWCS:
    def __init__(self, dhtPins=[5,6], lcdAddr=[0x27, 0x26], buttonsPin=7):
        #self.lcdSize = (2, 16)

        #i2c = I2C(sda=Pin(17), scl=Pin(16), freq=400000)
        #self.lcdYes = i2c_lcd.I2cLcd(i2c, lcdAddr[0], *self.lcdSize)
        #self.lcdNo = i2c_lcd.I2cLcd(i2c, lcdAddr[1], *self.lcdSize)

        self.dht_sensorYes = dht.DHT11(Pin(dhtPins[0], Pin.IN, Pin.PULL_UP))
        self.dht_sensorNo = dht.DHT11(Pin(17, Pin.IN, Pin.PULL_UP))

        #self.sys_switch = Pin(buttonsPin, Pin.IN, Pin.PULL_UP)

        #self.screens = [self.lcdYes, self.lcdNo]

    def setup_completed(self):
        self.lcdYes.putstr("LCD Setup completed")
        self.lcdNo.putstr("LCD Setup completed")
        print("LCD Setup completed")
        sleep_ms(1000)
        self.lcdYes.clear()
        self.lcdNo.clear()

    def get_DHT_data(self):
        try:
            self.dht_sensorYes.measure()
            #self.dht_sensorNo.measure()
            dataYes = [self.dht_sensorYes.temperature(), self.dht_sensorYes.humidity()]
            #dataNo = [self.dht_sensorNo.temperature(), self.dht_sensorNo.humidity()]
            dataNo = [0, 0]
            #print("Yes Temperature:", dataYes[0], "Yes Humidity:", dataYes[1])
            #print("No Temperature:", dataNo[0], "No Humidity:", dataNo[1])
            datas = [dataYes, dataNo]
            sleep(2)
            return datas
        except OSError as e:
            print("Sensor error:", e)
            sleep(2)
            return [[0,0],[0,0]]

    def display_data(self, datas):
        for i in range(2):
            line1 = f"Home {i} Temp: {datas[i][0]}C."
            line2 = f"Home {i} Humidity: {datas[i][1]}%."
            print(line1 + "\n" + line2)
            #self.write_lcd(self.screens[i], line1, line2)

    def write_lcd(self, lcd, text_line_1, text_line_2):
        """Displays text on a givven LCD screens."""
        lcd.clear()
        lcd.putstr(text_line_1)
        lcd.move_to(0, 1)
        lcd.putstr(text_line_2)
        lcd.move_to(0, 0)

    def run(self):
        self.setup_completed()
        while (self.sys_switch.value()): #while the switch is HIGH - 3.3v - True.
            datas = self.get_DHT_data()
            self.display_data(datas)

        print("Code ended")



