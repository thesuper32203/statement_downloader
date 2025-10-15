# NewBusiness


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The legal name of the business | 
**personally_liable** | **bool** | Indicates whether a business owner is personally liable for a loan | 
**address** | [**NewAddress**](NewAddress.md) |  | 
**phone_number** | [**PhoneNumberFormat**](PhoneNumberFormat.md) |  | 
**url** | **str** | A URL for the business website | [optional] 
**email** | **str** | An email address | [optional] 
**type** | **str** | The business type eg LLC, Corp, S Corp, C Corp, B Corp, Sole Propriertorship, Nonprofit, etc. | [optional] 
**tax_id** | **str** | Provide details of the tax id for the business | [optional] 

## Example

```python
from openapi_client.models.new_business import NewBusiness

# TODO update the JSON string below
json = "{}"
# create an instance of NewBusiness from a JSON string
new_business_instance = NewBusiness.from_json(json)
# print the JSON string representation of the object
print(NewBusiness.to_json())

# convert the object into a dict
new_business_dict = new_business_instance.to_dict()
# create an instance of NewBusiness from a dict
new_business_from_dict = NewBusiness.from_dict(new_business_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


