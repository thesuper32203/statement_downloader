# LoanPaymentDetails

Loan payment details for a customer account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_number** | **str** | The number of the specific loan under the account. | 
**loan_payment_number** | **str** | The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number. | 
**loan_payment_address** | **str** | The payment address to send manual payments to | 
**account_detail** | [**LoanPaymentDetailsAccount**](LoanPaymentDetailsAccount.md) |  | [optional] 

## Example

```python
from openapi_client.models.loan_payment_details import LoanPaymentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LoanPaymentDetails from a JSON string
loan_payment_details_instance = LoanPaymentDetails.from_json(json)
# print the JSON string representation of the object
print(LoanPaymentDetails.to_json())

# convert the object into a dict
loan_payment_details_dict = loan_payment_details_instance.to_dict()
# create an instance of LoanPaymentDetails from a dict
loan_payment_details_from_dict = LoanPaymentDetails.from_dict(loan_payment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


