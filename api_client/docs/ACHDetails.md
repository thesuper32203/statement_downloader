# ACHDetails

The routing and account number information to initiate ACH transfers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_number** | **str** | The routing number of the financial institution for specific customer account | 
**real_account_number** | **str** | The account number for initiating ACH transfers for this account | 

## Example

```python
from openapi_client.models.ach_details import ACHDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ACHDetails from a JSON string
ach_details_instance = ACHDetails.from_json(json)
# print the JSON string representation of the object
print(ACHDetails.to_json())

# convert the object into a dict
ach_details_dict = ach_details_instance.to_dict()
# create an instance of ACHDetails from a dict
ach_details_from_dict = ACHDetails.from_dict(ach_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


