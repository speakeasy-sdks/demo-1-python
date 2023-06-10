# GetOrgsOrgIDAppsAppIDDeltasRequest


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `app_id`                                                        | *str*                                                           | :heavy_check_mark:                                              | The Application ID.<br/><br/>                                   |
| `archived`                                                      | *Optional[bool]*                                                | :heavy_minus_sign:                                              | If true, return archived Deltas.<br/><br/>                      |
| `env`                                                           | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Only return Deltas associated with the specified Environment.<br/><br/> |
| `org_id`                                                        | *str*                                                           | :heavy_check_mark:                                              | The Organization ID.<br/><br/>                                  |