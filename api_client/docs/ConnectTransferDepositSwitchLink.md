# ConnectTransferDepositSwitchLink

contains url to launch connect session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | web url to launch a connect session | [optional] 

## Example

```python
from openapi_client.models.connect_transfer_deposit_switch_link import ConnectTransferDepositSwitchLink

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectTransferDepositSwitchLink from a JSON string
connect_transfer_deposit_switch_link_instance = ConnectTransferDepositSwitchLink.from_json(json)
# print the JSON string representation of the object
print(ConnectTransferDepositSwitchLink.to_json())

# convert the object into a dict
connect_transfer_deposit_switch_link_dict = connect_transfer_deposit_switch_link_instance.to_dict()
# create an instance of ConnectTransferDepositSwitchLink from a dict
connect_transfer_deposit_switch_link_from_dict = ConnectTransferDepositSwitchLink.from_dict(connect_transfer_deposit_switch_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


