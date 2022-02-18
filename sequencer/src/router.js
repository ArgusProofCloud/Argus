const express = require("express");
const LogFile = require("logfile");

const logFile = LogFile.createLogFile("sequencer.log");
const logger = logFile.getLogger();

const router = express.Router();

router.get("/job/:id", async (req, res) => {

    const queueId = req.params.id;
    logger.debug(`Finding jobs in ${queueId} queue.`);

    // TODO: Query Redis

    res.status(404).send({status: 404, message: "No jobs are ready for execution"});
});

router.post("/result/:id", async (req, res) => {

    const queueId = req.params.id;
    logger.debug(`Adding results to ${queueId} queue.`);

    const results = req.body;
    logger.debug(JSON.stringify(req.body));

    // TODO: Add to redis queue

    res.status(201).send({status: 201, message: "Results successfully registered."})
});

router.all("*", async (req, res) => {
    res.status(404).send({status: 404, message: "This route does not exist!"})
});

router.close = async () => {
    logger.info("Closed Redis connection.");
};

module.exports = router;
