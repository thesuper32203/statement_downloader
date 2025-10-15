# ThirdPartyAccessReceipt

An object representing consent receipt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | **int** | Representation of the type of consent receipt | [optional] 
**version** | **str** | A schema version of receipt | [optional] 
**receipt_id** | **str** | This is officially the Consent Receipt ID, but is aliased as the Access Key ID. This is a unique identifier managed by Finicity that points to the contents of this JSON document. | [optional] 
**customer_id** | **str** | This is recipient&#39;s customerId represented as a pseudo identifier | [optional] 
**partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in) | [optional] 
**products** | [**List[ThirdPartyAccessProduct]**](ThirdPartyAccessProduct.md) |  | [optional] 
**provenance** | [**ThirdPartyAccessProvenance**](ThirdPartyAccessProvenance.md) |  | [optional] 
**timestamp** | **datetime** | A date-time with time zone | [optional] 

## Example

```python
from openapi_client.models.third_party_access_receipt import ThirdPartyAccessReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyAccessReceipt from a JSON string
third_party_access_receipt_instance = ThirdPartyAccessReceipt.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyAccessReceipt.to_json())

# convert the object into a dict
third_party_access_receipt_dict = third_party_access_receipt_instance.to_dict()
# create an instance of ThirdPartyAccessReceipt from a dict
third_party_access_receipt_from_dict = ThirdPartyAccessReceipt.from_dict(third_party_access_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


