const process = require("process");
const express = require("express");
const LogFile = require("logfile");
const RedisClient = require("redis");

// Get the logger instance
const logFile = LogFile.createLogFile("gateway");
const logger = logFile.getLogger();

// Create redis client
const redisClient = new RedisClient(process.env.REDIS_HOST || "localhost", process.env.REDIS_PORT || 26379);

// Register redis events
redisClient.onError((err) => {
    logger.error(err.message);
});

redisClient.onConnect(() => {
    logger.debug("Connecting to the redis database.");
});

redisClient.onReconnect(() => {
    logger.debug("Reconnecting to the redis database.");
});

redisClient.onReady(() => {
    logger.info("Connected to the redis database.");
});

redisClient.onDisconnect(() => {
    logger.info("Disconnected from the redis database.");
});

// Connect to the redis client
logger.debug(`Connecting to the redis database at ${process.env.REDIS_HOST ||
    "localhost"}:${process.env.REDIS_PORT || 6379}`);

// Create an express router
const router = express.Router();

router.post("/request", async (req, res)=>{     //TODO: authentication?
    const domains = req.body.data.domains;
    const id = req.body.data.checklists;

    await redisClient.insert(id, domains);
    res.status(201).send({status: 201, message: "Checks have succesfully been requested", tracker: "..."});
})

router.get("/poll", async (req, res)=>{         //TODO: authentication?
    const results = await redisClient.popEmpty("results");
    res.status(200).contentType("application/json").send(results);
})

router.get("/checklists", async (req, res)=>{   //TODO: authentication?
    res.status(200).send()
})

// Create graceful shutdown method
router.close = async () => {
    await redisClient.disconnect();
};

// Export the router
module.exports = router;
