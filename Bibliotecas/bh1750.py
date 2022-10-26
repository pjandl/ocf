#   Copyrigth 2022 Peter Jandl Junior
#
#   Based on Peter Dahlberg code from
#   
#   Copyright 2016 Peter Dahlberg
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import time

OP_SINGLE_HRES1 = 0x20
OP_SINGLE_HRES2 = 0x21
OP_SINGLE_LRES = 0x23

DELAY_HMODE = 180  # 180ms in H-mode
DELAY_LMODE = 24  # 24ms in L-mode


class BH1750:
    """
        Class to represente BH1750 I2C luminance sensor.
    """
    def __init__(self, i2c=None, mode=OP_SINGLE_HRES1, i2c_address=0x23):
        # Check i2c object
        if i2c is None:
            raise ValueError('I2C object must be supplied.')
        self._i2c = i2c
        # Check that mode is valid.
        if mode not in [OP_SINGLE_HRES1, OP_SINGLE_HRES2, OP_SINGLE_LRES]:
            raise ValueError(
                'Unexpected mode value {0}. Set mode to one of '
                'OP_SINGLE_HRES1, OP_SINGLE_HRES2, OP_SINGLE_LRES'.format(mode))
        self._mode = mode
        self._i2c_address = i2c_address
        
    def read_luminance(self):
        """
            Performs a single sampling. returns the result in lux
        """
        self._i2c.writeto(self._i2c_address, b"\x00")  # make sure device is in a clean state
        self._i2c.writeto(self._i2c_address, b"\x01")  # power up
        self._i2c.writeto(self._i2c_address, bytes([self._mode]))  # set measurement mode

        time.sleep_ms(DELAY_LMODE if self._mode == OP_SINGLE_LRES else DELAY_HMODE)

        raw = self._i2c.readfrom(self._i2c_address, 2)
        self._i2c.writeto(self._i2c_address, b"\x00")  # power down again

        # we must divide the end result by 1.2 to get the lux
        return ((raw[0] << 24) | (raw[1] << 16)) // 78642

    @property
    def luminance(self):
        "Return the luminance in lux."
        return "{} lux".format(self.read_luminance())

        