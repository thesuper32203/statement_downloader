# CashFlowInflowAttributes

Inflow Attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_deposit_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Average value of deposits during periods in the report | [optional] 
**count_deposits_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndCount]**](ObbDateRangeAndCount.md) | Count of all deposits during periods in the report | 
**historic_count_of_deposit_transactions** | **int** | Count of ALL deposits over entire known history of the account (may exceed requested length of report) | 
**historic_sum_of_deposits** | **float** | Sum of ALL deposits over entire known history of the account (may exceed requested length of report) | [optional] 
**maximum_deposit_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Maximum deposit value for different periods in the report | 
**minimum_deposit_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Minimum deposit value for different periods in the report | 
**sum_deposits_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Sum of all deposits during periods in the report | 

## Example

```python
from openapi_client.models.cash_flow_inflow_attributes import CashFlowInflowAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowInflowAttributes from a JSON string
cash_flow_inflow_attributes_instance = CashFlowInflowAttributes.from_json(json)
# print the JSON string representation of the object
print(CashFlowInflowAttributes.to_json())

# convert the object into a dict
cash_flow_inflow_attributes_dict = cash_flow_inflow_attributes_instance.to_dict()
# create an instance of CashFlowInflowAttributes from a dict
cash_flow_inflow_attributes_from_dict = CashFlowInflowAttributes.from_dict(cash_flow_inflow_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


