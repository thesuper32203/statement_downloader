# DisputeStatementErrorMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | An error code for dispute statement. Useful links: [API Errors](https://developer.mastercard.com/open-banking-us/documentation/errors/), [Aggregation Status Codes](https://developer.mastercard.com/open-banking-us/documentation/products/manage/aggregation-status-codes/). | 
**status** | **str** | A status code | [optional] 
**message** | **str** | An error message | 

## Example

```python
from openapi_client.models.dispute_statement_error_message import DisputeStatementErrorMessage

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeStatementErrorMessage from a JSON string
dispute_statement_error_message_instance = DisputeStatementErrorMessage.from_json(json)
# print the JSON string representation of the object
print(DisputeStatementErrorMessage.to_json())

# convert the object into a dict
dispute_statement_error_message_dict = dispute_statement_error_message_instance.to_dict()
# create an instance of DisputeStatementErrorMessage from a dict
dispute_statement_error_message_from_dict = DisputeStatementErrorMessage.from_dict(dispute_statement_error_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


