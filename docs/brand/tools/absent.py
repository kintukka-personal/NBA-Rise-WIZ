"""Search for the colour farthest (min OKLab dE, normal + protan/deutan/tritan) from every measured game accent,
that also reads as a marker on white and as a rule on the game's slate."""
import numpy as np, colorsys, sys, json
GAME = sys.argv[1].split(',')
def hex2rgb(h): h=h.lstrip('#'); return np.array([int(h[i:i+2],16) for i in (0,2,4)])/255
def lin(c): return np.where(c<=0.04045,c/12.92,((c+0.055)/1.055)**2.4)
def oklab(rgb):
    l=lin(rgb); M1=np.array([[0.4122214708,0.5363325363,0.0514459929],[0.2119034982,0.6806995451,0.1073969566],[0.0883024619,0.2817188376,0.6299787005]])
    lms=np.cbrt(M1@l); M2=np.array([[0.2104542553,0.7936177850,-0.0040720468],[1.9779984951,-2.4285922050,0.4505937099],[0.0259040371,0.7827717662,-0.8086757660]])
    return M2@lms
# Machado 2009 severity 1.0 (linear RGB)
CVD={'protan':np.array([[0.152286,1.052583,-0.204868],[0.114503,0.786281,0.099216],[-0.003882,-0.048116,1.051998]]),
     'deutan':np.array([[0.367322,0.860646,-0.227968],[0.280085,0.672501,0.047413],[-0.011820,0.042940,0.968881]]),
     'tritan':np.array([[1.255528,-0.076749,-0.178779],[-0.078411,0.930809,0.147602],[0.004733,0.691367,0.303900]])}
def sim(rgb,k):
    l=np.clip(CVD[k]@lin(rgb),0,1); return np.where(l<=0.0031308,12.92*l,1.055*l**(1/2.4)-0.055)
def lum(rgb): l=lin(rgb); return 0.2126*l[0]+0.7152*l[1]+0.0722*l[2]
def cr(a,b): la,lb=sorted([lum(a),lum(b)]); return (lb+0.05)/(la+0.05)
G=[hex2rgb(h) for h in GAME]; WHITE=hex2rgb('#F4F6F7'); SLATE=hex2rgb('#2A2E32')
best=[]
for h in range(0,360,2):
  for L in np.arange(0.38,0.66,0.02):
    for S in (0.75,0.85,0.95,1.0):
      c=np.array(colorsys.hls_to_rgb(h/360,L,S))
      if cr(c,WHITE)<3.0 or cr(c,SLATE)<float(__import__("os").environ.get("SL","2.6")): continue
      worst=99; why=''
      for g,hx in zip(G,GAME):
        for k in ('normal','protan','deutan','tritan'):
          a=oklab(c) if k=='normal' else oklab(sim(c,k)); b=oklab(g) if k=='normal' else oklab(sim(g,k))
          d=np.linalg.norm(a-b)*100*(1 if k=='normal' else 1.0)
          if k=='normal': d=d  # same scale
          if d<worst: worst=d; why=f'{hx}/{k}'
      best.append((worst,'#%02X%02X%02X'%tuple(int(round(v*255)) for v in c),h,round(L,2),S,why,round(cr(c,WHITE),2),round(cr(c,SLATE),2)))
best.sort(reverse=True)
for b in best[:15]: print(b)
