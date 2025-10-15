# InitiatedMicroDeposit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | An account ID | [optional] 
**status** | **str** | Micro entries successful initiation status | [optional] 
**deposit_count** | **int** | Count of micro entries | [optional] 
**status_description** | **str** | Micro entries successful initiation description | [optional] 
**rail_type** | **str** | The Rail (ACH / RTP) used for initiating bank deposit(s). | [optional] 

## Example

```python
from openapi_client.models.initiated_micro_deposit import InitiatedMicroDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of InitiatedMicroDeposit from a JSON string
initiated_micro_deposit_instance = InitiatedMicroDeposit.from_json(json)
# print the JSON string representation of the object
print(InitiatedMicroDeposit.to_json())

# convert the object into a dict
initiated_micro_deposit_dict = initiated_micro_deposit_instance.to_dict()
# create an instance of InitiatedMicroDeposit from a dict
initiated_micro_deposit_from_dict = InitiatedMicroDeposit.from_dict(initiated_micro_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


