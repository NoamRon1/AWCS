import dht
from machine import Pin
from time import sleep

sensor = dht.DHT11(Pin(5))
while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature:", temp, "Humidity:", hum)
    except OSError as e:
        print("Sensor error:", e)
    sleep(2)

