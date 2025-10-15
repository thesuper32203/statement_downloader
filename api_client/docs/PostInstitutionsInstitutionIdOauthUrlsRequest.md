# PostInstitutionsInstitutionIdOauthUrlsRequest

Used to request an oauth url for a given a given institution and customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uri** | **str** | The &#x60;redirectURI&#x60; will be called when the oauth session has completed. | 
**customer_id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | 
**configuration_id** | **str** | Unique identifier of the configuration object | [optional] 
**service_agreement** | [**ServiceAgreement**](ServiceAgreement.md) |  | 

## Example

```python
from openapi_client.models.post_institutions_institution_id_oauth_urls_request import PostInstitutionsInstitutionIdOauthUrlsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostInstitutionsInstitutionIdOauthUrlsRequest from a JSON string
post_institutions_institution_id_oauth_urls_request_instance = PostInstitutionsInstitutionIdOauthUrlsRequest.from_json(json)
# print the JSON string representation of the object
print(PostInstitutionsInstitutionIdOauthUrlsRequest.to_json())

# convert the object into a dict
post_institutions_institution_id_oauth_urls_request_dict = post_institutions_institution_id_oauth_urls_request_instance.to_dict()
# create an instance of PostInstitutionsInstitutionIdOauthUrlsRequest from a dict
post_institutions_institution_id_oauth_urls_request_from_dict = PostInstitutionsInstitutionIdOauthUrlsRequest.from_dict(post_institutions_institution_id_oauth_urls_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


