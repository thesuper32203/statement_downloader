# PaymentSuccessIndicatorsPhone

The phone information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_hint** | **str** | The ISO-3166 alpha-2 country code of the phone number. | [optional] 
**number** | **str** | The phone number in E.164 or local format. The default country calling code is +1 (USA). Note: This field is required only if email is not provided. | [optional] 

## Example

```python
from openapi_client.models.payment_success_indicators_phone import PaymentSuccessIndicatorsPhone

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSuccessIndicatorsPhone from a JSON string
payment_success_indicators_phone_instance = PaymentSuccessIndicatorsPhone.from_json(json)
# print the JSON string representation of the object
print(PaymentSuccessIndicatorsPhone.to_json())

# convert the object into a dict
payment_success_indicators_phone_dict = payment_success_indicators_phone_instance.to_dict()
# create an instance of PaymentSuccessIndicatorsPhone from a dict
payment_success_indicators_phone_from_dict = PaymentSuccessIndicatorsPhone.from_dict(payment_success_indicators_phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


