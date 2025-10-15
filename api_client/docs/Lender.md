# Lender


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | **str** | FCRA required 2-digit Permissible Purpose Code, specifying the reason for retrieving this report. | [optional] 

## Example

```python
from openapi_client.models.lender import Lender

# TODO update the JSON string below
json = "{}"
# create an instance of Lender from a JSON string
lender_instance = Lender.from_json(json)
# print the JSON string representation of the object
print(Lender.to_json())

# convert the object into a dict
lender_dict = lender_instance.to_dict()
# create an instance of Lender from a dict
lender_from_dict = Lender.from_dict(lender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


