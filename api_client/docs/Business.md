# Business


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
**business_id** | **str** | Unique identifier of the business | [optional] 
**created_date** | **str** | A date-time without time zone | [optional] 
**modified_date** | **str** | A date-time without time zone | [optional] 

## Example

```python
from openapi_client.models.business import Business

# TODO update the JSON string below
json = "{}"
# create an instance of Business from a JSON string
business_instance = Business.from_json(json)
# print the JSON string representation of the object
print(Business.to_json())

# convert the object into a dict
business_dict = business_instance.to_dict()
# create an instance of Business from a dict
business_from_dict = Business.from_dict(business_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


