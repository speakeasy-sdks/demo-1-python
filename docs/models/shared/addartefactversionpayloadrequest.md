# AddArtefactVersionPayloadRequest

AddArtefactVersionPayload describes the payload for a new ArtefactVersion request.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `commit`                                                    | *Optional[str]*                                             | :heavy_minus_sign:                                          | (Optional) The commit ID the Artefact Version was built on. |
| `digest`                                                    | *Optional[str]*                                             | :heavy_minus_sign:                                          | (Optional) The Artefact Version digest.                     |
| `name`                                                      | *str*                                                       | :heavy_check_mark:                                          | The Artefact name.                                          |
| `ref`                                                       | *Optional[str]*                                             | :heavy_minus_sign:                                          | (Optional) The ref the Artefact Version was built from.     |
| `type`                                                      | *str*                                                       | :heavy_check_mark:                                          | The Artefact Version type.                                  |
| `version`                                                   | *Optional[str]*                                             | :heavy_minus_sign:                                          | (Optional) The Artefact Version.                            |