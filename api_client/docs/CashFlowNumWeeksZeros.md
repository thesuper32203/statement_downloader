# CashFlowNumWeeksZeros

Weeks with zero transactions during the known history of the account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**historic_number_of_weeks_with_data_available** | **int** | Number of weeks during known history of account in which data was available | 
**historic_number_of_weeks_zero_transactions** | **int** | Number of weeks during known history of account where zero transactions were posted | 
**historic_weeks_with_zero_transactions** | [**List[ObbWeekOfYear]**](ObbWeekOfYear.md) | List of weeks with zero reported transactions | 

## Example

```python
from openapi_client.models.cash_flow_num_weeks_zeros import CashFlowNumWeeksZeros

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowNumWeeksZeros from a JSON string
cash_flow_num_weeks_zeros_instance = CashFlowNumWeeksZeros.from_json(json)
# print the JSON string representation of the object
print(CashFlowNumWeeksZeros.to_json())

# convert the object into a dict
cash_flow_num_weeks_zeros_dict = cash_flow_num_weeks_zeros_instance.to_dict()
# create an instance of CashFlowNumWeeksZeros from a dict
cash_flow_num_weeks_zeros_from_dict = CashFlowNumWeeksZeros.from_dict(cash_flow_num_weeks_zeros_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


