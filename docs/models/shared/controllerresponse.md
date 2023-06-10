# ControllerResponse

Controller represents deployment, stateful set etc


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `kind`                                                            | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `message`                                                         | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `pods`                                                            | list[[PodStateResponse](../../models/shared/podstateresponse.md)] | :heavy_check_mark:                                                | N/A                                                               |
| `replicas`                                                        | *int*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `revision`                                                        | *int*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `status`                                                          | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |