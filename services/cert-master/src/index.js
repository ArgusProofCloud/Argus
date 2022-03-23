const express = require("express");
const process = require("process");
const createService = require("service");
const StepProvisioner = require("./step.js");

const service = createService("cert-master", "/api/v1", { redis: { enabled: false } });
const { logger, router } = service;

const step = new StepProvisioner(process.env.ROOT_CRT || "ca.crt",
    process.env.CA_URL || ":443", process.env.STEP_CLI || "step");

router.use(express.text());

router.post("/renew", async (req, res) => {
    const clientCert = req.socket.getPeerCertificate();

    let rawCert = clientCert.raw.toString("base64")
    const crt = "-----BEGIN CERTIFICATE-----\n" + rawCert + "\n-----END CERTIFICATE-----";

    const newCert = await step.renew(crt, req.body);

    res.contentType("text/plain").send(newCert);
});

service.start();
