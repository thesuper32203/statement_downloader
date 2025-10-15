# ThirdPartyAccessKeyData

An object representing the third party access key request  * `customerId`: This is recipient's customer identifier * `partnerId`: This is recipient partner identifier * `thirdPartyPartnerId`: This is requester's partner identifier * `products`: Array of values representing the Mastercard Open Finance APIs for which access needs to be generated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | 
**partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in) | 
**third_party_partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in) | 
**provenance** | [**ThirdPartyAccessProvenance**](ThirdPartyAccessProvenance.md) |  | [optional] 
**products** | [**List[ThirdPartyAccessProduct]**](ThirdPartyAccessProduct.md) |  | 

## Example

```python
from openapi_client.models.third_party_access_key_data import ThirdPartyAccessKeyData

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyAccessKeyData from a JSON string
third_party_access_key_data_instance = ThirdPartyAccessKeyData.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyAccessKeyData.to_json())

# convert the object into a dict
third_party_access_key_data_dict = third_party_access_key_data_instance.to_dict()
# create an instance of ThirdPartyAccessKeyData from a dict
third_party_access_key_data_from_dict = ThirdPartyAccessKeyData.from_dict(third_party_access_key_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


