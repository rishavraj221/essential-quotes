#!/usr/bin/env python
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time

class windowDisplay(object):
    def __init__(self):
        self.options = RGBMatrixOptions()
        self.options.rows = 32
        self.options.cols = 64
        self.options.chain_length = 4
        self.options.pwm_bits = 6
        self.options.pwm_lsb_nanoseconds = 300
        self.options.parallel = 1
        self.options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
        self.font = graphics.Font()
        self.font.LoadFont("rpi-rgb-led-matrix/fonts/9x18.bdf")
        self.textColor = graphics.Color(255, 0, 0)
    def initiate(self):
        self.matrix = RGBMatrix(options = self.options)
        self.offscreen_canvas = self.matrix.CreateFrameCanvas()

    def set(self, m):
        self.msg = m

    def show(self):
       pos = self.offscreen_canvas.width
       vpos = 20
       loops = 0
       while (loops < 2):
         self.offscreen_canvas.Clear()
         mlen = graphics.DrawText(self.offscreen_canvas, self.font, pos, vpos, self.textColor, self.msg) # lenght of msg
         pos -= 1
         if (pos + mlen < 0):
             pos = self.offscreen_canvas.width
             loops += 1

         time.sleep(0.05)
         self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)

    def clear(self):
        self.matrix.Clear()
