# CashFlowPossibleLoanDepositsInstitutions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Finicity institution ID | 
**name** | **str** | Finicity institution name | 
**url_home_app** | **str** | The URL of the Financial Institution | 
**accounts** | [**List[CashFlowPossibleLoanDepositsAccount]**](CashFlowPossibleLoanDepositsAccount.md) | A list of account records | 

## Example

```python
from openapi_client.models.cash_flow_possible_loan_deposits_institutions import CashFlowPossibleLoanDepositsInstitutions

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowPossibleLoanDepositsInstitutions from a JSON string
cash_flow_possible_loan_deposits_institutions_instance = CashFlowPossibleLoanDepositsInstitutions.from_json(json)
# print the JSON string representation of the object
print(CashFlowPossibleLoanDepositsInstitutions.to_json())

# convert the object into a dict
cash_flow_possible_loan_deposits_institutions_dict = cash_flow_possible_loan_deposits_institutions_instance.to_dict()
# create an instance of CashFlowPossibleLoanDepositsInstitutions from a dict
cash_flow_possible_loan_deposits_institutions_from_dict = CashFlowPossibleLoanDepositsInstitutions.from_dict(cash_flow_possible_loan_deposits_institutions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


