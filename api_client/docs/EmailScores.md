# EmailScores


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 

## Example

```python
from openapi_client.models.email_scores import EmailScores

# TODO update the JSON string below
json = "{}"
# create an instance of EmailScores from a JSON string
email_scores_instance = EmailScores.from_json(json)
# print the JSON string representation of the object
print(EmailScores.to_json())

# convert the object into a dict
email_scores_dict = email_scores_instance.to_dict()
# create an instance of EmailScores from a dict
email_scores_from_dict = EmailScores.from_dict(email_scores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


