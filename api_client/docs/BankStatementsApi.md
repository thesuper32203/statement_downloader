# openapi_client.BankStatementsApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_statement_report**](BankStatementsApi.md#generate_statement_report) | **POST** /decisioning/v2/customers/{customerId}/statement | Generate Statement Report for the customer
[**get_customer_account_multiple_statement**](BankStatementsApi.md#get_customer_account_multiple_statement) | **GET** /aggregation/v3/customers/{customerId}/accounts/{accountId}/statement | Get Customer Account Multiple Statement Details
[**get_customer_account_statement**](BankStatementsApi.md#get_customer_account_statement) | **GET** /aggregation/v1/customers/{customerId}/accounts/{accountId}/statement | Get Customer Account Statement


# **generate_statement_report**
> StatementReportAck generate_statement_report(customer_id, statement_report_constraints, callback_url=callback_url)

Generate Statement Report for the customer

Generate a Statement Report for the given accounts under the given customer.

This is a premium service. A billable event will be created upon the successful generation of the Statement Report.

Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.statement_report_ack import StatementReportAck
from openapi_client.models.statement_report_constraints import StatementReportConstraints
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
    api_instance = openapi_client.BankStatementsApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    statement_report_constraints = openapi_client.StatementReportConstraints() # StatementReportConstraints | 
    callback_url = 'https://finicity-test/webhook' # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    try:
        # Generate Statement Report for the customer
        api_response = api_instance.generate_statement_report(customer_id, statement_report_constraints, callback_url=callback_url)
        print("The response of BankStatementsApi->generate_statement_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankStatementsApi->generate_statement_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **statement_report_constraints** | [**StatementReportConstraints**](StatementReportConstraints.md)|  | 
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional] 

### Return type

[**StatementReportAck**](StatementReportAck.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The report is being generated. When finished, a notification will be sent to the specified callback URL (Report Listener Service) and the report can be fetched using Get Report APIs. If you don&#39;t use a callback URL, Get Report returns a minimal report with the following status: &#39;inProgress&#39;. Repeat the call every 20 seconds until Get Report returns a different status. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**403** | The active security freeze for this consumer exists. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_account_multiple_statement**
> CustomerAccountMultipleStatements get_customer_account_multiple_statement(customer_id, account_id, index=index)

Get Customer Account Multiple Statement Details

This endpoint retrieves details of the account statements available for a given customer (up to a maximum of 24 statements).

Use the asset ID of the statement you are interested in to obtain the statement report using Get Asset by Customer and ID.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.customer_account_multiple_statements import CustomerAccountMultipleStatements
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
    api_instance = openapi_client.BankStatementsApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID
    index = '1' # str | Request details of statements with comma-separated indexes between 1-24. The default value is 1 which will return details of the most recent statement. Increasing the index will return details of older statements, for example, setting the index value to 6 will return data on the sixth most recent statement. (optional) (default to '1')

    try:
        # Get Customer Account Multiple Statement Details
        api_response = api_instance.get_customer_account_multiple_statement(customer_id, account_id, index=index)
        print("The response of BankStatementsApi->get_customer_account_multiple_statement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankStatementsApi->get_customer_account_multiple_statement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 
 **index** | **str**| Request details of statements with comma-separated indexes between 1-24. The default value is 1 which will return details of the most recent statement. Increasing the index will return details of older statements, for example, setting the index value to 6 will return data on the sixth most recent statement. | [optional] [default to &#39;1&#39;]

### Return type

[**CustomerAccountMultipleStatements**](CustomerAccountMultipleStatements.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The account statements were successfully retrieved. |  -  |
**203** | The request was unsuccessful due to a required Multi-Factor Authentication (MFA) challenge. There is no further action that can be taken to resolve this error. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_account_statement**
> bytearray get_customer_account_statement(customer_id, account_id, index=index, type=type)

Get Customer Account Statement

Retrieve the customer's bank statements in PDF format. Up to 24 months of history is available depending on the financial institution. Since this is a premium service, charges incur per each successful statement retrieved.

For certified financial institutions, statements are available for the following account types:
* Checking
* Savings
* Money market
* CDs
* Investments
* Mortgage
* Credit cards
* Loans
* Line of credit
* Student Loans

Note: setting the timeout to 180 seconds is recommended to allow enough time for a response.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
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
    api_instance = openapi_client.BankStatementsApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID
    index = 1 # int | Request statements from 1-24. By default, 1 is the most recent statement. Increase the index value to count back (by month) and retrieve its most recent statement. (optional) (default to 1)
    type = 'taxStatement' # str | The type of statement to retrieve (optional)

    try:
        # Get Customer Account Statement
        api_response = api_instance.get_customer_account_statement(customer_id, account_id, index=index, type=type)
        print("The response of BankStatementsApi->get_customer_account_statement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankStatementsApi->get_customer_account_statement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 
 **index** | **int**| Request statements from 1-24. By default, 1 is the most recent statement. Increase the index value to count back (by month) and retrieve its most recent statement. | [optional] [default to 1]
 **type** | **str**| The type of statement to retrieve | [optional] 

### Return type

**bytearray**

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The statement was successfully downloaded as a PDF file |  -  |
**203** | The request was unsuccessful due to a required Multi-Factor Authentication (MFA) challenge. There is no further action that can be taken to resolve this error. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

