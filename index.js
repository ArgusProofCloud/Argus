const fs=require("fs")
let rawdata=fs.readFileSync("./API.json")
let data=JSON.parse(rawdata)

const express=require("express")
const http= require("http")
const bp=require("body-parser")
const app=express() //express gebruiken

//userKey="7c10e90b58798304a7b3ef2135ad16f0a5a109123a645b6014d46d400157402a" //juiste key
//userKey="hello"
// log functie= middelware functie

const log =(req,res,next)=>{
    
    //console.log(userKey) //keysloggen
     
    if(checkKey(userKey))
    {
        next()
    }
    else
    {
       // console.log("niet juiste api") //niet juiste api loggen
        res.status(401).send('unautorised')
        
    }
}


function checkKey(userKey)
        {
            getKey()
            for (var i = 0; i < data.keys.length; i++) 
            {

               //console.log(data.keys[i]) // keys loggen
               
             
                if(userKey==data.keys[i])
                {
                   
                    return responseCheck=true
                }
              
            }
        }

fs.watch("./API.json",(eventType,file)=>{
 
 if(eventType == 'change')
 {
    getKey()
    
    //changed datakeys loggen
    // for (var i = 0; i < data.keys.length; i++) 
    // {

    //    console.log(data.keys[i])   
          
    // }

    
 }
 
})

function getKey()
        {
         
         rawdata=fs.readFileSync("./API.json")
         return data=JSON.parse(rawdata)
          
        }



// van vorige code index.js        
app.use(log)
app.use(bp.json())
app.use(bp.urlencoded({extended:true}))
app.post("/login/:userkey",function(req,res)
{     
    
    res.send("hallo autorised user")
   
})

app.get("/home",(req,res)=>{res.send("hallo home")})
app.listen(3000,err=>{
    if(err)
        console.log(err)
    console.log("listening on port 3000")
})

module.exports={log} //export log
module.exports=app;