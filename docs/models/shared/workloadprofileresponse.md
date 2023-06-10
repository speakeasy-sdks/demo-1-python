# WorkloadProfileResponse

Workload Profiles provide the baseline configuration for Workloads in Applications in Humanitec. Developers can configure various features of a workload profile to suit their needs. Examples of features might be `schedules` used in Kubernetes CronJobs or `ingress` which might be used to expose Pods controlled by a Kubernetes Deployment.

Workloads in Humanitec are implemented as Helm Charts which must implement a specific schema.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation date                                                        | 2020-06-22T09:37:23.523Z                                             |
| `created_by`                                                         | *str*                                                                | :heavy_check_mark:                                                   | User created the profile                                             |                                                                      |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Workload Profile ID                                                  |                                                                      |
| `latest`                                                             | *str*                                                                | :heavy_check_mark:                                                   | The latest version of the profile                                    |                                                                      |
| `org_id`                                                             | *str*                                                                | :heavy_check_mark:                                                   | Organization ID                                                      |                                                                      |