# InstitutionAddress

The address of a financial institution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City | [optional] 
**state** | **str** | State | [optional] 
**country** | **str** | Country code is Iso3166-1 Alpha-2 code and Alpha 3 standard (max length 3). | [optional] 
**postal_code** | **str** | A ZIP code | [optional] 
**address_line1** | **str** | Address line 1 | [optional] 
**address_line2** | **str** | Address line 2 | [optional] 

## Example

```python
from openapi_client.models.institution_address import InstitutionAddress

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionAddress from a JSON string
institution_address_instance = InstitutionAddress.from_json(json)
# print the JSON string representation of the object
print(InstitutionAddress.to_json())

# convert the object into a dict
institution_address_dict = institution_address_instance.to_dict()
# create an instance of InstitutionAddress from a dict
institution_address_from_dict = InstitutionAddress.from_dict(institution_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


