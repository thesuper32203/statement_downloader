# PaymentEnablementBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | 
**error_count** | **int** | The number of errors or failures that have occurred while processing the API request. If all the requested parameters are returned successfully then this value will be 0. Any value other than zero indicates failures. | 
**account_count** | **int** | Total number of accounts returned. | [optional] 
**account_identity_success_count** | **int** | Total number of successful sections returned when requesting accountIdentity. If not provided, value will be 0. | [optional] 
**balance_details_success_count** | **int** | Total number of successful sections returned when requesting balanceDetails. If not provided, value will be 0. | [optional] 
**payment_instruction_success_count** | **int** | Total number of successful sections returned when requesting paymentInstruction. If not provided, value will be 0. | [optional] 
**accounts** | [**List[PEBAccountDetails]**](PEBAccountDetails.md) | List of Account Details | 

## Example

```python
from openapi_client.models.payment_enablement_bundle import PaymentEnablementBundle

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentEnablementBundle from a JSON string
payment_enablement_bundle_instance = PaymentEnablementBundle.from_json(json)
# print the JSON string representation of the object
print(PaymentEnablementBundle.to_json())

# convert the object into a dict
payment_enablement_bundle_dict = payment_enablement_bundle_instance.to_dict()
# create an instance of PaymentEnablementBundle from a dict
payment_enablement_bundle_from_dict = PaymentEnablementBundle.from_dict(payment_enablement_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


