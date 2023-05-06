# image

## Overview

DEPRECATED: This type exists for historical compatibility and should not be used. Please use the [Artefact API](https://api-docs.humanitec.com/#tag/Artefact) instead.

Container Images (known simply as Images) can be registered with Humanitec. Continuous Integration (CI) pipelines can then notify Humanitec when a new build of a Container Image becomes available. Humanitec tracks the Image along with metadata about how it was built.
<SchemaDefinition schemaRef="#/components/schemas/ImageRequest" />


### Available Operations

* [get_orgs_org_id_images](#get_orgs_org_id_images) - List all Container Images
* [get_orgs_org_id_images_image_id_](#get_orgs_org_id_images_image_id_) - Get a specific Image Object
* [get_orgs_org_id_images_image_id_builds](#get_orgs_org_id_images_image_id_builds) - Lists all the Builds of an Image
* [post_orgs_org_id_images_image_id_builds](#post_orgs_org_id_images_image_id_builds) - Add a new Image Build

## get_orgs_org_id_images

DEPRECATED: This endpoint exists for historical compatibility and should not be used. Please use the [Artefact API](https://api-docs.humanitec.com/#tag/Artefact) instead.

Lists all of the Container Images registered for this organization.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDImagesRequest(
    org_id='distinctio',
)

res = s.image.get_orgs_org_id_images(req)

if res.image_responses is not None:
    # handle response
```

## get_orgs_org_id_images_image_id_

DEPRECATED: This endpoint exists for historical compatibility and should not be used. Please use the [Artefact API](https://api-docs.humanitec.com/#tag/Artefact) instead.

The response includes a list of Image Builds as well as some metadata about the Image such as its Image Source.

Note, `imageId` may not be the same as the container name. `imageId` is determined by the system making notifications about new builds.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDImagesImageIDRequest(
    image_id='voluptatem',
    org_id='autem',
)

res = s.image.get_orgs_org_id_images_image_id_(req)

if res.image_response is not None:
    # handle response
```

## get_orgs_org_id_images_image_id_builds

DEPRECATED: This endpoint exists for historical compatibility and should not be used. Please use the [Artefact API](https://api-docs.humanitec.com/#tag/Artefact) instead.

The response lists all available Image Builds of an Image.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDImagesImageIDBuildsRequest(
    image_id='esse',
    org_id='dolores',
)

res = s.image.get_orgs_org_id_images_image_id_builds(req)

if res.image_build_responses is not None:
    # handle response
```

## post_orgs_org_id_images_image_id_builds

DEPRECATED: This endpoint exists for historical compatibility and should not be used. Please use the [Artefact API](https://api-docs.humanitec.com/#tag/Artefact) instead.

This endpoint is used by Continuous Integration (CI) pipelines to notify Humanitec that a new Image Build is available.

If there is no Image with ID `imageId`, it will be automatically created.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDImagesImageIDBuildsRequest(
    image_build_request=shared.ImageBuildRequest(
        branch='assumenda',
        commit='beatae',
        image='est',
        tags=[
            'corrupti',
            'molestiae',
            'provident',
            'accusamus',
        ],
    ),
    image_id='necessitatibus',
    org_id='tempore',
)

res = s.image.post_orgs_org_id_images_image_id_builds(req)

if res.status_code == 200:
    # handle response
```
