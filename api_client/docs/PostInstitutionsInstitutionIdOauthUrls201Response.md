# PostInstitutionsInstitutionIdOauthUrls201Response

The response object for requests to generate OAuth URLs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique reference to the login session | 
**url** | **str** | The oauth url to direct the user to | 
**event_stream_id** | **str** | Unique reference to the event stream used to send events to the SDK | 

## Example

```python
from openapi_client.models.post_institutions_institution_id_oauth_urls201_response import PostInstitutionsInstitutionIdOauthUrls201Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostInstitutionsInstitutionIdOauthUrls201Response from a JSON string
post_institutions_institution_id_oauth_urls201_response_instance = PostInstitutionsInstitutionIdOauthUrls201Response.from_json(json)
# print the JSON string representation of the object
print(PostInstitutionsInstitutionIdOauthUrls201Response.to_json())

# convert the object into a dict
post_institutions_institution_id_oauth_urls201_response_dict = post_institutions_institution_id_oauth_urls201_response_instance.to_dict()
# create an instance of PostInstitutionsInstitutionIdOauthUrls201Response from a dict
post_institutions_institution_id_oauth_urls201_response_from_dict = PostInstitutionsInstitutionIdOauthUrls201Response.from_dict(post_institutions_institution_id_oauth_urls201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


