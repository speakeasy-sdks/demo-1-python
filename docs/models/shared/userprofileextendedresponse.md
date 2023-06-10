# UserProfileExtendedResponse

UserProfileExtended holds the profile information of a user including properties only accessible to the user.


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               | Example                                                   |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `created_at`                                              | *str*                                                     | :heavy_check_mark:                                        | The time the user was first registered with Humanitec     | 2020-06-22T09:37:23.523Z                                  |
| `email`                                                   | *Optional[str]*                                           | :heavy_minus_sign:                                        | The email address of the user from the profile            |                                                           |
| `id`                                                      | *str*                                                     | :heavy_check_mark:                                        | The User ID for this user                                 |                                                           |
| `name`                                                    | *str*                                                     | :heavy_check_mark:                                        | The name the user goes by                                 |                                                           |
| `properties`                                              | dict[str, *Any*]                                          | :heavy_check_mark:                                        | N/A                                                       |                                                           |
| `roles`                                                   | dict[str, *str*]                                          | :heavy_check_mark:                                        | N/A                                                       |                                                           |
| `type`                                                    | *str*                                                     | :heavy_check_mark:                                        | The type of the account. Could be user, service or system |                                                           |