# ObbErrorMessage

OBB Error response message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** | Error code | 
**message** | **str** | Detailed reason about the source of the error | 

## Example

```python
from openapi_client.models.obb_error_message import ObbErrorMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ObbErrorMessage from a JSON string
obb_error_message_instance = ObbErrorMessage.from_json(json)
# print the JSON string representation of the object
print(ObbErrorMessage.to_json())

# convert the object into a dict
obb_error_message_dict = obb_error_message_instance.to_dict()
# create an instance of ObbErrorMessage from a dict
obb_error_message_from_dict = ObbErrorMessage.from_dict(obb_error_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


