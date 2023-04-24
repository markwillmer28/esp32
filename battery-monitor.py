# SPDX-FileCopyrightText: Copyright (c) 2023 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import time
import board
from adafruit_max1704x import MAX17048
import microcontroller
import board
import digitalio

switch = digitalio.DigitalInOut(board.D1)
switch.direction = digitalio.Direction.INPUT
#
i2c = board.I2C()
while not i2c.try_lock():
    pass
i2c_address_list = i2c.scan()
i2c.unlock()

device = None

if 0x36 in i2c_address_list:
    max17048 = MAX17048(board.I2C())

    device = max17048

else:
    raise Exception("Battery monitor not found.")

while device:
    print(f"Battery voltage: {device.cell_voltage:.2f} Volts")
    print(f"Battery percentage: {device.cell_percent:.1f} %")
    print(f"Board temperature: {microcontroller.cpu.temperature:.1f} C")
    print(f"Button state: {switch.value}");
    print("")
    time.sleep(1)
