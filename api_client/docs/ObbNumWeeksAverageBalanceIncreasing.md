# ObbNumWeeksAverageBalanceIncreasing

Report of average account balance week over week and count of weeks where the average balance increased

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**historic_average_weekly_balances** | [**List[ObbAverageWeeklyBalance]**](ObbAverageWeeklyBalance.md) | Average weekly balances over the known history | 
**historic_number_of_weeks_average_balance_increasing** | **int** | Number of weeks during the known history where the average balance of the account increased week over week | 
**historic_number_of_weeks_with_data_available** | **int** | Number of weeks during the history in which data was available | 

## Example

```python
from openapi_client.models.obb_num_weeks_average_balance_increasing import ObbNumWeeksAverageBalanceIncreasing

# TODO update the JSON string below
json = "{}"
# create an instance of ObbNumWeeksAverageBalanceIncreasing from a JSON string
obb_num_weeks_average_balance_increasing_instance = ObbNumWeeksAverageBalanceIncreasing.from_json(json)
# print the JSON string representation of the object
print(ObbNumWeeksAverageBalanceIncreasing.to_json())

# convert the object into a dict
obb_num_weeks_average_balance_increasing_dict = obb_num_weeks_average_balance_increasing_instance.to_dict()
# create an instance of ObbNumWeeksAverageBalanceIncreasing from a dict
obb_num_weeks_average_balance_increasing_from_dict = ObbNumWeeksAverageBalanceIncreasing.from_dict(obb_num_weeks_average_balance_increasing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


