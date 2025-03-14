import board
import displayio
import framebufferio
import rgbmatrix
import time
import random

displayio.release_displays()
matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=1,
    rgb_pins=[board.IO1, board.IO2, board.IO3, board.IO5, board.IO4, board.IO6],
    addr_pins=[board.IO8, board.IO7, board.IO10, board.IO9],
    clock_pin=board.IO12, latch_pin=board.IO11, output_enable_pin=board.IO13
)

def blink(bitmaps):
    for bitmap in bitmaps:
        tile_grid.bitmap = bitmap
        time.sleep(0.1)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)
frames = ["protogen_0.bmp", "protogen_1.bmp", "protogen_2.bmp", "protogen_3.bmp", "protogen-4.bmp"]
group = displayio.Group()
display.root_group = group
bitmaps = [displayio.OnDiskBitmap(f) for f in frames]
tile_grid = displayio.TileGrid(bitmaps[0], pixel_shader=bitmaps[0].pixel_shader)
group.append(tile_grid)

while True:
    blink(bitmaps)
    bitmaps.reverse()
    blink(bitmaps)
    bitmaps.reverse()
    time.sleep(random.uniform(3,6))
