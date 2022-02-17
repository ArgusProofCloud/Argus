const redis = require("redis");

const port= 6363 //in conf file
const host='127.0.0.1' //in conf file

class Redis
{
    constructor()
    {
        const client = redis.createClient(port, host)

        client.on("error", function(err){
            console.log(err)
        });

        client.on("connect", function(err){
            console.log("connected")
        })
    }

    InsertInstr = ()=>
    {
        await client.connect()
        //RPUSH (json to string!)
        await client.quit()
    }

    GetInstr = ()=>
    {
        await client.connect()
        //LPOP
        await client.quit()
    }

    ReadInstr = ()=>
    {
        await client.connect()
        //lrange
        await client.quit()
    }

}

module.exports = Redis