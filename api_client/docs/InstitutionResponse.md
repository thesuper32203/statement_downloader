# InstitutionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found** | **int** | The total number of results matching search criteria | [optional] 
**displaying** | **int** | The number of results returned | [optional] 
**more_available** | **bool** | If the value of &#x60;moreAvailable&#x60; is \&quot;true\&quot;, you can retrieve the next page of results by increasing the value of the start parameter in your next request:\&quot;...&amp;start&#x3D;6&amp;limit&#x3D;5\&quot; | [optional] 
**institutions** | [**List[FinancialInstitution]**](FinancialInstitution.md) | List of institution details for an application | [optional] 

## Example

```python
from openapi_client.models.institution_response import InstitutionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionResponse from a JSON string
institution_response_instance = InstitutionResponse.from_json(json)
# print the JSON string representation of the object
print(InstitutionResponse.to_json())

# convert the object into a dict
institution_response_dict = institution_response_instance.to_dict()
# create an instance of InstitutionResponse from a dict
institution_response_from_dict = InstitutionResponse.from_dict(institution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


