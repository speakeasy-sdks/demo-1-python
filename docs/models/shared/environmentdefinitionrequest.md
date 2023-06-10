# EnvironmentDefinitionRequest

The ID, Name, Type, and Deployment the Environment will be derived from.




## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `from_deploy_id`                                                             | *str*                                                                        | :heavy_check_mark:                                                           | Defines the existing Deployment the new Environment will be based on.        |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | The ID the Environment is referenced as.                                     |
| `name`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | The Human-friendly name for the Environment.                                 |
| `type`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | The Environment Type. This is used for organizing and managing Environments. |