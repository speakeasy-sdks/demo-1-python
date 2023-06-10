# UserRoleResponse

UserRole holds the mapping of role to user for a particular object.


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               | Example                                                   |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `created_at`                                              | *str*                                                     | :heavy_check_mark:                                        | The time the user was first registered with Humanitec     | 2020-06-22T09:37:23.523Z                                  |
| `email`                                                   | *Optional[str]*                                           | :heavy_minus_sign:                                        | The email address of the user from the profile            |                                                           |
| `id`                                                      | *str*                                                     | :heavy_check_mark:                                        | The User ID for this user                                 |                                                           |
| `invite`                                                  | *Optional[str]*                                           | :heavy_minus_sign:                                        | The status of an invitation (If applicable)               |                                                           |
| `name`                                                    | *str*                                                     | :heavy_check_mark:                                        | The name the user goes by                                 |                                                           |
| `role`                                                    | *str*                                                     | :heavy_check_mark:                                        | The role that this user holds                             |                                                           |
| `type`                                                    | *str*                                                     | :heavy_check_mark:                                        | The type of the account. Could be user, service or system |                                                           |
| `user`                                                    | *Optional[str]*                                           | :heavy_minus_sign:                                        | The user ID that hold the role                            |                                                           |