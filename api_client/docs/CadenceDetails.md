# CadenceDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **int** | &#x60;postedDate&#x60; of the first deposit transaction | [optional] 
**stop_date** | **int** | &#x60;postedDate&#x60; of the final deposit transaction (omitted if status is active) | [optional] 
**days** | **int** | Number of days between the recurring deposits | [optional] 

## Example

```python
from openapi_client.models.cadence_details import CadenceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CadenceDetails from a JSON string
cadence_details_instance = CadenceDetails.from_json(json)
# print the JSON string representation of the object
print(CadenceDetails.to_json())

# convert the object into a dict
cadence_details_dict = cadence_details_instance.to_dict()
# create an instance of CadenceDetails from a dict
cadence_details_from_dict = CadenceDetails.from_dict(cadence_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


