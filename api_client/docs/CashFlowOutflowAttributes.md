# CashFlowOutflowAttributes

Outflow attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_withdrawal_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Average value of withdrawals during periods in the report | [optional] 
**count_withdrawals_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndCount]**](ObbDateRangeAndCount.md) | Count of all withdrawals during periods in the report | 
**historic_count_of_withdrawal_transactions** | **int** | Count of ALL withdrawals over entire known history of the account (may exceed requested length of report) | 
**historic_sum_of_withdrawals** | **float** | Sum of ALL withdrawals over entire known history of the account (may exceed requested length of report) | [optional] 
**maximum_withdrawal_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Maximum withdrawal value for different periods in the report | 
**minimum_withdrawal_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Minimum withdrawal value for different periods in the report | 
**sum_withdrawals_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Sum of all withdrawals during periods in the report | 

## Example

```python
from openapi_client.models.cash_flow_outflow_attributes import CashFlowOutflowAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowOutflowAttributes from a JSON string
cash_flow_outflow_attributes_instance = CashFlowOutflowAttributes.from_json(json)
# print the JSON string representation of the object
print(CashFlowOutflowAttributes.to_json())

# convert the object into a dict
cash_flow_outflow_attributes_dict = cash_flow_outflow_attributes_instance.to_dict()
# create an instance of CashFlowOutflowAttributes from a dict
cash_flow_outflow_attributes_from_dict = CashFlowOutflowAttributes.from_dict(cash_flow_outflow_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


