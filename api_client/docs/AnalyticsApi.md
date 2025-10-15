# openapi_client.AnalyticsApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_foresight_analytics_non_cra_report**](AnalyticsApi.md#generate_foresight_analytics_non_cra_report) | **POST** /decisioning/customers/{customerId}/reports/foresight-analytics/userTypes/{userType} | Generate foresight analytics non-CRA report for the customer - Personal


# **generate_foresight_analytics_non_cra_report**
> AnalyticsReportAck generate_foresight_analytics_non_cra_report(customer_id, user_type, foresight_analytics_report_constraints, callback_url=callback_url)

Generate foresight analytics non-CRA report for the customer - Personal

Generate a foresight analytics non-CRA report for a given customer. The report includes benchmarking and forecasting data for a customer based on inputs of account and transaction data as permitted by the customer, and segments (e.g., postal code) provided by the partner. A consumer is not required to generate this report.

If no account type of checking, credit card, or savings is found, the service will return an HTTP 400 Bad Request.

This is a premium service, billable per every successful API call for non-testing customers. A successful call to this API will generate a foresight analytics report which can be retrieved via Get Report by Customer.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.analytics_report_ack import AnalyticsReportAck
from openapi_client.models.foresight_analytics_report_constraints import ForesightAnalyticsReportConstraints
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
    api_instance = openapi_client.AnalyticsApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    user_type = 'personal' # str | UserType indicates if the request is for a personal use case, Allowed values: personal.
    foresight_analytics_report_constraints = openapi_client.ForesightAnalyticsReportConstraints() # ForesightAnalyticsReportConstraints | 
    callback_url = 'https://finicity-test/webhook' # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    try:
        # Generate foresight analytics non-CRA report for the customer - Personal
        api_response = api_instance.generate_foresight_analytics_non_cra_report(customer_id, user_type, foresight_analytics_report_constraints, callback_url=callback_url)
        print("The response of AnalyticsApi->generate_foresight_analytics_non_cra_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->generate_foresight_analytics_non_cra_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **user_type** | **str**| UserType indicates if the request is for a personal use case, Allowed values: personal. | 
 **foresight_analytics_report_constraints** | [**ForesightAnalyticsReportConstraints**](ForesightAnalyticsReportConstraints.md)|  | 
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional] 

### Return type

[**AnalyticsReportAck**](AnalyticsReportAck.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The report is being generated. When finished, a notification will be sent to the specified callback URL (Report Listener Service) and the report can be fetched using Get Report APIs. If you don&#39;t use a callback URL, Get Report returns a minimal report with the following status: &#39;inProgress&#39;. Repeat the call every 20 seconds until Get Report returns a different status. |  * Location - Please Check the Report status at URL /decisioning/v3/customers/{customer_id}/reports/{report_id} <br>  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**403** | The active security freeze for this consumer exists. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

