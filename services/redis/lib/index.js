const IoRedis = require("ioredis");
const RedLock = require("redlock").default;

/**
 * this class contains all methods needed to connect with a redis server
 * the constructor demands a host and port. If no port is given, the default port 26379 will be used
 */
class Redis
{
    /**
     * @param {string} host
     * @param {number} port
     */
    constructor(host, port=26379, password = "")
    {
        const options = {
            sentinels: [
                {
                    port: port,
                    host: host
                }
            ],
            name: "mymaster"
        };

        if(password)
        {
            options.sentinelPassword = password;
            options.password = password;
        }

        this.client = new IoRedis(options);
        this.redLock = new RedLock([this.client]);
    }

    /**
     * @returns {Promise<void>}
     * closes connection immediately, regardless of pending replies
     */
    disconnect()
    {
        return this.client.disconnect();
    }

    /**
     * @returns {Promise<void>}
     * closes connection after all pending replies are resolved
     */
    quit()
    {
        return this.client.quit();
    }

    /**
     * @param {string} key
     * @param {any} value JSON-object that gets parsed to a string
     * @returns {Promise<number>}
     * returns Key with value according to the FIFO principle
     */
    insert(key, value)
    {
        return this.client.rpush(key, JSON.stringify(value));
    }

    /**
     * @param {string} key
     * @returns {Promise<string>}
     * deletes and returns the oldest job
     */
    pop(key)
    {
        return this.client.lpop(key);
    }

    /**
     * @param {string} key
     * @returns {Promise<string[]>}
     * deletes and returns a list
     */
    async popEmpty(key)
    {
        const self = this;
        let list;
        await this.redLock.using([key + ":lock"], 5000, async signal => {
            const amount = await self.client.llen(key);

            if (signal.aborted)
            {
                throw signal.error;
            }

            list = await self.client.lpop(key, amount);
        });
        return list;
    }

    /**
     * Return the queue length.
     * @param {string} key
     * @returns {Promise<number>}
     */
    length(key)
    {
        return this.client.llen(key);
    }

    /**
     * @param {string} key the queue in which the value will be stored
     * @param {any} value
     * @returns {Promise<string>}
     * performs a sorted set on a certain queue
     */
    sortedSet(key, value)
    {
        // set expiration on key to 10 mins
        this.client.setex(key,600,value);
        return this.client.zadd(key, Date.now(), value);
    }

    /**
     * @param {string} key
     * @returns {Promise<string[]>}
     */
    sortedGet(key)
    {
        return this.client.zrange(key,0,-1, "WITHSCORES" );
    }


    /**
     * @param {(...args: any[])=> void} callback
     */
    onErrorRedLock(callback)
    {
        this.redLock.on("error", callback);
    }

    /**
     * @param {(...args: any[])=> void} callback
     */
    onError(callback)
    {
        this.client.on("error", callback);
    }

    /**
     * @param {(...args: any[])=> void} callback
     */
    onConnect(callback)
    {
        this.client.on("connect", callback);
    }

    /**
     * @param {(...args: any[])=> void} callback
     */
    onReady(callback)
    {
        this.client.on("ready", callback);
    }

    /**
     * @param {(...args: any[])=> void} callback
     */
    onDisconnect(callback)
    {
        this.client.on("end", callback);
    }

    /**
     * @param {(...args: any[])=> void} callback
     */
    onReconnect(callback)
    {
        this.client.on("reconnect", callback);
    }
}

module.exports = Redis;
