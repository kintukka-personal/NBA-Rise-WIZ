"""Median-cut palette + hue stats for an image region. Usage: palette.py IMG x0 y0 x1 y1 [ncolors]"""
import sys, colorsys
from PIL import Image
import numpy as np
f=sys.argv[1]; box=tuple(int(v) for v in sys.argv[2:6]); n=int(sys.argv[6]) if len(sys.argv)>6 else 24
im=Image.open(f).convert('RGB').crop(box)
q=im.quantize(colors=n, method=Image.Quantize.MEDIANCUT)
pal=q.getpalette()[:n*3]; cnt=sorted(q.getcolors(), reverse=True)
tot=sum(c for c,_ in cnt)
for c,i in cnt:
    r,g,b=pal[i*3:i*3+3]; h,l,s=colorsys.rgb_to_hls(r/255,g/255,b/255)
    print(f"#{r:02X}{g:02X}{b:02X}  {100*c/tot:5.1f}%  hue {h*360:5.0f}  L {l*100:4.0f}  S {s*100:4.0f}")
a=np.asarray(im,dtype=np.int32); lum=a.mean(axis=2); dark=a[lum<60]
if len(dark):
    rb=(dark[:,0]-dark[:,2]); print(f"dark px {len(dark)}: mean R-B {rb.mean():+.2f}  share blue>red {(rb<0).mean()*100:.1f}%  mean RGB {dark.mean(axis=0).round(1)}")
