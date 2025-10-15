# openapi_client.VerifyIncomeAndEmploymentApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_pay_statement_report**](VerifyIncomeAndEmploymentApi.md#generate_pay_statement_report) | **POST** /decisioning/v2/customers/{customerId}/payStatement | Generate Pay Statement Report for the customer
[**generate_voe_payroll_report**](VerifyIncomeAndEmploymentApi.md#generate_voe_payroll_report) | **POST** /decisioning/v2/customers/{customerId}/voePayroll | Generate VOE - Payroll Report for the customer
[**generate_voe_transactions_report**](VerifyIncomeAndEmploymentApi.md#generate_voe_transactions_report) | **POST** /decisioning/v2/customers/{customerId}/voeTransactions | Generate VOE - Transactions Report for the customer
[**generate_voi_report**](VerifyIncomeAndEmploymentApi.md#generate_voi_report) | **POST** /decisioning/v2/customers/{customerId}/voi | Generate VOI Report for the customer
[**generate_voie_paystub_report**](VerifyIncomeAndEmploymentApi.md#generate_voie_paystub_report) | **POST** /decisioning/v2/customers/{customerId}/voieTxVerify/withStatement | Generate VOIE - Paystub Report for the customer
[**generate_voie_paystub_with_tx_verify_report**](VerifyIncomeAndEmploymentApi.md#generate_voie_paystub_with_tx_verify_report) | **POST** /decisioning/v2/customers/{customerId}/voieTxVerify/withInterview | Generate VOIE Paystub (with TXVerify) Report for the customer
[**refresh_voie_payroll_report**](VerifyIncomeAndEmploymentApi.md#refresh_voie_payroll_report) | **POST** /decisioning/v2/customers/{customerId}/voiePayroll | Generate VOIE - Payroll Report for the customer


# **generate_pay_statement_report**
> PayStatementReportAck generate_pay_statement_report(customer_id, pay_statement_report_constraints, callback_url=callback_url)

Generate Pay Statement Report for the customer

Generate Pay Statement Extraction Report for the given customer. This service accepts asset IDs of the stored pay statements to generate a Pay Statement Extraction Report.

This is a premium service. The billing rate is the variable rate for Pay Statement Extraction Report under the current subscription plan. The billable event is the successful generation of a Pay Statement Extraction Report.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.pay_statement_report_ack import PayStatementReportAck
from openapi_client.models.pay_statement_report_constraints import PayStatementReportConstraints
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
    api_instance = openapi_client.VerifyIncomeAndEmploymentApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    pay_statement_report_constraints = openapi_client.PayStatementReportConstraints() # PayStatementReportConstraints | 
    callback_url = 'https://finicity-test/webhook' # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    try:
        # Generate Pay Statement Report for the customer
        api_response = api_instance.generate_pay_statement_report(customer_id, pay_statement_report_constraints, callback_url=callback_url)
        print("The response of VerifyIncomeAndEmploymentApi->generate_pay_statement_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerifyIncomeAndEmploymentApi->generate_pay_statement_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **pay_statement_report_constraints** | [**PayStatementReportConstraints**](PayStatementReportConstraints.md)|  | 
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional] 

### Return type

[**PayStatementReportAck**](PayStatementReportAck.md)

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

# **generate_voe_payroll_report**
> PayrollReportAck generate_voe_payroll_report(customer_id, payroll_report_constraints, callback_url=callback_url)

Generate VOE - Payroll Report for the customer

Generate or refresh a VOE - Payroll report. Often used as a complementary report to the VOIE-Payroll report to fulfill the pre-close VOE requirements. It retrieves the customer's employment details and employment status through the payroll source without any income information.

This is a premium service. The billable event is the successful generation of a VOE - Payroll report.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.payroll_report_ack import PayrollReportAck
from openapi_client.models.payroll_report_constraints import PayrollReportConstraints
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
    api_instance = openapi_client.VerifyIncomeAndEmploymentApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    payroll_report_constraints = openapi_client.PayrollReportConstraints() # PayrollReportConstraints | 
    callback_url = 'https://finicity-test/webhook' # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    try:
        # Generate VOE - Payroll Report for the customer
        api_response = api_instance.generate_voe_payroll_report(customer_id, payroll_report_constraints, callback_url=callback_url)
        print("The response of VerifyIncomeAndEmploymentApi->generate_voe_payroll_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerifyIncomeAndEmploymentApi->generate_voe_payroll_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **payroll_report_constraints** | [**PayrollReportConstraints**](PayrollReportConstraints.md)|  | 
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional] 

### Return type

[**PayrollReportAck**](PayrollReportAck.md)

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

# **generate_voe_transactions_report**
> VOETransactionsReportAck generate_voe_transactions_report(customer_id, voe_transactions_report_constraints, callback_url=callback_url)

Generate VOE - Transactions Report for the customer

Premium Service: A billable event when the API response is successful.

MVS-Direct integration developers only.

Used as a complimentary report to the VOA with Income and VOIE - Paystub (with TXVerify) reports and used to fulfill the pre-close VOE requirements.

Retrieve the latest credit transaction information from the borrower's connected bank accounts and groups them into income streams so that you can view their payment history to ensure a direct deport was made within the expected cadence. The report displays transaction descriptions without any dollar amounts so that income re-verification isn't necessary.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.voe_transactions_report_ack import VOETransactionsReportAck
from openapi_client.models.voe_transactions_report_constraints import VOETransactionsReportConstraints
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
    api_instance = openapi_client.VerifyIncomeAndEmploymentApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    voe_transactions_report_constraints = openapi_client.VOETransactionsReportConstraints() # VOETransactionsReportConstraints | 
    callback_url = 'https://finicity-test/webhook' # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    try:
        # Generate VOE - Transactions Report for the customer
        api_response = api_instance.generate_voe_transactions_report(customer_id, voe_transactions_report_constraints, callback_url=callback_url)
        print("The response of VerifyIncomeAndEmploymentApi->generate_voe_transactions_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerifyIncomeAndEmploymentApi->generate_voe_transactions_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **voe_transactions_report_constraints** | [**VOETransactionsReportConstraints**](VOETransactionsReportConstraints.md)|  | 
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional] 

### Return type

[**VOETransactionsReportAck**](VOETransactionsReportAck.md)

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

# **generate_voi_report**
> VOIReportAck generate_voi_report(customer_id, voi_report_constraints, callback_url=callback_url)

Generate VOI Report for the customer

Generate a Verification of Income (VOI) report for all checking, savings, and money market accounts for the given customer. This service retrieves up to two years of transaction history for each account and uses this information to generate the VOI report.

This is a premium service. The billing rate is the variable rate for Verification of Income under the current subscription plan. The billable event is the successful generation of a VOI report.

If no account of type checking, savings, or money market is found, the service will return HTTP 400 Bad Request.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.voi_report_ack import VOIReportAck
from openapi_client.models.voi_report_constraints import VOIReportConstraints
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
    api_instance = openapi_client.VerifyIncomeAndEmploymentApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    voi_report_constraints = openapi_client.VOIReportConstraints() # VOIReportConstraints | 
    callback_url = 'https://finicity-test/webhook' # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    try:
        # Generate VOI Report for the customer
        api_response = api_instance.generate_voi_report(customer_id, voi_report_constraints, callback_url=callback_url)
        print("The response of VerifyIncomeAndEmploymentApi->generate_voi_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerifyIncomeAndEmploymentApi->generate_voi_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **voi_report_constraints** | [**VOIReportConstraints**](VOIReportConstraints.md)|  | 
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional] 

### Return type

[**VOIReportAck**](VOIReportAck.md)

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

# **generate_voie_paystub_report**
> VOIEPaystubReportAck generate_voie_paystub_report(customer_id, voie_report_constraints, callback_url=callback_url)

Generate VOIE - Paystub Report for the customer

Generate a VOIE - Paystub report. This service uses the provided paystub(s), which are passed into the request body as asset IDs (generated using the Store Customer Pay Statement API) to generate the VOIE - Paystub report with digitized paystub details.

This is a premium service. The billing rate is the variable rate for VOIE - Paystub under the current subscription plan. The billable event is the successful generation of a VOIE - Paystub Report.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.voie_paystub_report_ack import VOIEPaystubReportAck
from openapi_client.models.voie_report_constraints import VOIEReportConstraints
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
    api_instance = openapi_client.VerifyIncomeAndEmploymentApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    voie_report_constraints = openapi_client.VOIEReportConstraints() # VOIEReportConstraints | 
    callback_url = 'https://finicity-test/webhook' # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    try:
        # Generate VOIE - Paystub Report for the customer
        api_response = api_instance.generate_voie_paystub_report(customer_id, voie_report_constraints, callback_url=callback_url)
        print("The response of VerifyIncomeAndEmploymentApi->generate_voie_paystub_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerifyIncomeAndEmploymentApi->generate_voie_paystub_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **voie_report_constraints** | [**VOIEReportConstraints**](VOIEReportConstraints.md)|  | 
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional] 

### Return type

[**VOIEPaystubReportAck**](VOIEPaystubReportAck.md)

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

# **generate_voie_paystub_with_tx_verify_report**
> VOIEPaystubWithTXVerifyReportAck generate_voie_paystub_with_tx_verify_report(customer_id, voie_with_tx_verify_report_constraints, callback_url=callback_url)

Generate VOIE Paystub (with TXVerify) Report for the customer

Generate a VOIE - Paystub (with TXVerify) report for all checking and savings under the given customer. This service retrieves up to two years of transaction history for the given accounts. It then uses this information as well as the provided paystub(s), which are passed into the request body as asset IDs (generated using the Store Customer Pay Statement API) to generate the VOIE - Paystub (with TXVerify) report.

Note: if you are using this API to refresh the bank transactions, use the same asset ID from the first report. A new paystub is not required unless the paystub is too old for underwriting requirements. Using the same asset ID that was on the original report and the previously extracted details will be used to speed up report generation response time.

This is a premium service. The billing rate is the variable rate for VOIE TXVerify under the current subscription plan. The billable event is the successful generation of a VOIE TXVerify Report.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.voie_paystub_with_tx_verify_report_ack import VOIEPaystubWithTXVerifyReportAck
from openapi_client.models.voie_with_tx_verify_report_constraints import VOIEWithTXVerifyReportConstraints
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
    api_instance = openapi_client.VerifyIncomeAndEmploymentApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    voie_with_tx_verify_report_constraints = openapi_client.VOIEWithTXVerifyReportConstraints() # VOIEWithTXVerifyReportConstraints | 
    callback_url = 'https://finicity-test/webhook' # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    try:
        # Generate VOIE Paystub (with TXVerify) Report for the customer
        api_response = api_instance.generate_voie_paystub_with_tx_verify_report(customer_id, voie_with_tx_verify_report_constraints, callback_url=callback_url)
        print("The response of VerifyIncomeAndEmploymentApi->generate_voie_paystub_with_tx_verify_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerifyIncomeAndEmploymentApi->generate_voie_paystub_with_tx_verify_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **voie_with_tx_verify_report_constraints** | [**VOIEWithTXVerifyReportConstraints**](VOIEWithTXVerifyReportConstraints.md)|  | 
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional] 

### Return type

[**VOIEPaystubWithTXVerifyReportAck**](VOIEPaystubWithTXVerifyReportAck.md)

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

# **refresh_voie_payroll_report**
> PayrollReportAck refresh_voie_payroll_report(customer_id, payroll_report_constraints, callback_url=callback_url)

Generate VOIE - Payroll Report for the customer

Generate or refresh a VOIE - Payroll report. For clients using the product via a consumer permissioning experience via Data Connect, the original VOIE - Payroll report generates when the consumer completes the Data Connect experience, and this API is only used for future report refreshes without reengaging the consumer.

This is a premium service. The billable event is the successful generation of a VOIE - Payroll report.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.payroll_report_ack import PayrollReportAck
from openapi_client.models.payroll_report_constraints import PayrollReportConstraints
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
    api_instance = openapi_client.VerifyIncomeAndEmploymentApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    payroll_report_constraints = openapi_client.PayrollReportConstraints() # PayrollReportConstraints | 
    callback_url = 'https://finicity-test/webhook' # str | A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. (optional)

    try:
        # Generate VOIE - Payroll Report for the customer
        api_response = api_instance.refresh_voie_payroll_report(customer_id, payroll_report_constraints, callback_url=callback_url)
        print("The response of VerifyIncomeAndEmploymentApi->refresh_voie_payroll_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerifyIncomeAndEmploymentApi->refresh_voie_payroll_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **payroll_report_constraints** | [**PayrollReportConstraints**](PayrollReportConstraints.md)|  | 
 **callback_url** | **str**| A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code. | [optional] 

### Return type

[**PayrollReportAck**](PayrollReportAck.md)

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

