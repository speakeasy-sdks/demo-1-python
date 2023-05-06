# delta

## Overview

A Deployment Delta (or just "Delta") describes the changes that must be applied to one Deployment Set to generate another Deployment Set. Deployment Deltas are the only way to create new Deployment Sets.

Deployment Deltas can be created fully formed or combined together via PATCHing. They can also be generated from the difference between two Deployment Sets.

**Basic Structure**

```
 {
   "id": <ID of the Deployment Delta.>,
   "metadata": {
     <Properties such as who created the Delta, which Environment it is associated to and a Human-friendly name>
   }
   "modules" : {
     "add" : {
       <ID of Module to add to the Deployment Set> : {
         <An entire Modules object>
       }
     },
     "remove": [
       <An array of Module IDs that should be removed from the Deployment Set>
     ],
    "update": {
       <ID of Module already in the Set to be updated> : [
         <An array of JSON Patch (Search Results (RFC 6902) objects scoped to the module>
       ]
     }
   }
 }
```
<SchemaDefinition schemaRef="#/components/schemas/DeltaRequest" />


### Available Operations

* [get_delta](#get_delta) - Fetch an existing Delta
* [get_orgs_org_id_apps_app_id_deltas](#get_orgs_org_id_apps_app_id_deltas) - List Deltas in an Application
* [patch_orgs_org_id_apps_app_id_deltas_delta_id_](#patch_orgs_org_id_apps_app_id_deltas_delta_id_) - Update an existing Delta
* [post_orgs_org_id_apps_app_id_deltas](#post_orgs_org_id_apps_app_id_deltas) - Create a new Delta
* [put_delta](#put_delta) - Update an existing Delta
* [put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_archived](#put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_archived) - Mark a Delta as "archived"
* [put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_env_id](#put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_env_id) - Change the Environment of a Delta
* [put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_name](#put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_name) - Change the name of a Delta

## get_delta

Fetch an existing Delta

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetDeltaRequest(
    app_id='praesentium',
    delta_id='rem',
    org_id='voluptates',
)

res = s.delta.get_delta(req)

if res.delta_response is not None:
    # handle response
```

## get_orgs_org_id_apps_app_id_deltas

List Deltas in an Application

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDDeltasRequest(
    app_id='quasi',
    archived=False,
    env='repudiandae',
    org_id='sint',
)

res = s.delta.get_orgs_org_id_apps_app_id_deltas(req)

if res.delta_responses is not None:
    # handle response
```

## patch_orgs_org_id_apps_app_id_deltas_delta_id_

Update an existing Delta

### Example Usage

```python
import test_1
import dateutil.parser
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PatchOrgsOrgIDAppsAppIDDeltasDeltaIDRequest(
    request_body=[
        shared.DeltaRequest(
            id='e450ad2a-bd44-4269-802d-502a94bb4f63',
            metadata=shared.DeltaMetadataRequest(
                archived=False,
                contributers=[
                    'sint',
                    'aliquid',
                    'provident',
                    'necessitatibus',
                ],
                created_at=dateutil.parser.isoparse('2020-06-22T09:37:23.523Z'),
                created_by='sint',
                env_id='officia',
                last_modified_at=dateutil.parser.isoparse('2020-06-22T09:37:23.523Z'),
                name='Raquel Wilderman',
                shared=False,
            ),
            modules=shared.ModuleDeltasRequest(
                add={
                    "illum": {
                        "rerum": shared.ControllerRequest(
                            kind='dicta',
                            message='magnam',
                            pods=[
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "aliquid": 'laborum',
                                            "accusamus": 'non',
                                        },
                                        {
                                            "enim": 'accusamus',
                                            "delectus": 'quidem',
                                            "provident": 'nam',
                                        },
                                        {
                                            "blanditiis": 'deleniti',
                                            "sapiente": 'amet',
                                            "deserunt": 'nisi',
                                        },
                                        {
                                            "natus": 'omnis',
                                            "molestiae": 'perferendis',
                                        },
                                    ],
                                    phase='nihil',
                                    pod_name='magnam',
                                    revision=716075,
                                    status='id',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "suscipit": 'natus',
                                            "nobis": 'eum',
                                        },
                                        {
                                            "aspernatur": 'architecto',
                                            "magnam": 'et',
                                            "excepturi": 'ullam',
                                            "provident": 'quos',
                                        },
                                    ],
                                    phase='sint',
                                    pod_name='accusantium',
                                    revision=653201,
                                    status='reiciendis',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "eum": 'dolor',
                                            "necessitatibus": 'odit',
                                        },
                                        {
                                            "quasi": 'iure',
                                            "doloribus": 'debitis',
                                        },
                                        {
                                            "maxime": 'deleniti',
                                            "facilis": 'in',
                                        },
                                    ],
                                    phase='architecto',
                                    pod_name='architecto',
                                    revision=919483,
                                    status='ullam',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "repellat": 'quibusdam',
                                            "sed": 'saepe',
                                        },
                                        {
                                            "accusantium": 'consequuntur',
                                            "praesentium": 'natus',
                                            "magni": 'sunt',
                                            "quo": 'illum',
                                        },
                                        {
                                            "maxime": 'ea',
                                            "excepturi": 'odit',
                                            "ea": 'accusantium',
                                            "ab": 'maiores',
                                        },
                                    ],
                                    phase='quidem',
                                    pod_name='ipsam',
                                    revision=453543,
                                    status='autem',
                                ),
                            ],
                            replicas=722056,
                            revision=50588,
                            status='pariatur',
                        ),
                        "nemo": shared.ControllerRequest(
                            kind='voluptatibus',
                            message='perferendis',
                            pods=[
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "cumque": 'corporis',
                                        },
                                    ],
                                    phase='hic',
                                    pod_name='libero',
                                    revision=749999,
                                    status='dolores',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "dignissimos": 'eaque',
                                            "quis": 'nesciunt',
                                            "eos": 'perferendis',
                                        },
                                        {
                                            "minus": 'quam',
                                        },
                                    ],
                                    phase='dolor',
                                    pod_name='vero',
                                    revision=345352,
                                    status='hic',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "facilis": 'perspiciatis',
                                            "voluptatem": 'porro',
                                            "consequuntur": 'blanditiis',
                                        },
                                        {
                                            "eaque": 'occaecati',
                                            "rerum": 'adipisci',
                                            "asperiores": 'earum',
                                        },
                                        {
                                            "iste": 'dolorum',
                                            "deleniti": 'pariatur',
                                        },
                                        {
                                            "nobis": 'libero',
                                            "delectus": 'quaerat',
                                            "quos": 'aliquid',
                                        },
                                    ],
                                    phase='dolorem',
                                    pod_name='dolorem',
                                    revision=222443,
                                    status='qui',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "excepturi": 'cum',
                                            "voluptate": 'dignissimos',
                                            "reiciendis": 'amet',
                                            "dolorum": 'numquam',
                                        },
                                    ],
                                    phase='veritatis',
                                    pod_name='ipsa',
                                    revision=56418,
                                    status='iure',
                                ),
                            ],
                            replicas=487838,
                            revision=311796,
                            status='accusamus',
                        ),
                        "quidem": shared.ControllerRequest(
                            kind='voluptatibus',
                            message='voluptas',
                            pods=[
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "sit": 'fugiat',
                                            "ab": 'soluta',
                                            "dolorum": 'iusto',
                                        },
                                    ],
                                    phase='voluptate',
                                    pod_name='dolorum',
                                    revision=536579,
                                    status='omnis',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "asperiores": 'nihil',
                                            "ipsum": 'voluptate',
                                            "id": 'saepe',
                                        },
                                        {
                                            "aspernatur": 'perferendis',
                                            "amet": 'optio',
                                        },
                                        {
                                            "ad": 'saepe',
                                            "suscipit": 'deserunt',
                                            "provident": 'minima',
                                            "repellendus": 'totam',
                                        },
                                        {
                                            "alias": 'at',
                                            "quaerat": 'tempora',
                                            "vel": 'quod',
                                        },
                                    ],
                                    phase='officiis',
                                    pod_name='qui',
                                    revision=679880,
                                    status='a',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "iusto": 'ipsum',
                                            "quisquam": 'tenetur',
                                            "amet": 'tempore',
                                        },
                                        {
                                            "numquam": 'enim',
                                            "dolorem": 'sapiente',
                                            "totam": 'nihil',
                                            "sit": 'expedita',
                                        },
                                    ],
                                    phase='neque',
                                    pod_name='sed',
                                    revision=424685,
                                    status='libero',
                                ),
                            ],
                            replicas=374170,
                            revision=646265,
                            status='quam',
                        ),
                        "ipsum": shared.ControllerRequest(
                            kind='incidunt',
                            message='qui',
                            pods=[
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "soluta": 'dicta',
                                            "laborum": 'totam',
                                            "incidunt": 'aspernatur',
                                            "dolores": 'distinctio',
                                        },
                                        {
                                            "aliquid": 'quam',
                                            "molestias": 'temporibus',
                                            "qui": 'neque',
                                        },
                                        {
                                            "magni": 'odio',
                                        },
                                        {
                                            "ullam": 'nam',
                                        },
                                    ],
                                    phase='hic',
                                    pod_name='voluptatem',
                                    revision=765326,
                                    status='soluta',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "saepe": 'ipsum',
                                        },
                                        {
                                            "nobis": 'quos',
                                        },
                                        {
                                            "cupiditate": 'aperiam',
                                            "delectus": 'dolorem',
                                            "dolore": 'labore',
                                        },
                                    ],
                                    phase='adipisci',
                                    pod_name='dolorum',
                                    revision=100294,
                                    status='quae',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "itaque": 'consequatur',
                                            "est": 'repellendus',
                                            "porro": 'doloribus',
                                        },
                                    ],
                                    phase='ut',
                                    pod_name='facilis',
                                    revision=586410,
                                    status='qui',
                                ),
                            ],
                            replicas=63955,
                            revision=512393,
                            status='odio',
                        ),
                    },
                    "occaecati": {
                        "quisquam": shared.ControllerRequest(
                            kind='vero',
                            message='omnis',
                            pods=[
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "voluptate": 'consectetur',
                                            "vero": 'tenetur',
                                            "dignissimos": 'hic',
                                            "distinctio": 'quod',
                                        },
                                    ],
                                    phase='odio',
                                    pod_name='similique',
                                    revision=708548,
                                    status='vero',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "quibusdam": 'illum',
                                            "sequi": 'natus',
                                        },
                                        {
                                            "aut": 'voluptatibus',
                                            "exercitationem": 'nulla',
                                            "fugit": 'porro',
                                            "maiores": 'doloribus',
                                        },
                                    ],
                                    phase='iusto',
                                    pod_name='eligendi',
                                    revision=497391,
                                    status='alias',
                                ),
                            ],
                            replicas=639473,
                            revision=269479,
                            status='ipsam',
                        ),
                        "ea": shared.ControllerRequest(
                            kind='aspernatur',
                            message='vel',
                            pods=[
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "ex": 'laudantium',
                                        },
                                        {
                                            "dolor": 'maiores',
                                        },
                                    ],
                                    phase='quasi',
                                    pod_name='ex',
                                    revision=862192,
                                    status='excepturi',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "sapiente": 'quisquam',
                                            "saepe": 'ea',
                                        },
                                        {
                                            "corporis": 'veniam',
                                            "aliquid": 'inventore',
                                            "magnam": 'ea',
                                            "quo": 'consectetur',
                                        },
                                        {
                                            "aspernatur": 'minima',
                                            "eaque": 'a',
                                            "libero": 'aut',
                                            "aut": 'deleniti',
                                        },
                                        {
                                            "aliquam": 'fugit',
                                            "accusamus": 'inventore',
                                            "non": 'et',
                                            "dolorum": 'laborum',
                                        },
                                    ],
                                    phase='placeat',
                                    pod_name='velit',
                                    revision=432148,
                                    status='autem',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "assumenda": 'nulla',
                                            "voluptas": 'libero',
                                            "quasi": 'tempora',
                                        },
                                        {
                                            "explicabo": 'provident',
                                            "ipsa": 'molestiae',
                                        },
                                        {
                                            "odio": 'eius',
                                            "esse": 'esse',
                                        },
                                        {
                                            "fuga": 'reprehenderit',
                                            "quidem": 'fugiat',
                                            "ut": 'eum',
                                        },
                                    ],
                                    phase='suscipit',
                                    pod_name='assumenda',
                                    revision=181151,
                                    status='praesentium',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "ipsa": 'id',
                                        },
                                        {
                                            "neque": 'quo',
                                            "illum": 'quo',
                                            "fuga": 'eius',
                                        },
                                        {
                                            "voluptas": 'ab',
                                        },
                                        {
                                            "consequatur": 'tempora',
                                            "debitis": 'ipsam',
                                            "aspernatur": 'sequi',
                                        },
                                    ],
                                    phase='quo',
                                    pod_name='esse',
                                    revision=925164,
                                    status='aperiam',
                                ),
                            ],
                            replicas=715179,
                            revision=799796,
                            status='dignissimos',
                        ),
                        "inventore": shared.ControllerRequest(
                            kind='nihil',
                            message='totam',
                            pods=[
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "occaecati": 'commodi',
                                            "sapiente": 'dolores',
                                        },
                                        {
                                            "molestiae": 'accusantium',
                                            "porro": 'eum',
                                            "quas": 'praesentium',
                                        },
                                    ],
                                    phase='consequuntur',
                                    pod_name='deleniti',
                                    revision=143829,
                                    status='fuga',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "atque": 'explicabo',
                                            "minima": 'nisi',
                                        },
                                        {
                                            "sapiente": 'consequuntur',
                                        },
                                        {
                                            "explicabo": 'saepe',
                                        },
                                    ],
                                    phase='occaecati',
                                    pod_name='atque',
                                    revision=92260,
                                    status='esse',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "veritatis": 'esse',
                                            "quod": 'nam',
                                            "vero": 'aliquid',
                                            "quasi": 'saepe',
                                        },
                                        {
                                            "harum": 'molestiae',
                                            "rerum": 'occaecati',
                                        },
                                        {
                                            "distinctio": 'eligendi',
                                            "sit": 'culpa',
                                        },
                                        {
                                            "adipisci": 'cumque',
                                            "consequuntur": 'consequatur',
                                            "minus": 'quaerat',
                                        },
                                    ],
                                    phase='sapiente',
                                    pod_name='consectetur',
                                    revision=458139,
                                    status='blanditiis',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "nulla": 'quas',
                                            "esse": 'quasi',
                                            "a": 'error',
                                            "sint": 'pariatur',
                                        },
                                        {
                                            "quia": 'eveniet',
                                            "asperiores": 'facere',
                                            "veritatis": 'consequuntur',
                                            "quasi": 'similique',
                                        },
                                        {
                                            "aliquid": 'tenetur',
                                            "quae": 'earum',
                                            "vel": 'in',
                                        },
                                    ],
                                    phase='eius',
                                    pod_name='libero',
                                    revision=849039,
                                    status='soluta',
                                ),
                            ],
                            replicas=33304,
                            revision=306986,
                            status='sapiente',
                        ),
                        "dicta": shared.ControllerRequest(
                            kind='ullam',
                            message='reprehenderit',
                            pods=[
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "voluptatum": 'qui',
                                        },
                                        {
                                            "ex": 'deleniti',
                                            "itaque": 'dolorum',
                                            "architecto": 'omnis',
                                            "tenetur": 'quasi',
                                        },
                                    ],
                                    phase='at',
                                    pod_name='et',
                                    revision=454162,
                                    status='ipsa',
                                ),
                                shared.PodStateRequest(
                                    container_statuses=[
                                        {
                                            "consectetur": 'adipisci',
                                        },
                                        {
                                            "temporibus": 'accusantium',
                                            "rem": 'aut',
                                            "laudantium": 'eum',
                                        },
                                    ],
                                    phase='mollitia',
                                    pod_name='ab',
                                    revision=544591,
                                    status='non',
                                ),
                            ],
                            replicas=32465,
                            revision=221161,
                            status='occaecati',
                        ),
                    },
                },
                remove=[
                    'impedit',
                    'explicabo',
                ],
                update={
                    "aut": [
                        shared.UpdateActionRequest(
                            from_='dicta',
                            op='maiores',
                            path='natus',
                            value='velit',
                        ),
                        shared.UpdateActionRequest(
                            from_='voluptatibus',
                            op='voluptas',
                            path='asperiores',
                            value='aperiam',
                        ),
                    ],
                    "ea": [
                        shared.UpdateActionRequest(
                            from_='consequuntur',
                            op='repellendus',
                            path='officia',
                            value='maxime',
                        ),
                        shared.UpdateActionRequest(
                            from_='dignissimos',
                            op='officia',
                            path='asperiores',
                            value='nemo',
                        ),
                    ],
                },
            ),
            shared=[
                shared.UpdateActionRequest(
                    from_='quaerat',
                    op='porro',
                    path='quod',
                    value='labore',
                ),
            ],
        ),
    ],
    app_id='ab',
    delta_id='adipisci',
    org_id='fuga',
)

res = s.delta.patch_orgs_org_id_apps_app_id_deltas_delta_id_(req)

if res.delta_response is not None:
    # handle response
```

## post_orgs_org_id_apps_app_id_deltas

Create a new Delta

### Example Usage

```python
import test_1
import dateutil.parser
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDDeltasRequest(
    delta_request=shared.DeltaRequest(
        id='a63aae8d-6786-44db-b675-fd5e60b375ed',
        metadata=shared.DeltaMetadataRequest(
            archived=False,
            contributers=[
                'doloribus',
                'suscipit',
            ],
            created_at=dateutil.parser.isoparse('2020-06-22T09:37:23.523Z'),
            created_by='reiciendis',
            env_id='quidem',
            last_modified_at=dateutil.parser.isoparse('2020-06-22T09:37:23.523Z'),
            name='Dr. Terence Gulgowski',
            shared=False,
        ),
        modules=shared.ModuleDeltasRequest(
            add={
                "amet": {
                    "dignissimos": shared.ControllerRequest(
                        kind='a',
                        message='debitis',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "laboriosam": 'ipsa',
                                        "voluptates": 'libero',
                                        "vitae": 'accusamus',
                                    },
                                    {
                                        "tempora": 'aspernatur',
                                        "voluptas": 'voluptas',
                                        "voluptas": 'minima',
                                    },
                                ],
                                phase='nobis',
                                pod_name='dolorum',
                                revision=237807,
                                status='minus',
                            ),
                        ],
                        replicas=171853,
                        revision=503934,
                        status='in',
                    ),
                },
            },
            remove=[
                'aliquam',
                'officiis',
            ],
            update={
                "ullam": [
                    shared.UpdateActionRequest(
                        from_='cum',
                        op='blanditiis',
                        path='quas',
                        value='hic',
                    ),
                ],
                "nesciunt": [
                    shared.UpdateActionRequest(
                        from_='corrupti',
                        op='pariatur',
                        path='totam',
                        value='hic',
                    ),
                    shared.UpdateActionRequest(
                        from_='exercitationem',
                        op='nobis',
                        path='sit',
                        value='rerum',
                    ),
                    shared.UpdateActionRequest(
                        from_='sed',
                        op='reiciendis',
                        path='explicabo',
                        value='asperiores',
                    ),
                ],
                "facilis": [
                    shared.UpdateActionRequest(
                        from_='expedita',
                        op='ab',
                        path='iste',
                        value='dolore',
                    ),
                    shared.UpdateActionRequest(
                        from_='laborum',
                        op='sed',
                        path='in',
                        value='commodi',
                    ),
                ],
                "quidem": [
                    shared.UpdateActionRequest(
                        from_='voluptas',
                        op='unde',
                        path='architecto',
                        value='suscipit',
                    ),
                ],
            },
        ),
        shared=[
            shared.UpdateActionRequest(
                from_='debitis',
                op='illo',
                path='reiciendis',
                value='perferendis',
            ),
            shared.UpdateActionRequest(
                from_='corrupti',
                op='maiores',
                path='incidunt',
                value='sed',
            ),
            shared.UpdateActionRequest(
                from_='provident',
                op='eius',
                path='necessitatibus',
                value='ipsum',
            ),
            shared.UpdateActionRequest(
                from_='ea',
                op='occaecati',
                path='quos',
                value='voluptatibus',
            ),
        ],
    ),
    app_id='tempora',
    org_id='tempora',
)

res = s.delta.post_orgs_org_id_apps_app_id_deltas(req)

if res.post_orgs_org_id_apps_app_id_deltas_200_application_json_one_of is not None:
    # handle response
```

## put_delta

Update an existing Delta

### Example Usage

```python
import test_1
import dateutil.parser
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PutDeltaRequest(
    delta_request=shared.DeltaRequest(
        id='7f603e8b-445e-480c-a55e-fd20e457e185',
        metadata=shared.DeltaMetadataRequest(
            archived=False,
            contributers=[
                'cum',
                'laboriosam',
                'dolorum',
            ],
            created_at=dateutil.parser.isoparse('2020-06-22T09:37:23.523Z'),
            created_by='voluptatum',
            env_id='error',
            last_modified_at=dateutil.parser.isoparse('2020-06-22T09:37:23.523Z'),
            name='Rudolph Trantow',
            shared=False,
        ),
        modules=shared.ModuleDeltasRequest(
            add={
                "officia": {
                    "corrupti": shared.ControllerRequest(
                        kind='accusamus',
                        message='tempora',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "fugiat": 'voluptatem',
                                        "culpa": 'expedita',
                                    },
                                ],
                                phase='magnam',
                                pod_name='consequatur',
                                revision=460220,
                                status='ipsam',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "quas": 'repudiandae',
                                        "corporis": 'et',
                                        "blanditiis": 'ex',
                                    },
                                ],
                                phase='sed',
                                pod_name='sit',
                                revision=425508,
                                status='nostrum',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "consequatur": 'incidunt',
                                        "reiciendis": 'dolorem',
                                        "harum": 'dicta',
                                    },
                                    {
                                        "occaecati": 'labore',
                                    },
                                    {
                                        "atque": 'laborum',
                                        "nam": 'tenetur',
                                        "laboriosam": 'alias',
                                    },
                                    {
                                        "deserunt": 'voluptate',
                                    },
                                ],
                                phase='unde',
                                pod_name='reiciendis',
                                revision=588740,
                                status='repellendus',
                            ),
                        ],
                        replicas=962771,
                        revision=914791,
                        status='perferendis',
                    ),
                    "est": shared.ControllerRequest(
                        kind='quidem',
                        message='reprehenderit',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "mollitia": 'veniam',
                                        "voluptatem": 'quisquam',
                                        "repudiandae": 'quasi',
                                    },
                                    {
                                        "reprehenderit": 'asperiores',
                                        "totam": 'suscipit',
                                        "quidem": 'maxime',
                                    },
                                    {
                                        "esse": 'amet',
                                    },
                                ],
                                phase='assumenda',
                                pod_name='ea',
                                revision=539118,
                                status='error',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "accusamus": 'natus',
                                        "minima": 'aspernatur',
                                        "ex": 'maiores',
                                        "corrupti": 'at',
                                    },
                                    {
                                        "blanditiis": 'suscipit',
                                        "repudiandae": 'atque',
                                        "atque": 'sunt',
                                    },
                                    {
                                        "dolorum": 'repellendus',
                                        "labore": 'reiciendis',
                                        "doloremque": 'repudiandae',
                                        "dicta": 'accusantium',
                                    },
                                    {
                                        "dolores": 'enim',
                                    },
                                ],
                                phase='laboriosam',
                                pod_name='velit',
                                revision=952143,
                                status='molestias',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "consequuntur": 'occaecati',
                                        "officiis": 'perspiciatis',
                                        "in": 'adipisci',
                                        "eveniet": 'occaecati',
                                    },
                                    {
                                        "fugit": 'id',
                                    },
                                ],
                                phase='quis',
                                pod_name='reprehenderit',
                                revision=625528,
                                status='illo',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "eveniet": 'non',
                                        "vero": 'doloremque',
                                        "iure": 'ipsa',
                                    },
                                    {
                                        "quae": 'molestiae',
                                        "eveniet": 'qui',
                                        "cum": 'iure',
                                    },
                                ],
                                phase='necessitatibus',
                                pod_name='ratione',
                                revision=672582,
                                status='distinctio',
                            ),
                        ],
                        replicas=528940,
                        revision=523006,
                        status='aliquam',
                    ),
                    "ad": shared.ControllerRequest(
                        kind='repellat',
                        message='alias',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "mollitia": 'voluptas',
                                        "alias": 'maiores',
                                    },
                                    {
                                        "dolores": 'id',
                                        "minima": 'dolore',
                                        "dolorum": 'nesciunt',
                                        "quae": 'recusandae',
                                    },
                                    {
                                        "quaerat": 'molestiae',
                                        "ex": 'ut',
                                        "culpa": 'adipisci',
                                    },
                                ],
                                phase='debitis',
                                pod_name='laudantium',
                                revision=432606,
                                status='nemo',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "provident": 'quis',
                                        "eum": 'reiciendis',
                                    },
                                    {
                                        "aspernatur": 'ullam',
                                        "quasi": 'animi',
                                        "nostrum": 'mollitia',
                                    },
                                    {
                                        "possimus": 'animi',
                                        "ex": 'aliquid',
                                        "accusantium": 'repellat',
                                    },
                                    {
                                        "ullam": 'in',
                                        "nam": 'earum',
                                        "officia": 'laborum',
                                        "placeat": 'modi',
                                    },
                                ],
                                phase='voluptatibus',
                                pod_name='molestias',
                                revision=889794,
                                status='sapiente',
                            ),
                        ],
                        replicas=764562,
                        revision=113486,
                        status='rerum',
                    ),
                },
                "tempora": {
                    "inventore": shared.ControllerRequest(
                        kind='fugit',
                        message='cumque',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "aspernatur": 'eum',
                                    },
                                ],
                                phase='eius',
                                pod_name='rem',
                                revision=871083,
                                status='impedit',
                            ),
                        ],
                        replicas=179410,
                        revision=958741,
                        status='eum',
                    ),
                    "dicta": shared.ControllerRequest(
                        kind='minima',
                        message='beatae',
                        pods=[
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "soluta": 'hic',
                                        "illum": 'eaque',
                                        "earum": 'perspiciatis',
                                        "maiores": 'debitis',
                                    },
                                    {
                                        "porro": 'suscipit',
                                        "dolorem": 'fugit',
                                    },
                                    {
                                        "fuga": 'ratione',
                                        "animi": 'necessitatibus',
                                        "nulla": 'consequatur',
                                        "quasi": 'et',
                                    },
                                ],
                                phase='ducimus',
                                pod_name='natus',
                                revision=581082,
                                status='suscipit',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "magni": 'doloribus',
                                    },
                                ],
                                phase='nulla',
                                pod_name='necessitatibus',
                                revision=58534,
                                status='tempora',
                            ),
                            shared.PodStateRequest(
                                container_statuses=[
                                    {
                                        "dicta": 'iusto',
                                        "esse": 'praesentium',
                                    },
                                    {
                                        "reiciendis": 'vel',
                                        "architecto": 'fugiat',
                                        "doloremque": 'dicta',
                                        "odio": 'tempora',
                                    },
                                ],
                                phase='esse',
                                pod_name='ex',
                                revision=235263,
                                status='aliquid',
                            ),
                        ],
                        replicas=58870,
                        revision=671384,
                        status='sunt',
                    ),
                },
            },
            remove=[
                'fugiat',
                'expedita',
            ],
            update={
                "officia": [
                    shared.UpdateActionRequest(
                        from_='aliquid',
                        op='perferendis',
                        path='eum',
                        value='voluptas',
                    ),
                    shared.UpdateActionRequest(
                        from_='iste',
                        op='id',
                        path='ab',
                        value='error',
                    ),
                ],
                "possimus": [
                    shared.UpdateActionRequest(
                        from_='mollitia',
                        op='laborum',
                        path='libero',
                        value='ad',
                    ),
                    shared.UpdateActionRequest(
                        from_='deleniti',
                        op='enim',
                        path='vitae',
                        value='repellendus',
                    ),
                    shared.UpdateActionRequest(
                        from_='ex',
                        op='quo',
                        path='ex',
                        value='ut',
                    ),
                    shared.UpdateActionRequest(
                        from_='ad',
                        op='expedita',
                        path='voluptatem',
                        value='molestias',
                    ),
                ],
            },
        ),
        shared=[
            shared.UpdateActionRequest(
                from_='aliquid',
                op='beatae',
                path='voluptatum',
                value='omnis',
            ),
            shared.UpdateActionRequest(
                from_='veritatis',
                op='rerum',
                path='est',
                value='culpa',
            ),
            shared.UpdateActionRequest(
                from_='voluptatem',
                op='sapiente',
                path='officiis',
                value='architecto',
            ),
        ],
    ),
    app_id='fuga',
    delta_id='pariatur',
    org_id='debitis',
)

res = s.delta.put_delta(req)

if res.status_code == 200:
    # handle response
```

## put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_archived

Archived Deltas are still accessible but can no longer be updated.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataArchivedRequest(
    request_body=False,
    app_id='voluptatem',
    delta_id='alias',
    org_id='deleniti',
)

res = s.delta.put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_archived(req)

if res.status_code == 200:
    # handle response
```

## put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_env_id

Change the Environment of a Delta

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataEnvIDRequest(
    request_body='earum',
    app_id='ex',
    delta_id='sapiente',
    org_id='rem',
)

res = s.delta.put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_env_id(req)

if res.status_code == 200:
    # handle response
```

## put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_name

Change the name of a Delta

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataNameRequest(
    request_body='minus',
    app_id='nemo',
    delta_id='asperiores',
    org_id='ratione',
)

res = s.delta.put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_name(req)

if res.status_code == 200:
    # handle response
```
