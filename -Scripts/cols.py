
import colorsys

def hex_to_rgb(hex):
    if len(hex)==6:
        ret= [ int('0x'+hex[:2], 0), int('0x'+hex[2:4], 0), int('0x'+hex[4:6], 0) ]
    if len(hex)==3:
        ret= [ int('0x'+hex[0]*2, 0), int('0x'+hex[1]*2, 0), int('0x'+hex[2]*2, 0) ]
    print(ret)
    return ret

def rgb_to_hex(rgb):
    print(rgb)
    r, g, b = rgb
    return hex(r)[2:4] + hex(g)[2:4] + hex(b)[2:4]

def inverse(rgb):
    r, g, b = rgb
    h, l, s = colorsys.rgb_to_hls(r,g,b)
    l = 360 - l
    print([h,l,s])
    r1,g1,b1= colorsys.hls_to_rgb(h,l,s)
    return [int(r1), int(g1), int(b1)]


color=input('hex?: ')

print(colorsys.rgb_to_hls(*hex_to_rgb(color)))
