# BusinessDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of a business | 
**address** | [**AFBusinessAddress**](AFBusinessAddress.md) |  | 
**business_id** | **str** | Unique identifier of the business | [optional] 

## Example

```python
from openapi_client.models.business_details import BusinessDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDetails from a JSON string
business_details_instance = BusinessDetails.from_json(json)
# print the JSON string representation of the object
print(BusinessDetails.to_json())

# convert the object into a dict
business_details_dict = business_details_instance.to_dict()
# create an instance of BusinessDetails from a dict
business_details_from_dict = BusinessDetails.from_dict(business_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


