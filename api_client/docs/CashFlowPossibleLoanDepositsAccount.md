# CashFlowPossibleLoanDepositsAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Finicity account ID | 
**owner_name** | **str** | The name(s) of the account owner(s). If the owner information is not available, this field will not appear in the report. If the account has multiple owners then all owners will be listed separated by |. | 
**owner_address** | **str** | The mailing address of the account owner(s). If the owner information is not available, this field will not appear in the report. If the account has multiple owners then the address of the primary owner will be listed. | 
**owner_as_of_date** | **int** | The ownerAsOfDate field is populated if the account owner information was retrieved from a prior report and will show the created date of that report. Reports always try and aggregate fresh account owner information and only rarely aren&#39;t able to aggregate it. If account owner information is not able to be aggregated, but it was available from a prior report that had that same account, the information from that prior report will be used and this field will be populated. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/errors/error-list/#handling-epoch-dates-and-times). | [optional] 
**name** | **str** | The account name from the institution | 
**number** | **str** | The account number from the institution (obfuscated) | 
**type** | **str** | CFR: &#x60;ALL&#x60; (&#x60;checking&#x60; / &#x60;savings&#x60; / &#x60;loan&#x60; / &#x60;mortgage&#x60; / &#x60;credit card&#x60; / &#x60;CD&#x60; / &#x60;MM&#x60; / &#x60;investment&#x60;...) | 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt for this account (non-zero means the account was not accessed successfully for this report, and additional fields for this account may not be reliable) | 
**current_balance** | **float** | The cleared balance of the account as-of &#x60;balanceDate&#x60; | 
**available_balance** | **float** | Available balance | 
**balance_date** | **int** | A timestamp showing when the &#x60;balance&#x60; was captured | 
**transactions** | [**List[ReportTransaction]**](ReportTransaction.md) | a list of transaction records | 

## Example

```python
from openapi_client.models.cash_flow_possible_loan_deposits_account import CashFlowPossibleLoanDepositsAccount

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowPossibleLoanDepositsAccount from a JSON string
cash_flow_possible_loan_deposits_account_instance = CashFlowPossibleLoanDepositsAccount.from_json(json)
# print the JSON string representation of the object
print(CashFlowPossibleLoanDepositsAccount.to_json())

# convert the object into a dict
cash_flow_possible_loan_deposits_account_dict = cash_flow_possible_loan_deposits_account_instance.to_dict()
# create an instance of CashFlowPossibleLoanDepositsAccount from a dict
cash_flow_possible_loan_deposits_account_from_dict = CashFlowPossibleLoanDepositsAccount.from_dict(cash_flow_possible_loan_deposits_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


