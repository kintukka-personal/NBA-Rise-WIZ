"""Hue occupancy of saturated UI pixels across many images; reports empty hue arcs.
usage: huegap.py out.json img1 img2 ...  (each image may carry ':x0,y0,x1,y1' crop)"""
import sys, json, numpy as np
from PIL import Image
out=sys.argv[1]; bins=np.zeros(360); n_img=0
for spec in sys.argv[2:]:
    f,_,box=spec.partition(':')
    try: im=Image.open(f).convert('RGB')
    except Exception: continue
    if box: im=im.crop(tuple(map(int,box.split(','))))
    im.thumbnail((700,700)); a=np.asarray(im,dtype=np.float32)/255
    mx=a.max(2); mn=a.min(2); l=(mx+mn)/2; d=mx-mn
    s=np.where(d==0,0,d/(1-np.abs(2*l-1)+1e-6))
    r,g,b=a[...,0],a[...,1],a[...,2]
    h=np.where(mx==r,((g-b)/(d+1e-6))%6,np.where(mx==g,(b-r)/(d+1e-6)+2,(r-g)/(d+1e-6)+4))*60
    m=(s>0.45)&(l>0.22)&(l<0.85)
    hist,_=np.histogram(h[m],bins=360,range=(0,360)); bins+=hist/ max(1,m.size); n_img+=1
share=bins/bins.sum()
occ=share>float(__import__("os").environ.get("THR","0.0015"))
# find empty arcs (circular)
arcs=[];i=0
ext=np.concatenate([occ,occ])
start=None
for k in range(720):
    if not ext[k] and start is None: start=k
    if ext[k] and start is not None:
        if k-start>=8 and start<360: arcs.append((start%360,(k-1)%360,k-start))
        start=None
arcs=sorted(set(arcs),key=lambda a:-a[2])
print('images',n_img)
print('largest empty hue arcs (start,end,width):',arcs[:8])
top=np.argsort(-share)[:12]; print('busiest hues:',[(int(t),round(float(share[t])*100,2)) for t in top])
json.dump({'images':n_img,'share':share.round(6).tolist(),'empty_arcs':arcs},open(out,'w'))
