# LoanPaymentDetailsLoan

Loan details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | An account ID | 
**loan_number** | **str** | Institution&#39;s ID of the Student Loan | 
**loan_payment_number** | **str** | The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number. | 
**loan_payment_address** | **str** | The payment address to which send manual payments should be sent | 
**loan_future_payoff_amount** | **float** | The payoff amount for the loan | [optional] 
**loan_future_payoff_date** | **datetime** | The date to which the \&quot;Future Payoff Amount\&quot; applies | [optional] 

## Example

```python
from openapi_client.models.loan_payment_details_loan import LoanPaymentDetailsLoan

# TODO update the JSON string below
json = "{}"
# create an instance of LoanPaymentDetailsLoan from a JSON string
loan_payment_details_loan_instance = LoanPaymentDetailsLoan.from_json(json)
# print the JSON string representation of the object
print(LoanPaymentDetailsLoan.to_json())

# convert the object into a dict
loan_payment_details_loan_dict = loan_payment_details_loan_instance.to_dict()
# create an instance of LoanPaymentDetailsLoan from a dict
loan_payment_details_loan_from_dict = LoanPaymentDetailsLoan.from_dict(loan_payment_details_loan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


