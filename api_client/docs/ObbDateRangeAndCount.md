# ObbDateRangeAndCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count of occurrences for the given period | 
**period** | **str** | Period represented by this metric | 
**period_begin_date** | **str** | Begin date of the period being reported | 
**period_end_date** | **str** | End date of the period being reported | 

## Example

```python
from openapi_client.models.obb_date_range_and_count import ObbDateRangeAndCount

# TODO update the JSON string below
json = "{}"
# create an instance of ObbDateRangeAndCount from a JSON string
obb_date_range_and_count_instance = ObbDateRangeAndCount.from_json(json)
# print the JSON string representation of the object
print(ObbDateRangeAndCount.to_json())

# convert the object into a dict
obb_date_range_and_count_dict = obb_date_range_and_count_instance.to_dict()
# create an instance of ObbDateRangeAndCount from a dict
obb_date_range_and_count_from_dict = ObbDateRangeAndCount.from_dict(obb_date_range_and_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


