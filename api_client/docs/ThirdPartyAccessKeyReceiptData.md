# ThirdPartyAccessKeyReceiptData

An object representing the third party access key receipt    * `customerId`: This is recipient's customerId represented as a   pseudo identifier.   * `accountId`: This is the value provided to recipient   represented as a pseudo identifier for the accountId.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ThirdPartyAccessReceiptData]**](ThirdPartyAccessReceiptData.md) |  | [optional] 

## Example

```python
from openapi_client.models.third_party_access_key_receipt_data import ThirdPartyAccessKeyReceiptData

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyAccessKeyReceiptData from a JSON string
third_party_access_key_receipt_data_instance = ThirdPartyAccessKeyReceiptData.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyAccessKeyReceiptData.to_json())

# convert the object into a dict
third_party_access_key_receipt_data_dict = third_party_access_key_receipt_data_instance.to_dict()
# create an instance of ThirdPartyAccessKeyReceiptData from a dict
third_party_access_key_receipt_data_from_dict = ThirdPartyAccessKeyReceiptData.from_dict(third_party_access_key_receipt_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


