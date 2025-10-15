# openapi_client.PortfoliosApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_portfolio_by_consumer**](PortfoliosApi.md#get_portfolio_by_consumer) | **GET** /decisioning/v1/consumers/{consumerId}/portfolios/{portfolioId} | Get Portfolio by Consumer and Portfolio
[**get_portfolio_by_customer**](PortfoliosApi.md#get_portfolio_by_customer) | **GET** /decisioning/v1/customers/{customerId}/portfolios/{portfolioId} | Get Portfolio by Customer and Portfolio


# **get_portfolio_by_consumer**
> PortfolioWithConsumerSummary get_portfolio_by_consumer(consumer_id, portfolio_id)

Get Portfolio by Consumer and Portfolio

Return a portfolio of most recently generated reports for each report type for a given consumer. If there are multiple reports that were generated for a report type (VOA, VOI, etc.), only the most recently generated report for the type will be returned.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.portfolio_with_consumer_summary import PortfolioWithConsumerSummary
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PortfoliosApi(api_client)
    consumer_id = '0bf46322c167b562e6cbed9d40e19a4c' # str | The consumer ID
    portfolio_id = 'y4zsgccj4xpw-6-port' # str | A portfolio ID with the portfolio version number. Using the portfolio number without a version number will return the most recently generated reports.

    try:
        # Get Portfolio by Consumer and Portfolio
        api_response = api_instance.get_portfolio_by_consumer(consumer_id, portfolio_id)
        print("The response of PortfoliosApi->get_portfolio_by_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolio_by_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| The consumer ID | 
 **portfolio_id** | **str**| A portfolio ID with the portfolio version number. Using the portfolio number without a version number will return the most recently generated reports. | 

### Return type

[**PortfolioWithConsumerSummary**](PortfolioWithConsumerSummary.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolio was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**403** | The active security freeze for this consumer exists. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_by_customer**
> PortfolioSummary get_portfolio_by_customer(customer_id, portfolio_id)

Get Portfolio by Customer and Portfolio

Return a portfolio of most recently generated reports for each report type for the given customer. If there are multiple reports that were generated for a report type (VOA, VOI, etc.), only the most recently generated report for the type will be returned.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)


### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.portfolio_summary import PortfolioSummary
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PortfoliosApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    portfolio_id = 'y4zsgccj4xpw-6-port' # str | A portfolio ID with the portfolio version number. Using the portfolio number without a version number will return the most recently generated reports.

    try:
        # Get Portfolio by Customer and Portfolio
        api_response = api_instance.get_portfolio_by_customer(customer_id, portfolio_id)
        print("The response of PortfoliosApi->get_portfolio_by_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolio_by_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **portfolio_id** | **str**| A portfolio ID with the portfolio version number. Using the portfolio number without a version number will return the most recently generated reports. | 

### Return type

[**PortfolioSummary**](PortfolioSummary.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolio was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**403** | The active security freeze for this consumer exists. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

