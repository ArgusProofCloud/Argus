const redis = require("redis");

class Redis
{
    constructor(port, host)
    {
        this.client = redis.createClient(port, host);

        this.client.on("connect", function(err){
            this.Onerror(err);
            console.log("connected");
        });
    }

    Insert(Id, Value)
    {
        //inserts Id with value at the bottom => FIFO
        return this.client.RPUSH(Id, JSON.stringify(Value));
        this.Onerror();
    }

    Pop(Id){
        //delete and return Oldest Id
        return this.client.LPOP(Id);
        this.Onerror();
    }

    async PopEmpty(Id){
        //delete and return entire Id list
        amount= await this.client.LLEN(Id);
        return this.client.LPOP(Id, amount);
        this.Onerror();
    }


    Onerror()
    {
        this.client.on("error", function (){
            //logger err
        });
    }

}

module.exports = Redis;