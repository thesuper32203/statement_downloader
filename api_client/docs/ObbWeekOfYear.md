# ObbWeekOfYear


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date** | **str** | Begin date of the week | 
**to_date** | **str** | End date of the week | 
**week** | **int** | Week number, where the first week of each year begins on January 1st and ends on January 7th. May be in the range [1, 53] | 

## Example

```python
from openapi_client.models.obb_week_of_year import ObbWeekOfYear

# TODO update the JSON string below
json = "{}"
# create an instance of ObbWeekOfYear from a JSON string
obb_week_of_year_instance = ObbWeekOfYear.from_json(json)
# print the JSON string representation of the object
print(ObbWeekOfYear.to_json())

# convert the object into a dict
obb_week_of_year_dict = obb_week_of_year_instance.to_dict()
# create an instance of ObbWeekOfYear from a dict
obb_week_of_year_from_dict = ObbWeekOfYear.from_dict(obb_week_of_year_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


