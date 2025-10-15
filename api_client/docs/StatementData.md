# StatementData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | An account ID represented as a number | 
**statement_index** | **int** | Index of the statement to include in the report. Request statements from 1-24. By default, 1 is the most recent statement. Increase the index value to count back (by month) and retrieve its most recent statement. | [optional] [default to 1]

## Example

```python
from openapi_client.models.statement_data import StatementData

# TODO update the JSON string below
json = "{}"
# create an instance of StatementData from a JSON string
statement_data_instance = StatementData.from_json(json)
# print the JSON string representation of the object
print(StatementData.to_json())

# convert the object into a dict
statement_data_dict = statement_data_instance.to_dict()
# create an instance of StatementData from a dict
statement_data_from_dict = StatementData.from_dict(statement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


