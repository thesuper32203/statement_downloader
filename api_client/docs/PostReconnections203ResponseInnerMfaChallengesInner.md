# PostReconnections203ResponseInnerMfaChallengesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the MFA challenge | 
**mfa_type** | **str** | The type of MFA challenge:   * TFA_TEXT:  This challenge type will present a single input box to the customer and is commonly used for things like One-Time Passwords.   * TFA_CHOICE: The TFA_CHOICE object represents a multiple choice question and answer selection.   * TFA_MULTI: The TFA_MULTI challenge type will present the customer with multiple images to select from.   * TFA_IMAGE: A TFA_IMAGE challenge will present a captcha-style image the customer will need to decipher. | 
**prompt** | **str** | The MFA prompt text | 
**choice_ids** | **List[str]** | An array of unique identifiers for the MFA choices | 

## Example

```python
from openapi_client.models.post_reconnections203_response_inner_mfa_challenges_inner import PostReconnections203ResponseInnerMfaChallengesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostReconnections203ResponseInnerMfaChallengesInner from a JSON string
post_reconnections203_response_inner_mfa_challenges_inner_instance = PostReconnections203ResponseInnerMfaChallengesInner.from_json(json)
# print the JSON string representation of the object
print(PostReconnections203ResponseInnerMfaChallengesInner.to_json())

# convert the object into a dict
post_reconnections203_response_inner_mfa_challenges_inner_dict = post_reconnections203_response_inner_mfa_challenges_inner_instance.to_dict()
# create an instance of PostReconnections203ResponseInnerMfaChallengesInner from a dict
post_reconnections203_response_inner_mfa_challenges_inner_from_dict = PostReconnections203ResponseInnerMfaChallengesInner.from_dict(post_reconnections203_response_inner_mfa_challenges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


