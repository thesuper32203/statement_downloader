# ThirdPartyAccessReceiptData

An object representing consent access data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receipt** | [**ThirdPartyAccessReceipt**](ThirdPartyAccessReceipt.md) |  | [optional] 
**proof** | [**ThirdPartyAccessProof**](ThirdPartyAccessProof.md) |  | [optional] 

## Example

```python
from openapi_client.models.third_party_access_receipt_data import ThirdPartyAccessReceiptData

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyAccessReceiptData from a JSON string
third_party_access_receipt_data_instance = ThirdPartyAccessReceiptData.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyAccessReceiptData.to_json())

# convert the object into a dict
third_party_access_receipt_data_dict = third_party_access_receipt_data_instance.to_dict()
# create an instance of ThirdPartyAccessReceiptData from a dict
third_party_access_receipt_data_from_dict = ThirdPartyAccessReceiptData.from_dict(third_party_access_receipt_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


