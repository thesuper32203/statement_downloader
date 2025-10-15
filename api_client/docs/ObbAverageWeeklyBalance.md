# ObbAverageWeeklyBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Average daily ending balance during the week | 
**from_date** | **str** | Begin date of the week | 
**to_date** | **str** | End date of the week | 
**week** | **int** | Week number, where the first week of each year begins on January 1st and ends on January 7th. May be in the range [1, 53] | 

## Example

```python
from openapi_client.models.obb_average_weekly_balance import ObbAverageWeeklyBalance

# TODO update the JSON string below
json = "{}"
# create an instance of ObbAverageWeeklyBalance from a JSON string
obb_average_weekly_balance_instance = ObbAverageWeeklyBalance.from_json(json)
# print the JSON string representation of the object
print(ObbAverageWeeklyBalance.to_json())

# convert the object into a dict
obb_average_weekly_balance_dict = obb_average_weekly_balance_instance.to_dict()
# create an instance of ObbAverageWeeklyBalance from a dict
obb_average_weekly_balance_from_dict = ObbAverageWeeklyBalance.from_dict(obb_average_weekly_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


