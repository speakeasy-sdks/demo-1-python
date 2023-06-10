# NewServiceUserRequest

NewServiceUser holds the definition of a new service user.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `email`                                                                             | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The email address that should get notifications about this service user. (Optional) |
| `name`                                                                              | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The name that should be shown for this service user.                                |
| `role`                                                                              | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The role that the service user should have on the organization it is created in     |