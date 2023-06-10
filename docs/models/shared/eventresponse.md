# EventResponse

Events available for triggering automated jobs.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `properties`                                                           | list[*str*]                                                            | :heavy_check_mark:                                                     | List of event properties which can be used as variables for this event |
| `scope`                                                                | *str*                                                                  | :heavy_check_mark:                                                     | Event scope                                                            |
| `type`                                                                 | *str*                                                                  | :heavy_check_mark:                                                     | Event type                                                             |