# ErrorWrapper

A top level object for errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**Errors**](Errors.md) |  | 

## Example

```python
from openapi_client.models.error_wrapper import ErrorWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorWrapper from a JSON string
error_wrapper_instance = ErrorWrapper.from_json(json)
# print the JSON string representation of the object
print(ErrorWrapper.to_json())

# convert the object into a dict
error_wrapper_dict = error_wrapper_instance.to_dict()
# create an instance of ErrorWrapper from a dict
error_wrapper_from_dict = ErrorWrapper.from_dict(error_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


