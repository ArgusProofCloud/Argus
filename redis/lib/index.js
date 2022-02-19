const redis = require("redis");


class Redis
{
    constructor(port, host)
    {
        this.client = redis.createClient(port, host)

        this.client.on("connect", function(err){
            this.Onerror(err)
            console.log("connected")
        })
    }

    async InsertCheck(check, domain)
    {
        //inserts checks at the bottom => FIFO
        await this.client.rpush(check, JSON.stringify(domain), (err, res)=>{
            this.Onerror(err)
            return res
        })
    }

    async DelCheck(check)
    {
        //delete the oldest in the "check" list
        await this.client.lpop(check, (err, res)=>{
            this.Onerror(err)
            return res
        })
    }

    async ReadCheck(check)
    {
        //return the oldest in the check list
        await this.client.lrange(check, 0, 0, (err, res)=>{
            this.Onerror(err)
            return res
        })
    }


    Onerror(err)
    {
        this.client.on("error", function (){
            //logger err
        })
    }

}

module.exports = Redis