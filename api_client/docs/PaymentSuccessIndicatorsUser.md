# PaymentSuccessIndicatorsUser

The user's information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name provided by the customer for the transaction. | [optional] 
**email** | **str** | The email provided by the customer for the transaction. | [optional] 
**address** | [**PaymentSuccessIndicatorsAddress**](PaymentSuccessIndicatorsAddress.md) |  | [optional] 
**phone** | [**PaymentSuccessIndicatorsPhone**](PaymentSuccessIndicatorsPhone.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_success_indicators_user import PaymentSuccessIndicatorsUser

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSuccessIndicatorsUser from a JSON string
payment_success_indicators_user_instance = PaymentSuccessIndicatorsUser.from_json(json)
# print the JSON string representation of the object
print(PaymentSuccessIndicatorsUser.to_json())

# convert the object into a dict
payment_success_indicators_user_dict = payment_success_indicators_user_instance.to_dict()
# create an instance of PaymentSuccessIndicatorsUser from a dict
payment_success_indicators_user_from_dict = PaymentSuccessIndicatorsUser.from_dict(payment_success_indicators_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


