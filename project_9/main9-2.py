from gpiozero import PWMLED
import smbus
import time
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47

bus = smbus.SMBus(1)
Device_Address = 0x68

buzzer_pin = 18
buzzer = PWMLED(buzzer_pin)

def MPU_Init():
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    bus.write_byte_data(Device_Address, CONFIG, 0)
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr + 1)
    value = (high << 8) | low
    if value > 32768:
        value = value - 65536
    return value

try:
    MPU_Init()
    acc_data = sum(read_raw_data(ACCEL_XOUT_H) / 16384.0 for _ in range(10)) / 10
    print(acc_data)

    while True:
        acc_x = read_raw_data(ACCEL_XOUT_H) / 16384.0
        if acc_x - acc_data >= 0.1:
            print("shock!!")
            buzzer.blink(on_time=0.2, off_time=0.2, n=5)
        else:
            buzzer.off()

except KeyboardInterrupt:
    pass

finally:
    buzzer.close()
