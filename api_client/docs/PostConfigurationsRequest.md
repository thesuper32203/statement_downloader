# PostConfigurationsRequest

Used to generate a new configuration, which can be used during the login flow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_accounts** | **List[str]** | An optional filter to apply during account activation with institutions that support legacy login forms. | [optional] 
**account_classification_type** | **List[str]** | An optional filter to apply during account activation with institutions that support Oauth integration. Supported filters are: &#x60;personal&#x60;, &#x60;business&#x60;, and &#x60;unknown&#x60;. | [optional] 
**ao_required** | **bool** | When set to true, the user must explicitly permission Account Owner details at OAuth-supported institutions. If they do not, a [239] error is returned, and the login attempt is blocked. Partners are responsible for handling user re-attempt flows to ensure proper permissions are granted | [optional] [default to False]

## Example

```python
from openapi_client.models.post_configurations_request import PostConfigurationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostConfigurationsRequest from a JSON string
post_configurations_request_instance = PostConfigurationsRequest.from_json(json)
# print the JSON string representation of the object
print(PostConfigurationsRequest.to_json())

# convert the object into a dict
post_configurations_request_dict = post_configurations_request_instance.to_dict()
# create an instance of PostConfigurationsRequest from a dict
post_configurations_request_from_dict = PostConfigurationsRequest.from_dict(post_configurations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


