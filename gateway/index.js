const express = require("express");
const { logger, loggerMiddleware } = require("./logger.js");

const app = express();
app.use(loggerMiddleware);

app.get("", (req, res) => res.send("Hello World"));

app.listen(3000, () => {
    logger.info("The web server has started.");
});
