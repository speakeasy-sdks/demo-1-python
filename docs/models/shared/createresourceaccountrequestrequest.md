# CreateResourceAccountRequestRequest

CreateResourceAccountRequest describes the request to create a new security account.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `credentials`                                                                   | dict[str, *Any*]                                                                | :heavy_minus_sign:                                                              | Credentials associated with the account.                                        |
| `id`                                                                            | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Unique identifier for the account (in scope of the organization it belongs to). |
| `name`                                                                          | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Display name.                                                                   |
| `type`                                                                          | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The type of the account                                                         |