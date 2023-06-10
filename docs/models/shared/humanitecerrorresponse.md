# HumanitecErrorResponse

HumanitecError represents a standard Humanitec Error


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `details`                                           | dict[str, *Any*]                                    | :heavy_minus_sign:                                  | (Optional) Additional information is enclosed here. |
| `error`                                             | *str*                                               | :heavy_check_mark:                                  | A short code to help with error identification.     |
| `message`                                           | *str*                                               | :heavy_check_mark:                                  | A Human readable message about the error.           |