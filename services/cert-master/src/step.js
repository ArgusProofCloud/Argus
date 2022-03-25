const fs = require("fs");
const util = require("util");
const exec = util.promisify(require("child_process").exec);
const temp = require("temp");

temp.track();

class StepProvisioner
{
    constructor(root, caUrl, logger, stepCli = "step")
    {
        this.root = root;
        this.caUrl = caUrl;
        this.logger = logger;
        this.stepCli = stepCli;
    }

    async getTempFile(contents = null)
    {
        return new Promise((resolve, reject) => {
            temp.open("step", (err, result) => {
                if(err)
                {
                    reject(err);

                    return;
                }

                if(contents)
                {
                    fs.writeFileSync(result.path, contents);
                }

                resolve(result.path);
            });
        });
    }

    renew(crt, key)
    {
        return new Promise(async (resolve, reject) => {
            const crtFile = await this.getTempFile(crt);
            const keyFile = await this.getTempFile(key);
            const newFile = await this.getTempFile();

            exec(`${this.stepCli} ca renew -f --root="${this.root}" ` +
                `--ca-url="${this.caUrl}" "${crtFile}" "${keyFile}" --out "${newFile}"`)
                .catch(e => {

                    this.logger.error("Failed renewing certificate", e);
                    reject();
                }).then(() => {
                    resolve(fs.readFileSync(newFile));
                });
        });
    }
}

module.exports = StepProvisioner;
