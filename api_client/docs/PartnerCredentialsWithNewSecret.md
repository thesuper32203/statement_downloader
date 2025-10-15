# PartnerCredentialsWithNewSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in) | 
**partner_secret** | **str** | Your Partner Secret displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in) | 
**new_partner_secret** | **str** | A new value for the Partner Secret | 
**immediate** | **bool** | This is an optional flag, with a default value of true. This flag should be passed as false when the partners want the 30-day grace period to be activated. | [optional] 

## Example

```python
from openapi_client.models.partner_credentials_with_new_secret import PartnerCredentialsWithNewSecret

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerCredentialsWithNewSecret from a JSON string
partner_credentials_with_new_secret_instance = PartnerCredentialsWithNewSecret.from_json(json)
# print the JSON string representation of the object
print(PartnerCredentialsWithNewSecret.to_json())

# convert the object into a dict
partner_credentials_with_new_secret_dict = partner_credentials_with_new_secret_instance.to_dict()
# create an instance of PartnerCredentialsWithNewSecret from a dict
partner_credentials_with_new_secret_from_dict = PartnerCredentialsWithNewSecret.from_dict(partner_credentials_with_new_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


