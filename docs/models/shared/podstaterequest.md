# PodStateRequest

PodState represents single pod status


## Fields

| Field                  | Type                   | Required               | Description            |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `container_statuses`   | list[dict[str, *Any*]] | :heavy_minus_sign:     | N/A                    |
| `phase`                | *Optional[str]*        | :heavy_minus_sign:     | N/A                    |
| `pod_name`             | *Optional[str]*        | :heavy_minus_sign:     | N/A                    |
| `revision`             | *Optional[int]*        | :heavy_minus_sign:     | N/A                    |
| `status`               | *Optional[str]*        | :heavy_minus_sign:     | N/A                    |