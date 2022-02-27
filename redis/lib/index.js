const ioredis = require("ioredis");

/**
 * this class contains all methods needed to connect with an ioredis server
 * the constructor demands a host and port. If no port is given, the default port 6379 will be used
 * good to know: when ioredis returns a "null" opbject; it returns an empty string instead
 */
class Redis
{
    /**
     * @param {string} host
     * @param {number} port
     */
    constructor(host, port=6379)
    {
        this.client = new ioredis({
            port: port,
            host: host
            //password: x
        })
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
     * @param {string} Job
     * @param {any} Value JSON-object that gets parsed to a string
     * @returns {Promise<number>}
     * returns Job with value according to the FIFO principle
     */
    insert(Job, Value)
    {
        return this.client.rpush(Job, JSON.stringify(Value));
    }

    /**
     * @param {string} Job
     * @returns {Promise<string>}
     * deletes and returns the oldest job
     */
    pop(Job)
    {
        return this.client.lpop(Job);
    }

    /**
     * @param {string} Job
     * @returns {Promise<string[]>}
     * deletes and returns a job list
     */
    async popEmpty(Job)
    {
        const amount= await this.client.llen(Job);
        return this.client.lpop_count(Job, amount);
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
