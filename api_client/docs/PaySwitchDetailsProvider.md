# PaySwitchDetailsProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the service provider | 
**name** | **str** | The name of the service provider | 

## Example

```python
from openapi_client.models.pay_switch_details_provider import PaySwitchDetailsProvider

# TODO update the JSON string below
json = "{}"
# create an instance of PaySwitchDetailsProvider from a JSON string
pay_switch_details_provider_instance = PaySwitchDetailsProvider.from_json(json)
# print the JSON string representation of the object
print(PaySwitchDetailsProvider.to_json())

# convert the object into a dict
pay_switch_details_provider_dict = pay_switch_details_provider_instance.to_dict()
# create an instance of PaySwitchDetailsProvider from a dict
pay_switch_details_provider_from_dict = PaySwitchDetailsProvider.from_dict(pay_switch_details_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


