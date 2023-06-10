# ControllerRequest

Controller represents deployment, stateful set etc


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `kind`                                                          | *Optional[str]*                                                 | :heavy_minus_sign:                                              | N/A                                                             |
| `message`                                                       | *Optional[str]*                                                 | :heavy_minus_sign:                                              | N/A                                                             |
| `pods`                                                          | list[[PodStateRequest](../../models/shared/podstaterequest.md)] | :heavy_minus_sign:                                              | N/A                                                             |
| `replicas`                                                      | *Optional[int]*                                                 | :heavy_minus_sign:                                              | N/A                                                             |
| `revision`                                                      | *Optional[int]*                                                 | :heavy_minus_sign:                                              | N/A                                                             |
| `status`                                                        | *Optional[str]*                                                 | :heavy_minus_sign:                                              | N/A                                                             |