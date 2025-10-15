# ObbDailyBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date of balance information | 
**day_of_week** | **str** | Day of the week for which balance information available | 
**ending_balance** | **float** | End of day balance | 

## Example

```python
from openapi_client.models.obb_daily_balance import ObbDailyBalance

# TODO update the JSON string below
json = "{}"
# create an instance of ObbDailyBalance from a JSON string
obb_daily_balance_instance = ObbDailyBalance.from_json(json)
# print the JSON string representation of the object
print(ObbDailyBalance.to_json())

# convert the object into a dict
obb_daily_balance_dict = obb_daily_balance_instance.to_dict()
# create an instance of ObbDailyBalance from a dict
obb_daily_balance_from_dict = ObbDailyBalance.from_dict(obb_daily_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


