# set

## Overview

A Deployment Set (or just "Set") defines all of the non-Environment specific configuration for Modules and External Resources. Each of these Modules or External Resources has a unique name.

Deployment Sets are immutable and their ID is a cryptographic hash of their content. This means that a Deployment Set can be globally identified based on its ID. It also means that referencing a Deployment Set by ID will always return the same Deployment Set.

Deployment Sets cannot be created directly, instead they are created by applying a Deployment Delta to an existing Deployment Set.

**Basic Structure**

```
 {
   "id": <ID of the Deployment Set>,
   "modules" : {
     <ID of Module> : {
       "profile": <Defines how the optional "spec" property is interpreted>
       "spec": {
         <Properties that depend on the "profile" property.>
       }
       "externals": {
         <External Resource Name> : {
           "type": <Resource Type>,
           "params": {
             <Properties which parametrize the resource depending on the Resource Type.>
           }
         }
       }
     }
   }
 }
```

For details about how the Humanitec provided profiles work, see (Deployment Set Profiles)[].
<SchemaDefinition schemaRef="#/components/schemas/SetRequest" />


### Available Operations

* [get_sets](#get_sets) - Get all Deployment Sets
* [get_orgs_org_id_apps_app_id_sets_set_id_](#get_orgs_org_id_apps_app_id_sets_set_id_) - Get a Deployment Set
* [get_orgs_org_id_apps_app_id_sets_set_id_diff_source_set_id_](#get_orgs_org_id_apps_app_id_sets_set_id_diff_source_set_id_) - Get the difference between 2 Deployment Sets
* [post_orgs_org_id_apps_app_id_sets_set_id_](#post_orgs_org_id_apps_app_id_sets_set_id_) - Apply a Deployment Delta to a Deployment Set

## get_sets

Get all Deployment Sets

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetSetsRequest(
    app_id='beatae',
    org_id='aliquid',
)

res = s.set.get_sets(req)

if res.set_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetSetsRequest](../../models/operations/getsetsrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetSetsResponse](../../models/operations/getsetsresponse.md)**


## get_orgs_org_id_apps_app_id_sets_set_id_

Get a Deployment Set

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDSetsSetIDRequest(
    app_id='modi',
    diff='optio',
    org_id='voluptatibus',
    set_id='molestias',
)

res = s.set.get_orgs_org_id_apps_app_id_sets_set_id_(req)

if res.get_orgs_org_id_apps_app_id_sets_set_id_200_application_json_one_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetOrgsOrgIDAppsAppIDSetsSetIDRequest](../../models/operations/getorgsorgidappsappidsetssetidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetOrgsOrgIDAppsAppIDSetsSetIDResponse](../../models/operations/getorgsorgidappsappidsetssetidresponse.md)**


## get_orgs_org_id_apps_app_id_sets_set_id_diff_source_set_id_

Get the difference between 2 Deployment Sets

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDSetsSetIDDiffSourceSetIDRequest(
    app_id='officia',
    org_id='libero',
    set_id='totam',
    source_set_id='sequi',
)

res = s.set.get_orgs_org_id_apps_app_id_sets_set_id_diff_source_set_id_(req)

if res.plain_delta_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.GetOrgsOrgIDAppsAppIDSetsSetIDDiffSourceSetIDRequest](../../models/operations/getorgsorgidappsappidsetssetiddiffsourcesetidrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.GetOrgsOrgIDAppsAppIDSetsSetIDDiffSourceSetIDResponse](../../models/operations/getorgsorgidappsappidsetssetiddiffsourcesetidresponse.md)**


## post_orgs_org_id_apps_app_id_sets_set_id_

Apply a Deployment Delta to a Deployment Set

### Example Usage

```python
import test_1
import dateutil.parser
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDSetsSetIDRequest(
    delta_request=shared.DeltaRequest(
        id='66c723ff-da9e-406b-ae48-25c1fc0e115c',
        metadata=shared.DeltaMetadataRequest(
            archived=False,
            contributers=[
                'perferendis',
                'facilis',
                'reiciendis',
            ],
            created_at=dateutil.parser.isoparse('2020-06-22T09:37:23.523Z'),
            created_by='a',
            env_id='iste',
            last_modified_at=dateutil.parser.isoparse('2020-06-22T09:37:23.523Z'),
            name='Olga Hermiston',
            shared=False,
        ),
        modules=shared.ModuleDeltasRequest(
            add={
                "maxime": {
                    "consequuntur": shared.ControllerRequest(
                        kind='assumenda',
                        message='vero',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "accusamus": 'totam',
                                        "reiciendis": 'ab',
                                        "sint": 'nihil',
                                        "esse": 'iure',
                                    },
                                    {
                                        "nesciunt": 'debitis',
                                        "vel": 'neque',
                                    },
                                    {
                                        "voluptas": 'consequuntur',
                                        "officia": 'reprehenderit',
                                    },
                                    {
                                        "eius": 'ipsa',
                                        "rem": 'maiores',
                                        "accusantium": 'veniam',
                                    },
                                ],
                                phase='saepe',
                                pod_name='neque',
                                revision=816365,
                                status='aliquam',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "fugiat": 'est',
                                        "delectus": 'velit',
                                        "vitae": 'nesciunt',
                                        "similique": 'illo',
                                    },
                                    {
                                        "nemo": 'doloribus',
                                        "possimus": 'unde',
                                        "incidunt": 'explicabo',
                                        "ipsam": 'cupiditate',
                                    },
                                    {
                                        "alias": 'quidem',
                                        "nesciunt": 'commodi',
                                        "sapiente": 'consequuntur',
                                        "veniam": 'debitis',
                                    },
                                ],
                                phase='officia',
                                pod_name='sint',
                                revision=280859,
                                status='numquam',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "libero": 'in',
                                    },
                                    {
                                        "ex": 'minus',
                                        "ab": 'beatae',
                                    },
                                    {
                                        "nisi": 'quisquam',
                                        "dolor": 'ducimus',
                                        "fuga": 'minima',
                                        "architecto": 'qui',
                                    },
                                    {
                                        "magni": 'incidunt',
                                        "adipisci": 'praesentium',
                                    },
                                ],
                                phase='dolor',
                                pod_name='exercitationem',
                                revision=709701,
                                status='facilis',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "nemo": 'culpa',
                                    },
                                    {
                                        "amet": 'deserunt',
                                    },
                                    {
                                        "veniam": 'quod',
                                        "itaque": 'a',
                                    },
                                    {
                                        "enim": 'doloribus',
                                        "assumenda": 'officiis',
                                        "architecto": 'alias',
                                        "culpa": 'ipsa',
                                    },
                                ],
                                phase='nobis',
                                pod_name='necessitatibus',
                                revision=155978,
                                status='dicta',
                            ),
                        ],
                        replicas=426002,
                        revision=595584,
                        status='debitis',
                    ),
                    "ullam": shared.ControllerRequest(
                        kind='architecto',
                        message='accusantium',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "cumque": 'iure',
                                        "quibusdam": 'quod',
                                        "nemo": 'recusandae',
                                    },
                                ],
                                phase='velit',
                                pod_name='magnam',
                                revision=493591,
                                status='laboriosam',
                            ),
                        ],
                        replicas=152283,
                        revision=486272,
                        status='natus',
                    ),
                },
                "provident": {
                    "doloribus": shared.ControllerRequest(
                        kind='facilis',
                        message='quidem',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "modi": 'perspiciatis',
                                        "hic": 'cum',
                                        "aspernatur": 'libero',
                                    },
                                    {
                                        "incidunt": 'recusandae',
                                        "quod": 'id',
                                        "saepe": 'autem',
                                    },
                                ],
                                phase='quo',
                                pod_name='nesciunt',
                                revision=849383,
                                status='nemo',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "non": 'mollitia',
                                        "assumenda": 'recusandae',
                                        "distinctio": 'pariatur',
                                    },
                                    {
                                        "facere": 'laborum',
                                        "eveniet": 'laborum',
                                    },
                                    {
                                        "maxime": 'ipsam',
                                        "alias": 'suscipit',
                                    },
                                    {
                                        "molestias": 'laborum',
                                        "est": 'occaecati',
                                        "labore": 'quo',
                                    },
                                ],
                                phase='perferendis',
                                pod_name='fugit',
                                revision=399222,
                                status='magnam',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "hic": 'nostrum',
                                        "officiis": 'unde',
                                        "nulla": 'error',
                                        "mollitia": 'magnam',
                                    },
                                    {
                                        "esse": 'corrupti',
                                        "fuga": 'facere',
                                    },
                                ],
                                phase='impedit',
                                pod_name='quasi',
                                revision=647218,
                                status='quod',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "voluptatem": 'facere',
                                    },
                                    {
                                        "maxime": 'consequatur',
                                        "eaque": 'architecto',
                                        "similique": 'porro',
                                        "blanditiis": 'quae',
                                    },
                                ],
                                phase='magni',
                                pod_name='officiis',
                                revision=148379,
                                status='necessitatibus',
                            ),
                        ],
                        replicas=773259,
                        revision=55981,
                        status='excepturi',
                    ),
                    "a": shared.ControllerRequest(
                        kind='maiores',
                        message='laudantium',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "rem": 'dicta',
                                        "suscipit": 'earum',
                                        "doloribus": 'velit',
                                        "eius": 'esse',
                                    },
                                ],
                                phase='in',
                                pod_name='eligendi',
                                revision=94697,
                                status='neque',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "accusantium": 'qui',
                                        "impedit": 'beatae',
                                        "incidunt": 'dicta',
                                    },
                                    {
                                        "corporis": 'rerum',
                                    },
                                    {
                                        "error": 'vel',
                                    },
                                    {
                                        "id": 'laboriosam',
                                    },
                                ],
                                phase='ex',
                                pod_name='quas',
                                revision=85794,
                                status='ullam',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "incidunt": 'quam',
                                        "magni": 'deserunt',
                                        "delectus": 'omnis',
                                    },
                                ],
                                phase='sed',
                                pod_name='nesciunt',
                                revision=805463,
                                status='quis',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "excepturi": 'maiores',
                                        "laudantium": 'velit',
                                    },
                                    {
                                        "amet": 'nemo',
                                        "ipsa": 'quisquam',
                                        "tenetur": 'quas',
                                        "molestiae": 'aliquid',
                                    },
                                    {
                                        "a": 'nobis',
                                        "perspiciatis": 'accusantium',
                                        "dicta": 'minus',
                                        "commodi": 'eveniet',
                                    },
                                ],
                                phase='porro',
                                pod_name='tempore',
                                revision=693747,
                                status='modi',
                            ),
                        ],
                        replicas=916341,
                        revision=145435,
                        status='eius',
                    ),
                    "sequi": shared.ControllerRequest(
                        kind='eligendi',
                        message='asperiores',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "repellat": 'a',
                                        "animi": 'maiores',
                                        "itaque": 'nulla',
                                    },
                                    {
                                        "corporis": 'velit',
                                        "officiis": 'enim',
                                        "officia": 'saepe',
                                    },
                                    {
                                        "repudiandae": 'accusantium',
                                        "officia": 'impedit',
                                    },
                                ],
                                phase='quasi',
                                pod_name='blanditiis',
                                revision=260911,
                                status='quisquam',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "natus": 'minus',
                                        "quia": 'magnam',
                                        "reprehenderit": 'quod',
                                    },
                                ],
                                phase='quos',
                                pod_name='corrupti',
                                revision=227870,
                                status='molestiae',
                            ),
                        ],
                        replicas=227156,
                        revision=675126,
                        status='modi',
                    ),
                },
                "perferendis": {
                    "architecto": shared.ControllerRequest(
                        kind='molestias',
                        message='dolore',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "odit": 'earum',
                                    },
                                    {
                                        "ipsam": 'eaque',
                                        "exercitationem": 'veniam',
                                    },
                                    {
                                        "ad": 'nisi',
                                        "tenetur": 'quis',
                                    },
                                    {
                                        "nemo": 'suscipit',
                                        "pariatur": 'sit',
                                        "quidem": 'repellendus',
                                        "perferendis": 'id',
                                    },
                                ],
                                phase='sapiente',
                                pod_name='sed',
                                revision=823572,
                                status='repellat',
                            ),
                        ],
                        replicas=921060,
                        revision=100233,
                        status='adipisci',
                    ),
                    "pariatur": shared.ControllerRequest(
                        kind='harum',
                        message='dolore',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "minus": 'soluta',
                                    },
                                    {
                                        "velit": 'earum',
                                        "praesentium": 'error',
                                        "non": 'quasi',
                                    },
                                ],
                                phase='mollitia',
                                pod_name='accusamus',
                                revision=687589,
                                status='cumque',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "corrupti": 'eaque',
                                        "deserunt": 'aliquid',
                                        "excepturi": 'magni',
                                    },
                                ],
                                phase='tempora',
                                pod_name='possimus',
                                revision=220824,
                                status='rerum',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "optio": 'delectus',
                                        "minus": 'quo',
                                        "quos": 'asperiores',
                                        "voluptatum": 'iste',
                                    },
                                ],
                                phase='corporis',
                                pod_name='accusantium',
                                revision=75850,
                                status='aut',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "at": 'possimus',
                                        "neque": 'pariatur',
                                    },
                                    {
                                        "sapiente": 'mollitia',
                                        "quae": 'quos',
                                    },
                                    {
                                        "non": 'voluptates',
                                    },
                                    {
                                        "aliquam": 'quisquam',
                                        "quas": 'consequuntur',
                                    },
                                ],
                                phase='maiores',
                                pod_name='inventore',
                                revision=400448,
                                status='laudantium',
                            ),
                        ],
                        replicas=665872,
                        revision=221329,
                        status='aliquid',
                    ),
                    "consectetur": shared.ControllerRequest(
                        kind='cumque',
                        message='rem',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "recusandae": 'tempora',
                                    },
                                    {
                                        "numquam": 'sequi',
                                        "voluptatum": 'sit',
                                        "rerum": 'veritatis',
                                    },
                                ],
                                phase='tenetur',
                                pod_name='autem',
                                revision=694088,
                                status='totam',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "magni": 'nihil',
                                        "voluptas": 'animi',
                                        "commodi": 'alias',
                                    },
                                    {
                                        "aut": 'dolore',
                                        "maxime": 'aliquam',
                                        "iste": 'ullam',
                                    },
                                    {
                                        "placeat": 'voluptas',
                                        "occaecati": 'unde',
                                        "illo": 'nihil',
                                        "inventore": 'libero',
                                    },
                                    {
                                        "quasi": 'cumque',
                                        "dicta": 'harum',
                                    },
                                ],
                                phase='facere',
                                pod_name='facilis',
                                revision=105372,
                                status='cumque',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "expedita": 'corrupti',
                                        "rem": 'atque',
                                    },
                                    {
                                        "cum": 'pariatur',
                                        "sapiente": 'quo',
                                        "incidunt": 'quod',
                                        "minus": 'porro',
                                    },
                                    {
                                        "excepturi": 'occaecati',
                                        "libero": 'quo',
                                        "esse": 'hic',
                                    },
                                    {
                                        "accusantium": 'soluta',
                                        "fugit": 'pariatur',
                                        "eligendi": 'recusandae',
                                        "veritatis": 'aut',
                                    },
                                ],
                                phase='laudantium',
                                pod_name='iusto',
                                revision=219860,
                                status='voluptates',
                            ),
                        ],
                        replicas=274295,
                        revision=169935,
                        status='rerum',
                    ),
                    "doloremque": shared.ControllerRequest(
                        kind='voluptatem',
                        message='eum',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "voluptatum": 'blanditiis',
                                        "nihil": 'atque',
                                    },
                                    {
                                        "deserunt": 'atque',
                                        "nostrum": 'atque',
                                        "architecto": 'est',
                                    },
                                ],
                                phase='enim',
                                pod_name='rem',
                                revision=168142,
                                status='quae',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "enim": 'labore',
                                        "sapiente": 'saepe',
                                        "delectus": 'officia',
                                        "natus": 'cumque',
                                    },
                                    {
                                        "quaerat": 'doloribus',
                                        "quia": 'officiis',
                                        "mollitia": 'cumque',
                                    },
                                    {
                                        "enim": 'eum',
                                        "nemo": 'illum',
                                    },
                                ],
                                phase='nesciunt',
                                pod_name='sit',
                                revision=487148,
                                status='minus',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "voluptates": 'praesentium',
                                        "dicta": 'fugit',
                                        "sit": 'aliquid',
                                        "necessitatibus": 'sed',
                                    },
                                    {
                                        "sunt": 'nesciunt',
                                        "delectus": 'laborum',
                                        "aliquam": 'deserunt',
                                    },
                                    {
                                        "sunt": 'impedit',
                                        "eius": 'voluptatum',
                                    },
                                    {
                                        "at": 'dolorem',
                                    },
                                ],
                                phase='repellat',
                                pod_name='aspernatur',
                                revision=80284,
                                status='sequi',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "hic": 'eaque',
                                        "dolorem": 'architecto',
                                        "aperiam": 'aspernatur',
                                    },
                                ],
                                phase='nulla',
                                pod_name='enim',
                                revision=73574,
                                status='magnam',
                            ),
                        ],
                        replicas=961842,
                        revision=255064,
                        status='optio',
                    ),
                },
                "nobis": {
                    "repellat": shared.ControllerRequest(
                        kind='quae',
                        message='deleniti',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "aliquid": 'sed',
                                        "beatae": 'similique',
                                        "ea": 'animi',
                                    },
                                    {
                                        "tenetur": 'dignissimos',
                                        "esse": 'animi',
                                    },
                                    {
                                        "esse": 'eveniet',
                                        "earum": 'velit',
                                        "officiis": 'eius',
                                    },
                                    {
                                        "itaque": 'dignissimos',
                                        "ipsam": 'explicabo',
                                        "impedit": 'aliquid',
                                    },
                                ],
                                phase='quis',
                                pod_name='facilis',
                                revision=218128,
                                status='ut',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "praesentium": 'eveniet',
                                    },
                                    {
                                        "expedita": 'libero',
                                    },
                                ],
                                phase='iste',
                                pod_name='illo',
                                revision=792499,
                                status='quos',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "iusto": 'enim',
                                        "accusamus": 'aperiam',
                                        "voluptates": 'laudantium',
                                    },
                                    {
                                        "quae": 'omnis',
                                        "illum": 'rem',
                                    },
                                    {
                                        "deleniti": 'modi',
                                        "earum": 'architecto',
                                        "aliquam": 'labore',
                                        "maiores": 'sequi',
                                    },
                                    {
                                        "consequatur": 'esse',
                                        "debitis": 'facere',
                                        "quisquam": 'cumque',
                                        "aliquam": 'dolorum',
                                    },
                                ],
                                phase='deserunt',
                                pod_name='ad',
                                revision=970411,
                                status='sequi',
                            ),
                        ],
                        replicas=785555,
                        revision=671528,
                        status='nobis',
                    ),
                    "quibusdam": shared.ControllerRequest(
                        kind='omnis',
                        message='aut',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "reprehenderit": 'quia',
                                        "necessitatibus": 'accusantium',
                                        "ad": 'nisi',
                                    },
                                    {
                                        "quia": 'laudantium',
                                        "sed": 'odit',
                                    },
                                    {
                                        "expedita": 'eos',
                                        "repellendus": 'nesciunt',
                                    },
                                ],
                                phase='ipsa',
                                pod_name='sint',
                                revision=291389,
                                status='esse',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "sapiente": 'quam',
                                        "est": 'aliquam',
                                        "delectus": 'culpa',
                                    },
                                ],
                                phase='voluptatum',
                                pod_name='iusto',
                                revision=802069,
                                status='voluptatibus',
                            ),
                        ],
                        replicas=374414,
                        revision=247767,
                        status='ullam',
                    ),
                },
            },
            remove=[
                'voluptas',
                'doloribus',
                'animi',
            ],
            update={
                "corporis": [
                    shared.UpdateActionRequest(
                        from_='necessitatibus',
                        op='distinctio',
                        path='maiores',
                        value='laboriosam',
                    ),
                    shared.UpdateActionRequest(
                        from_='voluptatem',
                        op='optio',
                        path='sequi',
                        value='sunt',
                    ),
                ],
                "vitae": [
                    shared.UpdateActionRequest(
                        from_='doloremque',
                        op='sed',
                        path='amet',
                        value='rerum',
                    ),
                    shared.UpdateActionRequest(
                        from_='in',
                        op='nostrum',
                        path='temporibus',
                        value='ratione',
                    ),
                    shared.UpdateActionRequest(
                        from_='dolor',
                        op='nisi',
                        path='dignissimos',
                        value='reiciendis',
                    ),
                    shared.UpdateActionRequest(
                        from_='itaque',
                        op='vitae',
                        path='est',
                        value='accusantium',
                    ),
                ],
                "quod": [
                    shared.UpdateActionRequest(
                        from_='quos',
                        op='possimus',
                        path='maiores',
                        value='odio',
                    ),
                    shared.UpdateActionRequest(
                        from_='provident',
                        op='sapiente',
                        path='aperiam',
                        value='similique',
                    ),
                    shared.UpdateActionRequest(
                        from_='nesciunt',
                        op='provident',
                        path='ex',
                        value='repellendus',
                    ),
                    shared.UpdateActionRequest(
                        from_='unde',
                        op='alias',
                        path='impedit',
                        value='sequi',
                    ),
                ],
                "commodi": [
                    shared.UpdateActionRequest(
                        from_='expedita',
                        op='in',
                        path='quisquam',
                        value='sunt',
                    ),
                    shared.UpdateActionRequest(
                        from_='enim',
                        op='nulla',
                        path='maiores',
                        value='distinctio',
                    ),
                ],
            },
        ),
        shared=[
            shared.UpdateActionRequest(
                from_='impedit',
                op='accusamus',
                path='et',
                value='quas',
            ),
            shared.UpdateActionRequest(
                from_='blanditiis',
                op='cum',
                path='dicta',
                value='impedit',
            ),
            shared.UpdateActionRequest(
                from_='tempora',
                op='eveniet',
                path='repudiandae',
                value='sed',
            ),
        ],
    ),
    app_id='impedit',
    org_id='quas',
    set_id='impedit',
)

res = s.set.post_orgs_org_id_apps_app_id_sets_set_id_(req)

if res.post_orgs_org_id_apps_app_id_sets_set_id_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PostOrgsOrgIDAppsAppIDSetsSetIDRequest](../../models/operations/postorgsorgidappsappidsetssetidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PostOrgsOrgIDAppsAppIDSetsSetIDResponse](../../models/operations/postorgsorgidappsappidsetssetidresponse.md)**

