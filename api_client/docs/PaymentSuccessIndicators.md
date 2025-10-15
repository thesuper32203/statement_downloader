# PaymentSuccessIndicators

A Payment Success Indicators score response, indicating how likely a transaction is to be returned. NSF and Unauthorized return risks are provided if the score has a status of SUCCESS, or the captured errors are listed if the score has a status of FAILURE.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_request_id** | **str** | Unique identifier of the Payments request | 
**status** | **str** | Current status of the score generation. Possible values are \&quot;IN PROGRESS\&quot;, \&quot;SUCCESS\&quot;, \&quot;FAILURE\&quot; | 
**customer_id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | 
**account_id** | **str** | An account ID | 
**request_date** | **date** | The ISO 8601 format (YYYY-MM-DD) date of the request. | 
**transaction** | [**PaymentSuccessIndicatorsTransaction**](PaymentSuccessIndicatorsTransaction.md) |  | 
**nsf_return_risk** | [**NsfReturnRisk**](NsfReturnRisk.md) |  | [optional] 
**unauthorized_return_risk** | [**UnauthorizedReturnRisk**](UnauthorizedReturnRisk.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_success_indicators import PaymentSuccessIndicators

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSuccessIndicators from a JSON string
payment_success_indicators_instance = PaymentSuccessIndicators.from_json(json)
# print the JSON string representation of the object
print(PaymentSuccessIndicators.to_json())

# convert the object into a dict
payment_success_indicators_dict = payment_success_indicators_instance.to_dict()
# create an instance of PaymentSuccessIndicators from a dict
payment_success_indicators_from_dict = PaymentSuccessIndicators.from_dict(payment_success_indicators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


