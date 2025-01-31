import board
import displayio
import framebufferio
import rgbmatrix
import time
import random

displayio.release_displays()
matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=6,
    rgb_pins=[board.MTX_R1, board.MTX_G1, board.MTX_B1, board.MTX_R2, board.MTX_G2, board.MTX_B2],
    addr_pins=[board.MTX_ADDRA, board.MTX_ADDRB, board.MTX_ADDRC, board.MTX_ADDRD],
    clock_pin=board.MTX_CLK, latch_pin=board.MTX_LATCH, output_enable_pin=board.MTX_OE
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
