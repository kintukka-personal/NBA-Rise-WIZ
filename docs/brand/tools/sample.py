"""Sample named boxes: median colour + top clusters. Profile mode: vertical median colour profile.
usage: sample.py IMG name:x0,y0,x1,y1 ...   |   sample.py IMG --profile x0,x1,y0,y1,step"""
import sys
from PIL import Image
import numpy as np
im=Image.open(sys.argv[1]).convert('RGB'); A=np.asarray(im,dtype=np.int32)
hx=lambda c:'#%02X%02X%02X'%tuple(int(v) for v in c)
if sys.argv[2]=='--profile':
    x0,x1,y0,y1,st=map(int,sys.argv[3].split(','))
    for y in range(y0,y1,st):
        print(y, hx(np.median(A[y:y+st,x0:x1].reshape(-1,3),axis=0)))
    sys.exit()
for spec in sys.argv[2:]:
    name,b=spec.split(':'); x0,y0,x1,y1=map(int,b.split(','))
    reg=im.crop((x0,y0,x1,y1)); a=np.asarray(reg).reshape(-1,3)
    q=reg.quantize(colors=4,method=Image.Quantize.MEDIANCUT); pal=q.getpalette(); cs=sorted(q.getcolors(),reverse=True); t=sum(c for c,_ in cs)
    print(f"{name:18} median {hx(np.median(a,axis=0))}  | "+'  '.join(f"{hx(pal[i*3:i*3+3])} {100*c/t:.0f}%" for c,i in cs))
