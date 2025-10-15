# ReportTransactionBase2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**normalized_payee** | **str** | A normalized payee, derived from the transaction&#39;s &#x60;description&#x60; and &#x60;memo&#x60; fields | [optional] 
**institution_transaction_id** | **str** | The unique identifier given by the FI for each transaction | [optional] 
**category** | **str** | One of the values from Categories (assigned based on the payee name) | [optional] 
**type** | **str** | One of the values from transaction types | [optional] 
**security_type** | **str** | The type of investment security (VOA only) | [optional] 
**symbol** | **str** | Investment symbol (VOA only) | [optional] 
**commission** | **float** | A commission amount | [optional] 

## Example

```python
from openapi_client.models.report_transaction_base2 import ReportTransactionBase2

# TODO update the JSON string below
json = "{}"
# create an instance of ReportTransactionBase2 from a JSON string
report_transaction_base2_instance = ReportTransactionBase2.from_json(json)
# print the JSON string representation of the object
print(ReportTransactionBase2.to_json())

# convert the object into a dict
report_transaction_base2_dict = report_transaction_base2_instance.to_dict()
# create an instance of ReportTransactionBase2 from a dict
report_transaction_base2_from_dict = ReportTransactionBase2.from_dict(report_transaction_base2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


