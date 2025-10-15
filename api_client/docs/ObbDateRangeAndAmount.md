# ObbDateRangeAndAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Metric value for the given period | [optional] 
**period** | **str** | Period represented by this metric | 
**period_begin_date** | **str** | Begin date of the period being reported | 
**period_end_date** | **str** | End date of the period being reported | 

## Example

```python
from openapi_client.models.obb_date_range_and_amount import ObbDateRangeAndAmount

# TODO update the JSON string below
json = "{}"
# create an instance of ObbDateRangeAndAmount from a JSON string
obb_date_range_and_amount_instance = ObbDateRangeAndAmount.from_json(json)
# print the JSON string representation of the object
print(ObbDateRangeAndAmount.to_json())

# convert the object into a dict
obb_date_range_and_amount_dict = obb_date_range_and_amount_instance.to_dict()
# create an instance of ObbDateRangeAndAmount from a dict
obb_date_range_and_amount_from_dict = ObbDateRangeAndAmount.from_dict(obb_date_range_and_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


