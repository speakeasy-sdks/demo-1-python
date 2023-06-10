# UserInviteResponse

UserInvite stores the invitation details.


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     | Example                                         |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `created_at`                                    | *str*                                           | :heavy_check_mark:                              | The timestamp this invitation was created.      | 2020-06-22T09:37:23.523Z                        |
| `created_by`                                    | *str*                                           | :heavy_check_mark:                              | The ID of the user who created this invitation. |                                                 |
| `email`                                         | *Optional[str]*                                 | :heavy_minus_sign:                              | The email address of the user from the profile. |                                                 |
| `expires_at`                                    | *str*                                           | :heavy_check_mark:                              | The timestamp this invitation would expire.     | 2020-06-22T09:37:23.523Z                        |
| `user_id`                                       | *str*                                           | :heavy_check_mark:                              | The User ID for this user.                      |                                                 |