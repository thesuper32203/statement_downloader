# CashFlowPossibleLoanDeposits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institutions** | [**List[CashFlowPossibleLoanDepositsInstitutions]**](CashFlowPossibleLoanDepositsInstitutions.md) | A list of loan deposit institutions | 

## Example

```python
from openapi_client.models.cash_flow_possible_loan_deposits import CashFlowPossibleLoanDeposits

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowPossibleLoanDeposits from a JSON string
cash_flow_possible_loan_deposits_instance = CashFlowPossibleLoanDeposits.from_json(json)
# print the JSON string representation of the object
print(CashFlowPossibleLoanDeposits.to_json())

# convert the object into a dict
cash_flow_possible_loan_deposits_dict = cash_flow_possible_loan_deposits_instance.to_dict()
# create an instance of CashFlowPossibleLoanDeposits from a dict
cash_flow_possible_loan_deposits_from_dict = CashFlowPossibleLoanDeposits.from_dict(cash_flow_possible_loan_deposits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


