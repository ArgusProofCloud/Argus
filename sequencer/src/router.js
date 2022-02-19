const express = require("express");
const LogFile = require("logfile");

// Get the logger instance
const logFile = LogFile.createLogFile("sequencer.log");
const logger = logFile.getLogger();


// Create an express router
const router = express.Router();

// Get job from specified queue
router.get("/job/:id", async (req, res) => {

    const queueId = req.params.id;
    logger.debug(`Finding jobs in ${queueId} queue.`);

    // TODO: Query Redis

    res.status(404).send({status: 404, message: "No jobs are ready for execution"});
});

// Post results
router.post("/result/:id", async (req, res) => {

    const queueId = req.params.id;
    logger.debug(`Adding results to ${queueId} queue.`);

    const results = req.body;
    logger.debug(JSON.stringify(req.body));

    // TODO: Add to redis queue

    res.status(201).send({status: 201, message: "Results successfully registered."})
});


// Create graceful shutdown method
router.close = async () => {
    logger.info("Closed Redis connection.");
};

// Export the router
module.exports = router;
