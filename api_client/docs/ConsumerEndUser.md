# ConsumerEndUser

Reseller end user information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The first name of the account holder | 
**address** | **str** | Address line 1 | 
**city** | **str** | City | 
**state** | **str** | State | 
**zip** | **str** | A ZIP code | 
**phone** | **str** | A phone number (max length 15). | 
**email** | **str** | An email address | [optional] 
**url** | **str** | Reseller end user URL | [optional] 

## Example

```python
from openapi_client.models.consumer_end_user import ConsumerEndUser

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerEndUser from a JSON string
consumer_end_user_instance = ConsumerEndUser.from_json(json)
# print the JSON string representation of the object
print(ConsumerEndUser.to_json())

# convert the object into a dict
consumer_end_user_dict = consumer_end_user_instance.to_dict()
# create an instance of ConsumerEndUser from a dict
consumer_end_user_from_dict = ConsumerEndUser.from_dict(consumer_end_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


