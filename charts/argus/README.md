# Argus - Helm Chart

![Version: 0.1.2](https://img.shields.io/badge/Version-0.1.2-informational?style=flat-square&logo=helm)

An automated security checking platform that is highly extensible.

**Homepage:** <https://github.com/WatcherWhale/SecProA>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.bitnami.com/bitnami | redis | 16.8.5 |
| https://smallstep.github.io/helm-charts/ | autocert | 1.16.3 |

## Values

### App

App settings
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| app.host | string | `"argus.local"` | The hostname used in the ingress. |
| app.name | string | `"argus"` | The name of the deployment. |

### Autoscaling

Autoscaling configuration.
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| autoscaling.enabled | bool | `true` | Enable/Disable autoscaling. |
| autoscaling.tag | string | `"v1.0.0"` | The image tag for the custom autoscaler. |

### Checklists

A list of all available checklists that need to be deployed. These can be customized to add your own checks. Default available checklists: `cookie`, `dns`, `headers`, `https`, `ip` and `mail`.
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| checklists.dns.affinity | object | `{}` | Affinity for pod assignment. |
| checklists.dns.annotations | object | `{}` | Deployment annotations. |
| checklists.dns.env | object | `{}` | Custom environment variabled to add to the checklist. |
| checklists.dns.interval | int | `10000` | The throughput interval, the interval to periodically check the current queue size. (ms) |
| checklists.dns.nodeSelector | object | `{}` | Node Labels for pod assignment. |
| checklists.dns.podAnnotations | object | `{}` | Pod annotations. |
| checklists.dns.replicas.max | int | `5` | Maximum replicas |
| checklists.dns.replicas.min | int | `1` | Minimum replicas |
| checklists.dns.stabilization | int | `200` | The stabilization interval, used for down scaling. (s) |
| checklists.dns.tag | string | `"v1.0.0"` | The image tag of the checklist container. |
| checklists.dns.throughput | int | `100` | Check throughput The amount of request the checklist can handle in an interval. |
| checklists.dns.tolerations | list | `[]` | Tolerations for pod assignment. |

### Image

Container image settings.
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| image.imagePullSecrets | list | `[{"name":"ghcr-io"}]` | A list of image pull secrets to use. |
| image.pullPolicy | string | `"IfNotPresent"` | Default pullPolicy. |
| image.registry | string | `"ghcr.io/watcherwhale"` | The image registry to use. |

### Redis

Bitnami Redis configuration. See https://github.com/bitnami/charts/tree/master/bitnami/redis for more config options.
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| redis.auth | object | `{"enabled":true,"sentinel":true}` | Auth settings |
| redis.master | object | `{"persistence":{"enabled":false}}` | Master settings |
| redis.sentinel.enabled | bool | `true` | Enable or Disable sentinels Must be enabled |

### Security

Security Settings
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| security.cluster.tls | bool | `false` | Enable mTLS & TLS throughout the cluster. |
| security.ingress.caSecret | string | `"argus-ca"` | The Certificate Authority Certificate secret. |
| security.ingress.clientAuth | bool | `true` | Enable mTLS at the ingress. |
| security.ingress.tlsSecret | string | `"argus-tls"` | The tls secret for https. |

### Selenium

The Selenium deployment configuration.
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| selenium.affinity | object | `{}` | Affinity for pod assignment. |
| selenium.enabled | bool | `true` | Enable the Selenium deployment. |
| selenium.nodeSelector | object | `{}` | Node Labels for pod assignment. |
| selenium.replicas | int | `3` | Amount of Chrome node replicas. |
| selenium.tag | string | `"latest"` | The selenium hub/Chrome image tag. |
| selenium.tolerations | list | `[]` | Tolerations for pod assignment. |

### Services

All services

#### Certmaster

Cert-master service configuration. Only necessary when `security.cluster.tls` is enabled.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Affinity for pod assignment. |
| annotations | object | `{}` | Deployment annotations. |
| loglevel | string | `"info"` | Log level. |
| nodeSelector | object | `{}` | Node Labels for pod assignment. |
| podAnnotations | object | `{}` | Pod annotations. |
| replicas.max | int | `10` | Maximum replicas. |
| replicas.min | int | `1` | Minimum replicas. |
| securityContext | object | `{}` | Pod security context. |
| tag | string | `"v1.0.0"` | Image tag |
| tolerations | list | `[]` | Tolerations for pod assignment. |

#### Descriptions

Descriptions service configuration.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Affinity for pod assignment. |
| annotations | object | `{}` | Deployment annotations. |
| nodeSelector | object | `{}` | Node Labels for pod assignment. |
| podAnnotations | object | `{}` | Pod annotations. |
| replicas.max | int | `10` | Maximum replicas. |
| replicas.min | int | `1` | Minimum replicas. |
| securityContext | object | `{}` | Pod security context. |
| tag | string | `"v1.0.0"` | Image tag |
| tolerations | list | `[]` | Tolerations for pod assignment. |

#### Gateway

Gateway service configuration.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Affinity for pod assignment. |
| annotations | object | `{}` | Deployment annotations. |
| loglevel | string | `"info"` | Log level. |
| nodeSelector | object | `{}` | Node Labels for pod assignment. |
| podAnnotations | object | `{}` | Pod annotations. |
| replicas.max | int | `10` | Maximum replicas. |
| replicas.min | int | `1` | Minimum replicas. |
| securityContext | object | `{}` | Pod security context. |
| tag | string | `"v1.0.0"` | Image tag |
| tolerations | list | `[]` | Tolerations for pod assignment. |

#### Metrics

Metrics service configuration.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Affinity for pod assignment. |
| annotations | object | `{}` | Deployment annotations. |
| loglevel | string | `"info"` | Log level. |
| nodeSelector | object | `{}` | Node Labels for pod assignment. |
| podAnnotations | object | `{}` | Pod annotations. |
| replicas.max | int | `10` | Maximum replicas. |
| replicas.min | int | `1` | Minimum replicas. |
| securityContext | object | `{}` | Pod security context. |
| tag | string | `"v1.0.0"` | Image tag |
| tolerations | list | `[]` | Tolerations for pod assignment. |

#### Sequencer

Sequencer service configuration.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Affinity for pod assignment. |
| annotations | object | `{}` | Deployment annotations. |
| loglevel | string | `"info"` | Log level. |
| nodeSelector | object | `{}` | Node Labels for pod assignment. |
| podAnnotations | object | `{}` | Pod annotations. |
| replicas.max | int | `10` | Maximum replicas. |
| replicas.min | int | `1` | Minimum replicas. |
| securityContext | object | `{}` | Pod security context. |
| tag | string | `"v1.0.0"` | Image tag |
| tolerations | list | `[]` | Tolerations for pod assignment. |

## Source Code

* <https://github.com/WatcherWhale/SecProA>

## Chart Maintainers

| Name | GitHub |
| ---- | ------ |
| Mathias Maes | [https://github.com/WatcherWhale](https://github.com/WatcherWhale)
| Cato van Hooijdonk | [https://github.com/vanHooijdonkC](https://github.com/vanHooijdonkC)
