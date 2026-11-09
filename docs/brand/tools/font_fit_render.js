const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(2000);
const cands=JSON.parse(process.argv[3]); const txt=process.argv[4]; const tag=process.argv[5];
for(const [fam,w] of cands){
  const ok=await p.evaluate(async([f,w])=>{await document.fonts.load(w+' 160px "'+f+'"');return document.fonts.check(w+' 160px "'+f+'"');},[fam,w]);
  const d=await p.evaluate(([f,w,t])=>renderText('"'+f+'"',w,t),[fam,w,txt]);
  fs.writeFileSync(`fit_${tag}_${fam.replace(/[^A-Za-z0-9]/g,'')}_${w}.png`,Buffer.from(d.split(',')[1],'base64'));
  if(!ok) console.log('NOT LOADED',fam,w);}
await b.close();})();
