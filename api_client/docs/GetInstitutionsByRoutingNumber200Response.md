# GetInstitutionsByRoutingNumber200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found** | **int** | The total number of results matching search criteria | [optional] 
**displaying** | **int** | The number of results returned | [optional] 
**more_available** | **bool** | If the value of &#x60;moreAvailable&#x60; is \&quot;true\&quot;, you can retrieve the next page of results by increasing the value of the start parameter in your next request:\&quot;...&amp;start&#x3D;6&amp;limit&#x3D;5\&quot; | [optional] 
**created_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**institutions** | [**List[InstitutionsWithRoutingNumber]**](InstitutionsWithRoutingNumber.md) | List of institutions with matching routing numbers | [optional] 

## Example

```python
from openapi_client.models.get_institutions_by_routing_number200_response import GetInstitutionsByRoutingNumber200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetInstitutionsByRoutingNumber200Response from a JSON string
get_institutions_by_routing_number200_response_instance = GetInstitutionsByRoutingNumber200Response.from_json(json)
# print the JSON string representation of the object
print(GetInstitutionsByRoutingNumber200Response.to_json())

# convert the object into a dict
get_institutions_by_routing_number200_response_dict = get_institutions_by_routing_number200_response_instance.to_dict()
# create an instance of GetInstitutionsByRoutingNumber200Response from a dict
get_institutions_by_routing_number200_response_from_dict = GetInstitutionsByRoutingNumber200Response.from_dict(get_institutions_by_routing_number200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


