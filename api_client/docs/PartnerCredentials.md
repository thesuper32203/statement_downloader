# PartnerCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in) | 
**partner_secret** | **str** | Your Partner Secret displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in) | 

## Example

```python
from openapi_client.models.partner_credentials import PartnerCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerCredentials from a JSON string
partner_credentials_instance = PartnerCredentials.from_json(json)
# print the JSON string representation of the object
print(PartnerCredentials.to_json())

# convert the object into a dict
partner_credentials_dict = partner_credentials_instance.to_dict()
# create an instance of PartnerCredentials from a dict
partner_credentials_from_dict = PartnerCredentials.from_dict(partner_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


