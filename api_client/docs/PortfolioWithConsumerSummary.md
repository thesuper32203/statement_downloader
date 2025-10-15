# PortfolioWithConsumerSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | **str** | A unique identifier that will be consistent across all reports created for the same customer | 
**reports** | [**List[PortfolioReport]**](PortfolioReport.md) | A list of reports in the portfolio | 
**consumer** | [**PortfolioConsumer**](PortfolioConsumer.md) |  | 

## Example

```python
from openapi_client.models.portfolio_with_consumer_summary import PortfolioWithConsumerSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioWithConsumerSummary from a JSON string
portfolio_with_consumer_summary_instance = PortfolioWithConsumerSummary.from_json(json)
# print the JSON string representation of the object
print(PortfolioWithConsumerSummary.to_json())

# convert the object into a dict
portfolio_with_consumer_summary_dict = portfolio_with_consumer_summary_instance.to_dict()
# create an instance of PortfolioWithConsumerSummary from a dict
portfolio_with_consumer_summary_from_dict = PortfolioWithConsumerSummary.from_dict(portfolio_with_consumer_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


