# Birthday

A birth date

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | The birthday 4-digit year | [optional] 
**month** | **int** | The birthday 2-digit month (1 is January) | [optional] 
**day_of_month** | **int** | The birthday 2-digit day-of-month | [optional] 

## Example

```python
from openapi_client.models.birthday import Birthday

# TODO update the JSON string below
json = "{}"
# create an instance of Birthday from a JSON string
birthday_instance = Birthday.from_json(json)
# print the JSON string representation of the object
print(Birthday.to_json())

# convert the object into a dict
birthday_dict = birthday_instance.to_dict()
# create an instance of Birthday from a dict
birthday_from_dict = Birthday.from_dict(birthday_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


