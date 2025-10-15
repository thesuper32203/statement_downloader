# PaySwitchDetailsPaymentMethodsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of payment method used for the bill payment. Possible values include &#x60;card&#x60; or &#x60;bank&#x60;. | 
**title** | **str** | The title of the card / account | [optional] 
**brand** | **str** | The co-branding for customer&#39;s card | [optional] 
**bank_identifier** | **str** | The bank routing number | [optional] 
**ends_with** | **str** | The trailing portion of customer&#39;s bank account number or card | [optional] 
**bank_account_type** | **str** | The type of account used when payment type is bank | [optional] 

## Example

```python
from openapi_client.models.pay_switch_details_payment_methods_inner import PaySwitchDetailsPaymentMethodsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaySwitchDetailsPaymentMethodsInner from a JSON string
pay_switch_details_payment_methods_inner_instance = PaySwitchDetailsPaymentMethodsInner.from_json(json)
# print the JSON string representation of the object
print(PaySwitchDetailsPaymentMethodsInner.to_json())

# convert the object into a dict
pay_switch_details_payment_methods_inner_dict = pay_switch_details_payment_methods_inner_instance.to_dict()
# create an instance of PaySwitchDetailsPaymentMethodsInner from a dict
pay_switch_details_payment_methods_inner_from_dict = PaySwitchDetailsPaymentMethodsInner.from_dict(pay_switch_details_payment_methods_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


