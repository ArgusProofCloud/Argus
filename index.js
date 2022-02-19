// definieren van package
const express=require("express")
const http= require("http")
const bp=require("body-parser")
const {log} =require("./middelware")
const { response } = require("express")
const app=express() //express gebruiken


app.use(log)
app.use(bp.json())
app.use(bp.urlencoded({extended:true}))
app.post("/login",function(req,res)
{     
    console.log("authorised")
    res.send("hallo autorised user")
   
})

app.get("/home",(req,res)=>{res.send("hallo home")})
app.listen(3000,err=>{
    if(err)
        console.log(err)
    console.log("listening on port 3000")
})

module.exports=app;