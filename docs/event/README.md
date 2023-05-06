# event

## Overview

Webhook is a special type of a Job, it performs a HTTPS request to a specified URL with specified headers.
<SchemaDefinition schemaRef="#/components/schemas/WebhookRequest" />


### Available Operations

* [delete_orgs_org_id_apps_app_id_jobs](#delete_orgs_org_id_apps_app_id_jobs) - Deletes all Jobs for the Application
* [delete_orgs_org_id_apps_app_id_webhooks_job_id_](#delete_orgs_org_id_apps_app_id_webhooks_job_id_) - Delete a Webhook
* [get_orgs_org_id_apps_app_id_webhooks](#get_orgs_org_id_apps_app_id_webhooks) - List Webhooks
* [get_orgs_org_id_apps_app_id_webhooks_job_id_](#get_orgs_org_id_apps_app_id_webhooks_job_id_) - Get a Webhook
* [get_orgs_org_id_events](#get_orgs_org_id_events) - List Events
* [post_orgs_org_id_apps_app_id_webhooks](#post_orgs_org_id_apps_app_id_webhooks) - Create a new Webhook
* [post_orgs_org_id_apps_app_id_webhooks_job_id_](#post_orgs_org_id_apps_app_id_webhooks_job_id_) - Update a Webhook

## delete_orgs_org_id_apps_app_id_jobs

Deletes all Jobs for the Application

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDAppsAppIDJobsRequest(
    app_id='facere',
    org_id='libero',
)

res = s.event.delete_orgs_org_id_apps_app_id_jobs(req)

if res.status_code == 200:
    # handle response
```

## delete_orgs_org_id_apps_app_id_webhooks_job_id_

Delete a Webhook

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDAppsAppIDWebhooksJobIDRequest(
    app_id='architecto',
    job_id='voluptatibus',
    org_id='quia',
)

res = s.event.delete_orgs_org_id_apps_app_id_webhooks_job_id_(req)

if res.status_code == 200:
    # handle response
```

## get_orgs_org_id_apps_app_id_webhooks

List Webhooks

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDWebhooksRequest(
    app_id='porro',
    org_id='aliquam',
)

res = s.event.get_orgs_org_id_apps_app_id_webhooks(req)

if res.webhook_responses is not None:
    # handle response
```

## get_orgs_org_id_apps_app_id_webhooks_job_id_

Get a Webhook

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDWebhooksJobIDRequest(
    app_id='velit',
    job_id='illo',
    org_id='accusantium',
)

res = s.event.get_orgs_org_id_apps_app_id_webhooks_job_id_(req)

if res.webhook_response is not None:
    # handle response
```

## get_orgs_org_id_events

List Events

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDEventsRequest(
    org_id='vel',
)

res = s.event.get_orgs_org_id_events(req)

if res.event_responses is not None:
    # handle response
```

## post_orgs_org_id_apps_app_id_webhooks

Create a new Webhook

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDWebhooksRequest(
    webhook_request=shared.WebhookRequest(
        disabled=False,
        headers={
            "beatae": 'vero',
            "excepturi": 'eum',
        },
        id='349e1cf9-e06e-43a4-b700-0ae6b6bc9b8f',
        payload={
            "ullam": 'unde',
            "necessitatibus": 'animi',
        },
        triggers=[
            shared.EventBaseRequest(
                scope='ipsam',
                type='corporis',
            ),
            shared.EventBaseRequest(
                scope='est',
                type='error',
            ),
            shared.EventBaseRequest(
                scope='esse',
                type='labore',
            ),
            shared.EventBaseRequest(
                scope='veritatis',
                type='vero',
            ),
        ],
        url='consectetur',
    ),
    app_id='vitae',
    org_id='inventore',
)

res = s.event.post_orgs_org_id_apps_app_id_webhooks(req)

if res.webhook_response is not None:
    # handle response
```

## post_orgs_org_id_apps_app_id_webhooks_job_id_

Update a Webhook

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDWebhooksJobIDRequest(
    webhook_request=shared.WebhookRequest(
        disabled=False,
        headers={
            "ad": 'qui',
        },
        id='965bb8a7-2026-4114-b5e1-39dbc2259b1a',
        payload={
            "fugiat": 'officia',
            "quos": 'placeat',
            "sit": 'iusto',
        },
        triggers=[
            shared.EventBaseRequest(
                scope='voluptates',
                type='inventore',
            ),
        ],
        url='aperiam',
    ),
    app_id='totam',
    job_id='dolore',
    org_id='eligendi',
)

res = s.event.post_orgs_org_id_apps_app_id_webhooks_job_id_(req)

if res.webhook_response is not None:
    # handle response
```
