# CashFlowMonthlyCashFlowCredits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** | One instance for each complete calendar month in the report | 
**number_of_credits** | **str** | Number of credits by month | 
**total_credits_amount** | **float** | Total amount of credits by month | 
**largest_credit** | **float** | Largest credit by month | 
**number_of_credits_less_transfers** | **str** | Number of credits by month (less transfers) | 
**total_credits_amount_less_transfers** | **float** | Total amount of credits by month (less transfers) | 
**average_credit_amount** | **float** | The average credit amount | 
**estimated_number_of_loan_deposits** | **str** | The estimated number of loan deposits | 
**estimated_loan_deposit_amount** | **float** | The estimated loan deposit amount | 

## Example

```python
from openapi_client.models.cash_flow_monthly_cash_flow_credits import CashFlowMonthlyCashFlowCredits

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowMonthlyCashFlowCredits from a JSON string
cash_flow_monthly_cash_flow_credits_instance = CashFlowMonthlyCashFlowCredits.from_json(json)
# print the JSON string representation of the object
print(CashFlowMonthlyCashFlowCredits.to_json())

# convert the object into a dict
cash_flow_monthly_cash_flow_credits_dict = cash_flow_monthly_cash_flow_credits_instance.to_dict()
# create an instance of CashFlowMonthlyCashFlowCredits from a dict
cash_flow_monthly_cash_flow_credits_from_dict = CashFlowMonthlyCashFlowCredits.from_dict(cash_flow_monthly_cash_flow_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


