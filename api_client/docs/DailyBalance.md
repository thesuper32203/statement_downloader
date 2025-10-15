# DailyBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**beginning** | **float** | Beginning daily account balance | 
**ending** | **float** | Ending daily account balance. | 

## Example

```python
from openapi_client.models.daily_balance import DailyBalance

# TODO update the JSON string below
json = "{}"
# create an instance of DailyBalance from a JSON string
daily_balance_instance = DailyBalance.from_json(json)
# print the JSON string representation of the object
print(DailyBalance.to_json())

# convert the object into a dict
daily_balance_dict = daily_balance_instance.to_dict()
# create an instance of DailyBalance from a dict
daily_balance_from_dict = DailyBalance.from_dict(daily_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


