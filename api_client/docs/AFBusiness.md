# AFBusiness


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of a business | 
**address** | [**AFBusinessAddress**](AFBusinessAddress.md) |  | 

## Example

```python
from openapi_client.models.af_business import AFBusiness

# TODO update the JSON string below
json = "{}"
# create an instance of AFBusiness from a JSON string
af_business_instance = AFBusiness.from_json(json)
# print the JSON string representation of the object
print(AFBusiness.to_json())

# convert the object into a dict
af_business_dict = af_business_instance.to_dict()
# create an instance of AFBusiness from a dict
af_business_from_dict = AFBusiness.from_dict(af_business_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


