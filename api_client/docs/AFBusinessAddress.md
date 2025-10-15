# AFBusinessAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | Address line 1 | [optional] 
**address_line2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State | [optional] 
**country** | **str** | Country code is Iso3166-1 Alpha-2 code and Alpha 3 standard (max length 3). | [optional] 
**postal_code** | **str** | A ZIP code | [optional] 

## Example

```python
from openapi_client.models.af_business_address import AFBusinessAddress

# TODO update the JSON string below
json = "{}"
# create an instance of AFBusinessAddress from a JSON string
af_business_address_instance = AFBusinessAddress.from_json(json)
# print the JSON string representation of the object
print(AFBusinessAddress.to_json())

# convert the object into a dict
af_business_address_dict = af_business_address_instance.to_dict()
# create an instance of AFBusinessAddress from a dict
af_business_address_from_dict = AFBusinessAddress.from_dict(af_business_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


