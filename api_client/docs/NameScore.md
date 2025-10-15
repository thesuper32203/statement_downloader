# NameScore

List of account owner Identity Insights

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_name** | **int** | This score represent the matching between user input \&quot;name\&quot; sub-attributes (firstName, middleName, lastName, suffix) along with the account owner details fetch ownerName | 
**first_name** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 
**middle_name** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 
**last_name** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 
**suffix** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 

## Example

```python
from openapi_client.models.name_score import NameScore

# TODO update the JSON string below
json = "{}"
# create an instance of NameScore from a JSON string
name_score_instance = NameScore.from_json(json)
# print the JSON string representation of the object
print(NameScore.to_json())

# convert the object into a dict
name_score_dict = name_score_instance.to_dict()
# create an instance of NameScore from a dict
name_score_from_dict = NameScore.from_dict(name_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


