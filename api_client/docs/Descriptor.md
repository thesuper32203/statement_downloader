# Descriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Payment Instruction Descriptor Type | 
**value** | **str** | Value that the Descriptor Type Holds | 

## Example

```python
from openapi_client.models.descriptor import Descriptor

# TODO update the JSON string below
json = "{}"
# create an instance of Descriptor from a JSON string
descriptor_instance = Descriptor.from_json(json)
# print the JSON string representation of the object
print(Descriptor.to_json())

# convert the object into a dict
descriptor_dict = descriptor_instance.to_dict()
# create an instance of Descriptor from a dict
descriptor_from_dict = Descriptor.from_dict(descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


