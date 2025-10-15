# AppStatuses

The response for the Get App Registration Status API returns an array of status objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_records** | **int** | The total number of results | 
**total_pages** | **int** | The total number of pages | 
**page_number** | **int** | The current page number | 
**number_of_records_per_page** | **int** | The number of results per page | 
**applications** | [**List[AppStatus]**](AppStatus.md) | A list of applications with their statuses | 

## Example

```python
from openapi_client.models.app_statuses import AppStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of AppStatuses from a JSON string
app_statuses_instance = AppStatuses.from_json(json)
# print the JSON string representation of the object
print(AppStatuses.to_json())

# convert the object into a dict
app_statuses_dict = app_statuses_instance.to_dict()
# create an instance of AppStatuses from a dict
app_statuses_from_dict = AppStatuses.from_dict(app_statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


