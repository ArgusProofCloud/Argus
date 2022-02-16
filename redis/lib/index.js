const redis = require("redis");
port= 6360
host='127.0.0.1'

const client = redis.createClient(port, host);

client.on("error", function(err){
    console.error("error: ", err)
});

client.on("connect", function(err){
    console.log("Redis connected")
})


//6360