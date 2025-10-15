# DESAddress

Address source of the transactions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** | Line 1 of the transaction address. | [optional] 
**line2** | **str** | Line 2 of the transaction address. | [optional] 
**city** | **str** | City of the transaction. | [optional] 
**state** | **str** | State of the transaction. | [optional] 
**postal_code** | **str** | Postal Code of the transaction. | [optional] 
**country** | **str** | Country of the transaction. | [optional] 
**latitude** | **float** | Latitude of the transaction. | [optional] 
**longitude** | **float** | Longitude of the transaction. | [optional] 
**phone_number** | **str** | Phone number of the transaction. | [optional] 

## Example

```python
from openapi_client.models.des_address import DESAddress

# TODO update the JSON string below
json = "{}"
# create an instance of DESAddress from a JSON string
des_address_instance = DESAddress.from_json(json)
# print the JSON string representation of the object
print(DESAddress.to_json())

# convert the object into a dict
des_address_dict = des_address_instance.to_dict()
# create an instance of DESAddress from a dict
des_address_from_dict = DESAddress.from_dict(des_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


