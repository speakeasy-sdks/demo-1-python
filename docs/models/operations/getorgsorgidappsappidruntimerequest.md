# GetOrgsOrgIDAppsAppIDRuntimeRequest


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `app_id`                                                                         | *str*                                                                            | :heavy_check_mark:                                                               | The Application ID.<br/><br/>                                                    |
| `id`                                                                             | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Filter environments by ID (required). Up to 5 ids can be supplied per request.<br/><br/> |
| `org_id`                                                                         | *str*                                                                            | :heavy_check_mark:                                                               | The Organization ID.<br/><br/>                                                   |