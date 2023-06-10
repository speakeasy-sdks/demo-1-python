# UpdateActionRequest

A representation of the main object defined in JSON Patch specified in RFC 6902 from the IETF. The main differences are:

* Only `add`, `remove` and `replace` are supported

* `remove` can have have its scope of application applied in its `value`. e.g. `{"scope":"delta"}


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `from_`            | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `op`               | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `path`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `value`            | *Optional[Any]*    | :heavy_minus_sign: | N/A                |