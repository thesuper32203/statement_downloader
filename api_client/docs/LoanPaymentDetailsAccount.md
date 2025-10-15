# LoanPaymentDetailsAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | An account ID | 
**account_number** | **str** | Institution&#39;s ID of the Student Loan Account | 
**account_payment_number** | **str** | The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number. | 
**account_payment_address** | **str** | The payment address to which send manual payments should be sent | 
**account_future_payoff_amount** | **float** | The payoff amount for the account | [optional] 
**account_future_payoff_date** | **datetime** | The date to which the \&quot;Future Payoff Amount\&quot; applies | [optional] 
**group_detail** | [**List[LoanPaymentDetailsGroup]**](LoanPaymentDetailsGroup.md) | Group details | [optional] 
**loan_detail** | [**List[LoanPaymentDetailsLoan]**](LoanPaymentDetailsLoan.md) | Loan details | [optional] 

## Example

```python
from openapi_client.models.loan_payment_details_account import LoanPaymentDetailsAccount

# TODO update the JSON string below
json = "{}"
# create an instance of LoanPaymentDetailsAccount from a JSON string
loan_payment_details_account_instance = LoanPaymentDetailsAccount.from_json(json)
# print the JSON string representation of the object
print(LoanPaymentDetailsAccount.to_json())

# convert the object into a dict
loan_payment_details_account_dict = loan_payment_details_account_instance.to_dict()
# create an instance of LoanPaymentDetailsAccount from a dict
loan_payment_details_account_from_dict = LoanPaymentDetailsAccount.from_dict(loan_payment_details_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


