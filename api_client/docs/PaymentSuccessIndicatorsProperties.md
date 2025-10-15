# PaymentSuccessIndicatorsProperties

Properties to request a Payment Success Indicator score

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**PaymentSuccessIndicatorsTransaction**](PaymentSuccessIndicatorsTransaction.md) |  | 
**user** | [**PaymentSuccessIndicatorsUser**](PaymentSuccessIndicatorsUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_success_indicators_properties import PaymentSuccessIndicatorsProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSuccessIndicatorsProperties from a JSON string
payment_success_indicators_properties_instance = PaymentSuccessIndicatorsProperties.from_json(json)
# print the JSON string representation of the object
print(PaymentSuccessIndicatorsProperties.to_json())

# convert the object into a dict
payment_success_indicators_properties_dict = payment_success_indicators_properties_instance.to_dict()
# create an instance of PaymentSuccessIndicatorsProperties from a dict
payment_success_indicators_properties_from_dict = PaymentSuccessIndicatorsProperties.from_dict(payment_success_indicators_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


