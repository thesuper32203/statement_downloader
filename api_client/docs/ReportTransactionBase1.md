# ReportTransactionBase1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A transaction ID | 
**amount** | **float** | The total amount of the transaction. Transactions for deposits are positive values, withdrawals and debits are negative values. | [optional] 
**posted_date** | **int** | A timestamp showing when the transaction was posted or cleared by the institution | 
**description** | **str** | The description of the transaction, as provided by the institution (often known as &#x60;payee&#x60;). In the event that this field is left blank by the institution, Finicity will pass a value of \&quot;No description provided by institution\&quot;. All other values are provided by the institution. | 
**memo** | **str** | The memo field of the transaction, as provided by the institution. The institution must provide either a description, a memo, or both. It is recommended to concatenate the two fields into a single value. | [optional] 

## Example

```python
from openapi_client.models.report_transaction_base1 import ReportTransactionBase1

# TODO update the JSON string below
json = "{}"
# create an instance of ReportTransactionBase1 from a JSON string
report_transaction_base1_instance = ReportTransactionBase1.from_json(json)
# print the JSON string representation of the object
print(ReportTransactionBase1.to_json())

# convert the object into a dict
report_transaction_base1_dict = report_transaction_base1_instance.to_dict()
# create an instance of ReportTransactionBase1 from a dict
report_transaction_base1_from_dict = ReportTransactionBase1.from_dict(report_transaction_base1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


