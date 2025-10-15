# NewAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | Address line 1 | [optional] 
**address_line2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State | [optional] 
**country** | **str** | Two-letter ISO 3166-1 alpha-2 country code | [optional] 
**postal_code** | **str** | A ZIP code | [optional] 

## Example

```python
from openapi_client.models.new_address import NewAddress

# TODO update the JSON string below
json = "{}"
# create an instance of NewAddress from a JSON string
new_address_instance = NewAddress.from_json(json)
# print the JSON string representation of the object
print(NewAddress.to_json())

# convert the object into a dict
new_address_dict = new_address_instance.to_dict()
# create an instance of NewAddress from a dict
new_address_from_dict = NewAddress.from_dict(new_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


