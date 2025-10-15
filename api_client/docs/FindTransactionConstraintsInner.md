# FindTransactionConstraintsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**find_transaction_description_memo** | **str** | A string to return transactions that have an exact match to Description/Memo.&lt;/br&gt; - Description/Memo&lt;/br&gt;   - Found in the PDF report for reach transactions.&lt;/br&gt;   - A combination of **description** and **memo** from the JSON version of the report.&lt;/br&gt;  | [optional] 
**find_transaction_amount_from** | **float** | A decimal value to return transactions with **amount** greater than or equal to **findTransactionAmountFrom**.&lt;/br&gt; - If both **findTransactionAmountFrom** and **findTransactionAmountTo** are present. Then transactions with  **amount** between (inclusive) both values will be returned.  | [optional] 
**find_transaction_amount_to** | **float** | A decimal value to return transactions with **amount** less than or equal to **findTransactionAmountTo**.&lt;/br&gt; - If both **findTransactionAmountFrom** and **findTransactionAmountTo** are present. Then transactions with  **amount** between (inclusive) both values will be returned.  | [optional] 
**find_transaction_category** | **List[str]** | An array of **categories** to return transactions with an exact match to the array of **category**. Limit of 10.  | [optional] 

## Example

```python
from openapi_client.models.find_transaction_constraints_inner import FindTransactionConstraintsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FindTransactionConstraintsInner from a JSON string
find_transaction_constraints_inner_instance = FindTransactionConstraintsInner.from_json(json)
# print the JSON string representation of the object
print(FindTransactionConstraintsInner.to_json())

# convert the object into a dict
find_transaction_constraints_inner_dict = find_transaction_constraints_inner_instance.to_dict()
# create an instance of FindTransactionConstraintsInner from a dict
find_transaction_constraints_inner_from_dict = FindTransactionConstraintsInner.from_dict(find_transaction_constraints_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


