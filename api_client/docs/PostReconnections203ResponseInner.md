# PostReconnections203ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mfa_challenges** | [**List[PostReconnections203ResponseInnerMfaChallengesInner]**](PostReconnections203ResponseInnerMfaChallengesInner.md) | The required MFA Challenges required in order to log in. | [optional] 

## Example

```python
from openapi_client.models.post_reconnections203_response_inner import PostReconnections203ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostReconnections203ResponseInner from a JSON string
post_reconnections203_response_inner_instance = PostReconnections203ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PostReconnections203ResponseInner.to_json())

# convert the object into a dict
post_reconnections203_response_inner_dict = post_reconnections203_response_inner_instance.to_dict()
# create an instance of PostReconnections203ResponseInner from a dict
post_reconnections203_response_inner_from_dict = PostReconnections203ResponseInner.from_dict(post_reconnections203_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


