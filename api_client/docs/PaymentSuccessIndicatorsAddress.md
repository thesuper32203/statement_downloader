# PaymentSuccessIndicatorsAddress

The customer's address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_line1** | **str** | The first line of the street part in the structured address. | [optional] 
**street_line2** | **str** | The second line of the street part in the structured address. | [optional] 
**city** | **str** | The name of the city in the structured address. | [optional] 
**state** | **str** | The state/province/parent subdivision code of the structured address. | [optional] 
**postal_code** | **str** | The postal code of the structured address. | [optional] 
**country** | **str** | The ISO-3166 alpha-2 country code of the address. | [optional] 

## Example

```python
from openapi_client.models.payment_success_indicators_address import PaymentSuccessIndicatorsAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSuccessIndicatorsAddress from a JSON string
payment_success_indicators_address_instance = PaymentSuccessIndicatorsAddress.from_json(json)
# print the JSON string representation of the object
print(PaymentSuccessIndicatorsAddress.to_json())

# convert the object into a dict
payment_success_indicators_address_dict = payment_success_indicators_address_instance.to_dict()
# create an instance of PaymentSuccessIndicatorsAddress from a dict
payment_success_indicators_address_from_dict = PaymentSuccessIndicatorsAddress.from_dict(payment_success_indicators_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


