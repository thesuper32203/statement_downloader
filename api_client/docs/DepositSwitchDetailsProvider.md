# DepositSwitchDetailsProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the service provider | 
**name** | **str** | The name of the service provider | 

## Example

```python
from openapi_client.models.deposit_switch_details_provider import DepositSwitchDetailsProvider

# TODO update the JSON string below
json = "{}"
# create an instance of DepositSwitchDetailsProvider from a JSON string
deposit_switch_details_provider_instance = DepositSwitchDetailsProvider.from_json(json)
# print the JSON string representation of the object
print(DepositSwitchDetailsProvider.to_json())

# convert the object into a dict
deposit_switch_details_provider_dict = deposit_switch_details_provider_instance.to_dict()
# create an instance of DepositSwitchDetailsProvider from a dict
deposit_switch_details_provider_from_dict = DepositSwitchDetailsProvider.from_dict(deposit_switch_details_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


