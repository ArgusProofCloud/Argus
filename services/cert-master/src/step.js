const fs = require("fs");
const util = require("util");
const exec = util.promisify(require("child_process").exec);
const temp = require("temp");

temp.track();

class StepProvisioner
{
    constructor(root, caUrl, stepCli = "step")
    {
        this.root = root;
        this.caUrl = caUrl;
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

    async revoke(cert)
    {
        const serial = await this.getSerialNumber(cert);
        await this.revokeSerial(serial);
    }

    async revokeSerial(serial)
    {
        await exec(`${this.stepCli} ca revoke --root="${this.root}" --ca-url="${this.caUrl}" ${serial}`)
    }

    async renew(crt, key)
    {
        const crtFile = await this.getTempFile(crt);
        const keyFile = await this.getTempFile(key);
        const newFile = await this.getTempFile();

        try
        {
            await exec(`${this.stepCli} ca renew -f --root="${this.root}" --ca-url="${this.caUrl}" "${crtFile}" "${keyFile}" --out "${newFile}"`);
            return fs.readFileSync(newFile);
        }
        catch(e)
        {
            console.log(e);
            return null;
        }
    }

    async getSerialNumber(cert)
    {
        const crtFile = await this.getTempFile(cert);

        const { stdout } = await exec(`${this.stepCli} certificate inspect "${crtFile}" --format json`);
        const certInfo = JSON.parse(stdout);

        return certInfo.serial_number;
    }
}

module.exports = StepProvisioner;
