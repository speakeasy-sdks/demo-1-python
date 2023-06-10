# ModuleDeltasRequest

ModuleDeltas groups the different operations together.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `add`                                                                               | dict[str, dict[str, [ControllerRequest](../../models/shared/controllerrequest.md)]] | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `remove`                                                                            | list[*str*]                                                                         | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `update`                                                                            | dict[str, list[[UpdateActionRequest](../../models/shared/updateactionrequest.md)]]  | :heavy_minus_sign:                                                                  | N/A                                                                                 |