const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(2500);
const C=JSON.parse(process.argv[3]);
for(const [tag,css] of C){ for(const txt of ['18545','11717']){
  const ok=await p.evaluate(async(css)=>{await document.fonts.load(css);return document.fonts.check(css);},css);
  const d=await p.evaluate(([css,t])=>renderText(css,t),[css,txt]);
  fs.writeFileSync(`tp_${tag}_${txt}.png`,Buffer.from(d.split(',')[1],'base64'));
  if(!ok) console.log('NOT LOADED',tag);}}
await b.close();})();
