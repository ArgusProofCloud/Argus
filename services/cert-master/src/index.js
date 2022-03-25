const express = require("express");
const process = require("process");
const createService = require("service");
const StepProvisioner = require("./step.js");

const service = createService("cert-master", "/api/v1", { redis: { enabled: false } });
const { logger, router } = service;

const step = new StepProvisioner(process.env.ROOT_CRT || "ca.crt", process.env.CA_URL || ":443",
    logger, process.env.STEP_CLI || "step");

router.use(express.text());

router.post("/renew", async (req, res) => {
    const clientCert = req.socket.getPeerCertificate();

    const serial = BigInt("0x" + clientCert.serialNumber);


    const rawCert = clientCert.raw.toString("base64");
    const crt = "-----BEGIN CERTIFICATE-----\n" + rawCert + "\n-----END CERTIFICATE-----";

    step.renew(crt, req.body).then(newCert => {
        logger.info("Renewed " + serial + ".");
        res.contentType("text/plain").send(newCert);
    }).catch(e => {
        logger.warn("Failed renewing " + serial + ".", e);

        res.status(500).send({
            status: 500,
            msg: "Failed renewing certificate, check logs for more info."
        });
    });
});

service.start();
