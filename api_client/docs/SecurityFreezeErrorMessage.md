# SecurityFreezeErrorMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | An error code for security freeze. Useful links: [API Errors](https://developer.mastercard.com/open-banking-us/documentation/errors/), [Aggregation Status Codes](https://developer.mastercard.com/open-banking-us/documentation/products/manage/aggregation-status-codes/). | 
**status** | **str** | A status code | [optional] 
**message** | **str** | An error message | 

## Example

```python
from openapi_client.models.security_freeze_error_message import SecurityFreezeErrorMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityFreezeErrorMessage from a JSON string
security_freeze_error_message_instance = SecurityFreezeErrorMessage.from_json(json)
# print the JSON string representation of the object
print(SecurityFreezeErrorMessage.to_json())

# convert the object into a dict
security_freeze_error_message_dict = security_freeze_error_message_instance.to_dict()
# create an instance of SecurityFreezeErrorMessage from a dict
security_freeze_error_message_from_dict = SecurityFreezeErrorMessage.from_dict(security_freeze_error_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


