# ThirdPartyAccessProvenance

Provenance regarding the calling client like `clientFingerprint`, `ipAddress` and `token`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_fingerprint** | **str** | Calling client identifier | [optional] 
**ip_address** | **str** | Calling client IP address | [optional] 
**token** | **str** | Calling client cookie | [optional] 

## Example

```python
from openapi_client.models.third_party_access_provenance import ThirdPartyAccessProvenance

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyAccessProvenance from a JSON string
third_party_access_provenance_instance = ThirdPartyAccessProvenance.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyAccessProvenance.to_json())

# convert the object into a dict
third_party_access_provenance_dict = third_party_access_provenance_instance.to_dict()
# create an instance of ThirdPartyAccessProvenance from a dict
third_party_access_provenance_from_dict = ThirdPartyAccessProvenance.from_dict(third_party_access_provenance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


