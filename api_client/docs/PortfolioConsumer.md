# PortfolioConsumer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A consumer ID. See Create Consumer API for how to create a consumer ID. | 
**first_name** | **str** | The first name of the account holder | 
**last_name** | **str** | The last name of the account holder | 
**customer_id** | **int** | A customer ID represented as a number. See Add Customer API for how to create a customer ID. | 
**ssn** | **str** | A full SSN with or without hyphens | 
**birthday** | [**Birthday**](Birthday.md) |  | 
**suffix** | **str** | A generational or academic suffix | [optional] 

## Example

```python
from openapi_client.models.portfolio_consumer import PortfolioConsumer

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioConsumer from a JSON string
portfolio_consumer_instance = PortfolioConsumer.from_json(json)
# print the JSON string representation of the object
print(PortfolioConsumer.to_json())

# convert the object into a dict
portfolio_consumer_dict = portfolio_consumer_instance.to_dict()
# create an instance of PortfolioConsumer from a dict
portfolio_consumer_from_dict = PortfolioConsumer.from_dict(portfolio_consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


