# CashFlowCashFlowBalanceSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_cash_flow_balance_summaries** | [**List[CashFlowMonthlyCashFlowBalanceSummaries]**](CashFlowMonthlyCashFlowBalanceSummaries.md) | List of attributes for each month | 
**min_daily_balance** | **float** | Min Daily Balance across entire transaction history  for all accounts | 
**max_daily_balance** | **float** | Max Daily Balance across entire transaction history for all accounts | 
**twelve_month_average_daily_balance** | **float** | Average Daily Balance across twelve months for all accounts | 
**six_month_average_daily_balance** | **float** | Average Daily Balance across six months for all accounts | 
**two_month_average_daily_balance** | **float** | Average Daily Balance across two months for all accounts | 
**twelve_month_standard_deviation_of_daily_balance** | **str** | Standard Deviation of Daily Balance across twelve months for all accounts | 
**six_month_standard_deviation_of_daily_balance** | **str** | Standard Deviation of Daily Balance across six months for all accounts | [optional] 
**two_month_standard_deviation_of_daily_balance** | **str** | Standard Deviation of Daily Balance across two months for all accounts | 
**number_of_days_negative_balance** | **str** | Number of Days Negative Balance over entire transaction history for all accounts | 
**number_of_days_positive_balance** | **str** | Number of Days Positive Balance over entire transaction history for all accounts | 

## Example

```python
from openapi_client.models.cash_flow_cash_flow_balance_summary import CashFlowCashFlowBalanceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCashFlowBalanceSummary from a JSON string
cash_flow_cash_flow_balance_summary_instance = CashFlowCashFlowBalanceSummary.from_json(json)
# print the JSON string representation of the object
print(CashFlowCashFlowBalanceSummary.to_json())

# convert the object into a dict
cash_flow_cash_flow_balance_summary_dict = cash_flow_cash_flow_balance_summary_instance.to_dict()
# create an instance of CashFlowCashFlowBalanceSummary from a dict
cash_flow_cash_flow_balance_summary_from_dict = CashFlowCashFlowBalanceSummary.from_dict(cash_flow_cash_flow_balance_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


