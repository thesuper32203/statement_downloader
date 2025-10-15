# CashFlowMonthlyCashFlowCreditSummaries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** | One instance for each complete calendar month in the report | 
**number_of_credits** | **str** | Number of credits by month across all accounts | 
**total_credits_amount** | **float** | Total amount of credits by month across all accounts | 
**largest_credit** | **float** | Largest credit by month across all accounts | 
**number_of_credits_less_transfers** | **str** | Number of credits by month (less transfers) across all accounts | 
**total_credits_amount_less_transfers** | **float** | Total amount of credits by month (less transfers) across all accounts | 
**average_credit_amount** | **float** | The average credit amount | 
**estimated_number_of_loan_deposits** | **str** | The estimated number of loan deposits by month | 
**estimated_loan_deposit_amount** | **float** | The estimated loan deposit amount by month | 

## Example

```python
from openapi_client.models.cash_flow_monthly_cash_flow_credit_summaries import CashFlowMonthlyCashFlowCreditSummaries

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowMonthlyCashFlowCreditSummaries from a JSON string
cash_flow_monthly_cash_flow_credit_summaries_instance = CashFlowMonthlyCashFlowCreditSummaries.from_json(json)
# print the JSON string representation of the object
print(CashFlowMonthlyCashFlowCreditSummaries.to_json())

# convert the object into a dict
cash_flow_monthly_cash_flow_credit_summaries_dict = cash_flow_monthly_cash_flow_credit_summaries_instance.to_dict()
# create an instance of CashFlowMonthlyCashFlowCreditSummaries from a dict
cash_flow_monthly_cash_flow_credit_summaries_from_dict = CashFlowMonthlyCashFlowCreditSummaries.from_dict(cash_flow_monthly_cash_flow_credit_summaries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


