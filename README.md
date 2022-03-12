<img src="https://www.shareicon.net/data/512x512/2016/07/08/116959_key_512x512.png" alt="Logo of the project" align="right" height=45px>

# HowSamI  [![npm](https://img.shields.io/npm/v/npm.svg?style=flat-square)](https://www.npmjs.com/package/npm)

> How Safe am I? Really?

HowSamI was a responsibility given to the students of "Security Project", a course at AP Hogeschool.  
The idea is to create a highly available, agile platform to execute checks that control a given domain.  
We realised this by using different microservices that can be easily deployed with ansible scripts and dockerfiles.  
A high selling point of our platform is the use of a Kubernetes cluster, which ensures the autoscaling of all services.  
This project is created with a security mindset, but can be used for other (non-security) purposes. The principle of "plug 'n play" is a definite here, just remove / add / replace the checks with your own scripts and you're good to go.
For more details about what lives in the environment, we refer you to our [wiki page](https://github.com/WatcherWhale/SecProA/wiki).  

## Getting started
Before getting started, make sure you have installed [Docker](https://www.docker.com) on you machine.  
When ready to get started, execute following commands:
```shell
setting up env

```

## Developing
### Built with
Libraries used in this project:
| Library             | Version      |
| ------------------- | ------------ |
| IoRedis             | 4.28.5       |
| Express             | 4.17.3       |
| Redlock             | 5.0.0-beta.1 |
| Winston             | 3.6.0        |
| Morgan              | 1.10.0       |

### Checks
A list of all checks included in this project:
| Name         | Description      |
| ------------ | ---------------- |
| IP           |                  |
| DNS          |                  |
| Mail         |                  |
| Https        |                  |
|              |                  |

### Codestyle
We reinforced some codestyle rules with linter which will automatically run in Git upon pushing.  

Javascript rules found in: .eslintrc.js  
Python rules found in: .pylintrc  
Yaml rules found in: .yamllint  

## Licensing
licencing?