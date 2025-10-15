# StreamModel

Describes a history of repeated transactions between the same parties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cadence** | **int** | Number of days that occur between each transaction in the stream | 
**id** | **str** | Stream Id assigned to identified Stream | 
**payee** | **str** | The party in the transaction that is receiving the funds | 
**payor** | **str** | The party in the transaction that is sending the funds | 
**recency** | **int** | Number of days since the last transaction occurred in the stream | 
**transaction_ids** | **List[str]** | List of Transaction IDs that comprise the stream | 

## Example

```python
from openapi_client.models.stream_model import StreamModel

# TODO update the JSON string below
json = "{}"
# create an instance of StreamModel from a JSON string
stream_model_instance = StreamModel.from_json(json)
# print the JSON string representation of the object
print(StreamModel.to_json())

# convert the object into a dict
stream_model_dict = stream_model_instance.to_dict()
# create an instance of StreamModel from a dict
stream_model_from_dict = StreamModel.from_dict(stream_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


