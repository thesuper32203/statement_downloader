# PaymentSuccessIndicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | PSI error code for this scenario | [optional] 
**message** | **str** | Detailed reason about the source of the error | [optional] 
**customer_id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | 
**account_id** | **str** | An account ID | 
**pay_req_id** | **str** | The unique ID that represents the response generated for that specific, customer, account, and transaction. | 
**settle_by_date** | **date** | The expected date that the funds, from the consumer’s account, will be moved to the receiving account.  &#x60;settleByDate&#x60; in ISO 8601 date format (YYYY-MM-DD). &#x60;settleByDate&#x60; dictates the number of days the model responds with. The response can range from 3-10 days, including &#x60;day0&#x60;. Details explained below: 1. If &#x60;settleByDate&#x60; is 9 or more days out from today, the response includes 10 days of data, &#x60;day0&#x60; through &#x60;day9&#x60;. 2. If &#x60;settleByDate&#x60; is between 3 and 8 days out from today, the response includes 4-9 days of data, &#x60;day3-8&#x60;. 3. If &#x60;settleByDate&#x60; is between today and 2 days out from today, the response includes 3 days of data, &#x60;day0&#x60; through &#x60;day2&#x60;. | 
**settlement_amount** | **float** | The transaction amount in USD $. | 
**available_balance** | **float** | The available balance provided, by the consumer’s financial institution, at the time of the request. | 
**indicators_by_day** | [**List[Indicator]**](Indicator.md) | An Array of 3-10 days, providing the potentialSettlementDate, compositeScore, scoreIndicator, and reasons. | 

## Example

```python
from openapi_client.models.payment_success_indicator import PaymentSuccessIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSuccessIndicator from a JSON string
payment_success_indicator_instance = PaymentSuccessIndicator.from_json(json)
# print the JSON string representation of the object
print(PaymentSuccessIndicator.to_json())

# convert the object into a dict
payment_success_indicator_dict = payment_success_indicator_instance.to_dict()
# create an instance of PaymentSuccessIndicator from a dict
payment_success_indicator_from_dict = PaymentSuccessIndicator.from_dict(payment_success_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


