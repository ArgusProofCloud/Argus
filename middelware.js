const { redirect } = require("express/lib/response")
const router=require("./index")
const fs=require("fs")
const keydata =require("./API.json")


userKey="7c10e90b58798304a7b3ef2135ad16f0a5a109123a645b6014d46d400157402a" //juiste key
//userKey="hello"
const log =(req,res,next)=>{
    console.log(req.body)
    if(checkKey(userKey))
    {
        next()
    }
    else
    {
        console.log("niet juiste api")
        res.status(401).send('unautorised')
        
    }
}

function checkKey(userKey)
        {
            for (var i = 0; i < keydata.keys.length; i++) 
            {

               
             
                if(userKey==keydata.keys[i])
                {
                   
                    return responseCheck=true
                }
              
            }
        }


module.exports={log} //export log