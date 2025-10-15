# ThirdPartyAccessProof

An object representing a digital signature of the access key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | **str** | The digital signature for the \&quot;receipt\&quot; portion of the access key | [optional] 
**key_id** | **str** | The Finicity key identifier is used to sign the access key | [optional] 
**timestamp** | **datetime** | A date-time with time zone | [optional] 

## Example

```python
from openapi_client.models.third_party_access_proof import ThirdPartyAccessProof

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyAccessProof from a JSON string
third_party_access_proof_instance = ThirdPartyAccessProof.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyAccessProof.to_json())

# convert the object into a dict
third_party_access_proof_dict = third_party_access_proof_instance.to_dict()
# create an instance of ThirdPartyAccessProof from a dict
third_party_access_proof_from_dict = ThirdPartyAccessProof.from_dict(third_party_access_proof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


