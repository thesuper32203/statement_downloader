# Error

A single error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The application that generated this error | [optional] 
**reason_code** | **str** | A unique constant identifying the error case encountered during transaction processing | [optional] 
**description** | **str** | Description of the ReasonCode field with additional details. | [optional] 
**recoverable** | **bool** | Indicates whether this error will always be returned for this request, or retrying could change the outcome | [optional] 
**details** | **str** | Details for backwards compatibility. | [optional] 

## Example

```python
from openapi_client.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


