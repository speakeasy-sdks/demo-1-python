# ModuleDeltasResponse

ModuleDeltas groups the different operations together.


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `add`                                                                                 | dict[str, dict[str, [ControllerResponse](../../models/shared/controllerresponse.md)]] | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `remove`                                                                              | list[*str*]                                                                           | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `update`                                                                              | dict[str, list[[UpdateActionResponse](../../models/shared/updateactionresponse.md)]]  | :heavy_check_mark:                                                                    | N/A                                                                                   |