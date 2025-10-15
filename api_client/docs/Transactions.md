# Transactions

A list of transactions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found** | **int** | The total number of results matching search criteria | 
**displaying** | **int** | The number of results returned | 
**more_available** | **str** | If the value of &#x60;moreAvailable&#x60; is \&quot;true\&quot;, you can retrieve the next page of results by increasing the value of the start parameter in your next request:\&quot;...&amp;start&#x3D;6&amp;limit&#x3D;5\&quot; | 
**from_date** | **str** | Value of the &#x60;fromDate&#x60; request parameter that generated this response. This date is in Unix epoch time (in seconds). | 
**to_date** | **str** | Value of the &#x60;toDate&#x60; request parameter that generated this response. This date is in Unix epoch time (in seconds). | 
**sort** | **str** | Value of the sort request parameter that generated this response | 
**transactions** | [**List[Transaction]**](Transaction.md) | The array of transactions | 
**daily_balances** | [**List[DailyBalance]**](DailyBalance.md) | Array of daily beginning and ending account balances for each day that transactions are recorded | [optional] 

## Example

```python
from openapi_client.models.transactions import Transactions

# TODO update the JSON string below
json = "{}"
# create an instance of Transactions from a JSON string
transactions_instance = Transactions.from_json(json)
# print the JSON string representation of the object
print(Transactions.to_json())

# convert the object into a dict
transactions_dict = transactions_instance.to_dict()
# create an instance of Transactions from a dict
transactions_from_dict = Transactions.from_dict(transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


