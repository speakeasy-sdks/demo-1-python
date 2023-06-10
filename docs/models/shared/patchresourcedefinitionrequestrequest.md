# PatchResourceDefinitionRequestRequest

PatchResourceDefinitionRequest describes a ResourceDefinition change request.


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `driver_account`                                                              | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | (Optional) Security account required by the driver.                           |
| `driver_inputs`                                                               | [Optional[ValuesSecretsRequest]](../../models/shared/valuessecretsrequest.md) | :heavy_minus_sign:                                                            | ValuesSecrets stores data that should be passed around split by sensitivity.  |
| `name`                                                                        | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | (Optional) Resource display name                                              |