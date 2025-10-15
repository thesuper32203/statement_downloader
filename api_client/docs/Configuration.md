# Configuration

Used to modify behavior during the login flow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the configuration object | [optional] 
**filter_accounts** | **List[str]** | An optional filter to apply during account activation with institutions that support legacy login forms. | [optional] 
**account_classification_type** | **List[str]** | An optional filter to apply during account activation with institutions that support Oauth integration. Supported filters are: &#x60;personal&#x60;, &#x60;business&#x60;, and &#x60;unknown&#x60;. | [optional] 
**ao_required** | **bool** | When set to true, the user must explicitly permission Account Owner details at OAuth-supported institutions. If they do not, a [239] error is returned, and the login attempt is blocked. Partners are responsible for handling user re-attempt flows to ensure proper permissions are granted | [optional] [default to False]

## Example

```python
from openapi_client.models.configuration import Configuration

# TODO update the JSON string below
json = "{}"
# create an instance of Configuration from a JSON string
configuration_instance = Configuration.from_json(json)
# print the JSON string representation of the object
print(Configuration.to_json())

# convert the object into a dict
configuration_dict = configuration_instance.to_dict()
# create an instance of Configuration from a dict
configuration_from_dict = Configuration.from_dict(configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


