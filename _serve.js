const http=require('http'), fs=require('fs'), path=require('path');
const ROOT='/Users/m.ravikumar/Documents/TM_ClientConfiguration';
const PORT=parseInt(process.argv[2],10)||4601;
http.createServer((req,res)=>{
  let p=decodeURIComponent(req.url.split('?')[0]);
  if(p==='/'||p==='') p='/TM_Client_Config_App.html';
  const fp=path.join(ROOT,p);
  fs.readFile(fp,(e,data)=>{
    if(e){res.writeHead(404);res.end('not found');return;}
    const ext=path.extname(fp);
    const ct=ext==='.html'?'text/html':ext==='.svg'?'image/svg+xml':'application/octet-stream';
    res.writeHead(200,{'Content-Type':ct});res.end(data);
  });
}).listen(PORT,()=>console.log('listening '+PORT));
