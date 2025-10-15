# CashFlowInsufficientFundsFees

Non-Sufficient Fund Fees

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_of_transactions_for_the_report_time_period** | **int** | Count of all NSF transactions during the report | [optional] 
**sum_of_transactions_for_the_report_time_period** | **float** | Sum of all NSF transactions during the report | [optional] 
**transactions** | [**List[InsufficientFundsTransaction]**](InsufficientFundsTransaction.md) | Transactions categorized as NSF | [optional] 

## Example

```python
from openapi_client.models.cash_flow_insufficient_funds_fees import CashFlowInsufficientFundsFees

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowInsufficientFundsFees from a JSON string
cash_flow_insufficient_funds_fees_instance = CashFlowInsufficientFundsFees.from_json(json)
# print the JSON string representation of the object
print(CashFlowInsufficientFundsFees.to_json())

# convert the object into a dict
cash_flow_insufficient_funds_fees_dict = cash_flow_insufficient_funds_fees_instance.to_dict()
# create an instance of CashFlowInsufficientFundsFees from a dict
cash_flow_insufficient_funds_fees_from_dict = CashFlowInsufficientFundsFees.from_dict(cash_flow_insufficient_funds_fees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


