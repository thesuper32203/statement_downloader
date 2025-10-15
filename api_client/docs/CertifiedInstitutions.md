# CertifiedInstitutions

A list of financial institutions from the Get Certified Institutions API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found** | **int** | The total number of results matching search criteria | 
**displaying** | **int** | The number of results returned | 
**more_available** | **bool** | If the value of &#x60;moreAvailable&#x60; is \&quot;true\&quot;, you can retrieve the next page of results by increasing the value of the start parameter in your next request:\&quot;...&amp;start&#x3D;6&amp;limit&#x3D;5\&quot; | 
**requested_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**institutions** | [**List[CertifiedInstitution]**](CertifiedInstitution.md) | A list of institutions | 

## Example

```python
from openapi_client.models.certified_institutions import CertifiedInstitutions

# TODO update the JSON string below
json = "{}"
# create an instance of CertifiedInstitutions from a JSON string
certified_institutions_instance = CertifiedInstitutions.from_json(json)
# print the JSON string representation of the object
print(CertifiedInstitutions.to_json())

# convert the object into a dict
certified_institutions_dict = certified_institutions_instance.to_dict()
# create an instance of CertifiedInstitutions from a dict
certified_institutions_from_dict = CertifiedInstitutions.from_dict(certified_institutions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


