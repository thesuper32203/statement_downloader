# AddressScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_address** | **int** | This score represent the matching between user input \&quot;addresss\&quot; sub-attributes (line1,line2, line3, city, state, country, postalCode) with the account owner details fetch ownerAddress | [optional] 
**type** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 
**line1** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 
**line2** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 
**line3** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 
**city** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 
**country** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 
**postal_code** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 
**state** | **int** | This score represent the matching between user input with the account owner details fetch | [optional] 

## Example

```python
from openapi_client.models.address_score import AddressScore

# TODO update the JSON string below
json = "{}"
# create an instance of AddressScore from a JSON string
address_score_instance = AddressScore.from_json(json)
# print the JSON string representation of the object
print(AddressScore.to_json())

# convert the object into a dict
address_score_dict = address_score_instance.to_dict()
# create an instance of AddressScore from a dict
address_score_from_dict = AddressScore.from_dict(address_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


