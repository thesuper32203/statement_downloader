# LoanPaymentDetailsGroup

Group details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | An account ID | 
**group_number** | **str** | Institution&#39;s ID of the Student Loan Group | 
**group_payment_number** | **str** | The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number. | 
**group_payment_address** | **str** | The payment address to which send manual payments should be sent | 
**group_future_payoff_amount** | **float** | The payoff amount for the group | [optional] 
**group_future_payoff_date** | **datetime** | The date to which the \&quot;Future Payoff Amount\&quot; applies | [optional] 
**group_loan_detail** | [**List[LoanPaymentDetailsLoan]**](LoanPaymentDetailsLoan.md) |  | 

## Example

```python
from openapi_client.models.loan_payment_details_group import LoanPaymentDetailsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of LoanPaymentDetailsGroup from a JSON string
loan_payment_details_group_instance = LoanPaymentDetailsGroup.from_json(json)
# print the JSON string representation of the object
print(LoanPaymentDetailsGroup.to_json())

# convert the object into a dict
loan_payment_details_group_dict = loan_payment_details_group_instance.to_dict()
# create an instance of LoanPaymentDetailsGroup from a dict
loan_payment_details_group_from_dict = LoanPaymentDetailsGroup.from_dict(loan_payment_details_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


