# PhoneScores


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 

## Example

```python
from openapi_client.models.phone_scores import PhoneScores

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneScores from a JSON string
phone_scores_instance = PhoneScores.from_json(json)
# print the JSON string representation of the object
print(PhoneScores.to_json())

# convert the object into a dict
phone_scores_dict = phone_scores_instance.to_dict()
# create an instance of PhoneScores from a dict
phone_scores_from_dict = PhoneScores.from_dict(phone_scores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


