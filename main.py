from AWCS import AWCS

system = AWCS([5, 6], [0x27, 0x26], 7)

for i in range(1):
    datas = system.get_DHT_data()
    system.display_data(datas)


