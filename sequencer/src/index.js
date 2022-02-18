const process = require("process");
const express = require("express");
const LogFile = require("logfile");

const logFile = LogFile.createLogFile("sequencer.log", process.env.LOGLEVEL || "info");
const logger = logFile.getLogger();

const app = express();
const apiRouter = require("./router");

app.use(logFile.createMiddleware("info", "access.log"));
app.use(express.json());
app.use("/api/v1", apiRouter);

const server = app.listen(process.env.PORT || 3000, () => {
    logger.info(`Server started on port ${process.env.PORT || 3000}.`);
});


process.on("SIGINT", shutdown).on("SIGTERM", shutdown);

async function shutdown()
{
    logger.info("Shutting down service.");

    await apiRouter.close();
    server.close(() => {
        logger.info("Closed Web Server.")
        logger.info("Shutdown successful.")
    });
}

