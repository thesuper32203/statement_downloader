# PortfolioSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | **str** | A unique identifier that will be consistent across all reports created for the same customer | 
**reports** | [**List[PortfolioReport]**](PortfolioReport.md) | A list of reports in the portfolio | 

## Example

```python
from openapi_client.models.portfolio_summary import PortfolioSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioSummary from a JSON string
portfolio_summary_instance = PortfolioSummary.from_json(json)
# print the JSON string representation of the object
print(PortfolioSummary.to_json())

# convert the object into a dict
portfolio_summary_dict = portfolio_summary_instance.to_dict()
# create an instance of PortfolioSummary from a dict
portfolio_summary_from_dict = PortfolioSummary.from_dict(portfolio_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


