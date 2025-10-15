# openapi_client.PaymentSuccessIndicatorApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_fcra_payment_success_indicators**](PaymentSuccessIndicatorApi.md#generate_fcra_payment_success_indicators) | **POST** /payments/customers/{customerId}/accounts/{accountId}/fcra-payment-success-indicators | Generate FCRA Payment Success Indicators
[**generate_payment_success_indicators**](PaymentSuccessIndicatorApi.md#generate_payment_success_indicators) | **POST** /payments/customers/{customerId}/accounts/{accountId}/payment-success-indicators | Generate Non-FCRA Payment Success Indicators
[**get_fcra_payment_success_indicator**](PaymentSuccessIndicatorApi.md#get_fcra_payment_success_indicator) | **GET** /aggregation/v1/customers/{customerId}/accounts/{accountId}/payments/paymentIndicator/fcra | Get FCRA Payment Success Indicator (Legacy)
[**get_fcra_payment_success_indicators**](PaymentSuccessIndicatorApi.md#get_fcra_payment_success_indicators) | **GET** /payments/customers/{customerId}/accounts/{accountId}/fcra-payment-success-indicators/{payRequestId} | Get FCRA Payment Success Indicators by Pay Request ID
[**get_payment_success_indicator**](PaymentSuccessIndicatorApi.md#get_payment_success_indicator) | **GET** /aggregation/v2/customers/{customerId}/accounts/{accountId}/payments/paymentIndicator | Get Non-FCRA Payment Success Indicator (Legacy)
[**get_payment_success_indicators**](PaymentSuccessIndicatorApi.md#get_payment_success_indicators) | **GET** /payments/customers/{customerId}/accounts/{accountId}/payment-success-indicators/{payRequestId} | Get Non-FCRA Payment Success Indicators by Pay Request ID


# **generate_fcra_payment_success_indicators**
> PaymentSuccessIndicators generate_fcra_payment_success_indicators(customer_id, account_id, payment_success_indicators_properties, purpose=purpose)

Generate FCRA Payment Success Indicators

Payment Success Indicator (PSI) allows the user to evaluate the likelihood of a specific ACH transaction resulting in either an insufficient funds return (NSF) or an unauthorized return due to first- or third-party fraud. PSI is powered by a machine learning model trained on consumer-permissioned data. PSI provides a risk assessment, which includes a real-time balance check, predictive risk scores forecasting a consumer’s likelihood of having sufficient funds over a 10-day period, a real-time score predicting the likelihood of an unauthorized return, and risk attributes to explain and enhance decisioning. Provision and use of this report is subject to all applicable obligations of the FCRA and any applicable analogous state law. This product may only be used for the stated permissible purpose under the FCRA.
_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.payment_success_indicators import PaymentSuccessIndicators
from openapi_client.models.payment_success_indicators_properties import PaymentSuccessIndicatorsProperties
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
    api_instance = openapi_client.PaymentSuccessIndicatorApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID
    payment_success_indicators_properties = openapi_client.PaymentSuccessIndicatorsProperties() # PaymentSuccessIndicatorsProperties | 
    purpose = '3F' # str | 2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports. (optional)

    try:
        # Generate FCRA Payment Success Indicators
        api_response = api_instance.generate_fcra_payment_success_indicators(customer_id, account_id, payment_success_indicators_properties, purpose=purpose)
        print("The response of PaymentSuccessIndicatorApi->generate_fcra_payment_success_indicators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentSuccessIndicatorApi->generate_fcra_payment_success_indicators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 
 **payment_success_indicators_properties** | [**PaymentSuccessIndicatorsProperties**](PaymentSuccessIndicatorsProperties.md)|  | 
 **purpose** | **str**| 2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports. | [optional] 

### Return type

[**PaymentSuccessIndicators**](PaymentSuccessIndicators.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successfully requested to generate a Payment Success Indicators score |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**403** | Forbidden |  -  |
**404** | The resource doesn&#39;t exist |  -  |
**406** | Not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_payment_success_indicators**
> PaymentSuccessIndicators generate_payment_success_indicators(customer_id, account_id, payment_success_indicators_properties)

Generate Non-FCRA Payment Success Indicators

Payment Success Indicator (PSI) allows the user to evaluate the likelihood of a specific ACH transaction resulting in either an insufficient funds return (NSF) or an unauthorized return due to first- or third-party fraud. PSI is powered by a machine learning model trained on consumer-permissioned data. PSI provides a risk assessment, which includes a real-time balance check, predictive risk scores forecasting a consumer’s likelihood of having sufficient funds over a 10-day period, a real-time score predicting the likelihood of an unauthorized return, and risk attributes to explain and enhance decisioning. This product may not be used for uses subject to the FCRA.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.payment_success_indicators import PaymentSuccessIndicators
from openapi_client.models.payment_success_indicators_properties import PaymentSuccessIndicatorsProperties
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
    api_instance = openapi_client.PaymentSuccessIndicatorApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID
    payment_success_indicators_properties = openapi_client.PaymentSuccessIndicatorsProperties() # PaymentSuccessIndicatorsProperties | 

    try:
        # Generate Non-FCRA Payment Success Indicators
        api_response = api_instance.generate_payment_success_indicators(customer_id, account_id, payment_success_indicators_properties)
        print("The response of PaymentSuccessIndicatorApi->generate_payment_success_indicators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentSuccessIndicatorApi->generate_payment_success_indicators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 
 **payment_success_indicators_properties** | [**PaymentSuccessIndicatorsProperties**](PaymentSuccessIndicatorsProperties.md)|  | 

### Return type

[**PaymentSuccessIndicators**](PaymentSuccessIndicators.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successfully requested to generate a Payment Success Indicators score |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**403** | Forbidden |  -  |
**404** | The resource doesn&#39;t exist |  -  |
**406** | Not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fcra_payment_success_indicator**
> PaymentSuccessIndicator get_fcra_payment_success_indicator(customer_id, account_id, settlement_amount, settle_by_date, purpose_code)

Get FCRA Payment Success Indicator (Legacy)

Payment Success Indicator (PSI) allows the user to evaluate the likelihood of a specific ACH transaction resulting in an insufficient funds return (NSF). PSI is powered by a machine learning model trained on Finicity’s consumer-permissioned data network. PSI provides a risk assessment, which includes a real-time balance check, a predictive risk score for the up to the next 9 days, and 8 risk attributes to explain and enhance decisioning. Provision and use of this report is subject to all applicable obligations of the FCRA and any applicable analogous state law. This product may only be used for the stated permissible purpose under the FCRA.


 _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.payment_success_indicator import PaymentSuccessIndicator
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
    api_instance = openapi_client.PaymentSuccessIndicatorApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID
    settlement_amount = 10.05 # float | The transaction amount in USD $.
    settle_by_date = '2023-03-30' # date | The expected date that the funds, from the consumer’s account, will be moved to the receiving account.  `settleByDate` in ISO 8601 date format (YYYY-MM-DD). `settleByDate` dictates the number of days the model responds with. The response can range from 3-10 days, including `day0`. Details explained below: 1. If `settleByDate` is 9 or more days out from today, the response includes 10 days of data, `day0` through `day9`. 2. If `settleByDate` is between 3 and 8 days out from today, the response includes 4-9 days of data, `day3-8`. 3. If `settleByDate` is between today and 2 days out from today, the response includes 3 days of data, `day0` through `day2`.
    purpose_code = 'purpose_code_example' # str | The 2-digit code (1P) assigned to indicate the intended purpose. 1P represents the following permissible purpose: “Determine whether a consumers payment method may be accepted or authorized”, which falls under the “Legitimate Business Need” permissible purpose under section 604 of the FCRA.

    try:
        # Get FCRA Payment Success Indicator (Legacy)
        api_response = api_instance.get_fcra_payment_success_indicator(customer_id, account_id, settlement_amount, settle_by_date, purpose_code)
        print("The response of PaymentSuccessIndicatorApi->get_fcra_payment_success_indicator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentSuccessIndicatorApi->get_fcra_payment_success_indicator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 
 **settlement_amount** | **float**| The transaction amount in USD $. | 
 **settle_by_date** | **date**| The expected date that the funds, from the consumer’s account, will be moved to the receiving account.  &#x60;settleByDate&#x60; in ISO 8601 date format (YYYY-MM-DD). &#x60;settleByDate&#x60; dictates the number of days the model responds with. The response can range from 3-10 days, including &#x60;day0&#x60;. Details explained below: 1. If &#x60;settleByDate&#x60; is 9 or more days out from today, the response includes 10 days of data, &#x60;day0&#x60; through &#x60;day9&#x60;. 2. If &#x60;settleByDate&#x60; is between 3 and 8 days out from today, the response includes 4-9 days of data, &#x60;day3-8&#x60;. 3. If &#x60;settleByDate&#x60; is between today and 2 days out from today, the response includes 3 days of data, &#x60;day0&#x60; through &#x60;day2&#x60;. | 
 **purpose_code** | **str**| The 2-digit code (1P) assigned to indicate the intended purpose. 1P represents the following permissible purpose: “Determine whether a consumers payment method may be accepted or authorized”, which falls under the “Legitimate Business Need” permissible purpose under section 604 of the FCRA. | 

### Return type

[**PaymentSuccessIndicator**](PaymentSuccessIndicator.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The payment success indicator was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | Required details not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fcra_payment_success_indicators**
> FcraPaymentSuccessIndicators get_fcra_payment_success_indicators(customer_id, account_id, pay_request_id, include_reasons=include_reasons)

Get FCRA Payment Success Indicators by Pay Request ID

Get the FCRA Payment Success Indicator scores that have been generated by a previous call to Generate FCRA Payment Success Indicators.
_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.fcra_payment_success_indicators import FcraPaymentSuccessIndicators
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
    api_instance = openapi_client.PaymentSuccessIndicatorApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID
    pay_request_id = '476412776235977427' # str | Unique identifier of the Payments request
    include_reasons = true # bool | If this parameter is true, the reasons codes will be provided in the results. Otherwise, the reasons will be omitted. (optional)

    try:
        # Get FCRA Payment Success Indicators by Pay Request ID
        api_response = api_instance.get_fcra_payment_success_indicators(customer_id, account_id, pay_request_id, include_reasons=include_reasons)
        print("The response of PaymentSuccessIndicatorApi->get_fcra_payment_success_indicators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentSuccessIndicatorApi->get_fcra_payment_success_indicators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 
 **pay_request_id** | **str**| Unique identifier of the Payments request | 
 **include_reasons** | **bool**| If this parameter is true, the reasons codes will be provided in the results. Otherwise, the reasons will be omitted. | [optional] 

### Return type

[**FcraPaymentSuccessIndicators**](FcraPaymentSuccessIndicators.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully requested to retrieve a Payment Success Indicators score |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |
**406** | Not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_success_indicator**
> PaymentSuccessIndicator get_payment_success_indicator(customer_id, account_id, settlement_amount, settle_by_date)

Get Non-FCRA Payment Success Indicator (Legacy)

Payment Success Indicator (PSI) is a Payment Intelligence solution that uses Financial Institution (FI) data to help payment originators evaluate a consumer's ability to pay now and in the future within a given time period. PSI is for payment originators to assess a consumer's real-time FI account balance and historical FI account activities to help minimize ACH declines and enable payment originators to gracefully transition to alternative payment methods or schedules when payment settlement using ACH / Account-based payment is less likely. PSI may not be used for credit or insurance underwriting, employment or rental screening, or any other purpose(s) that would implicate the Fair Credit Reporting Act or other consumer reporting law.


 _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.payment_success_indicator import PaymentSuccessIndicator
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
    api_instance = openapi_client.PaymentSuccessIndicatorApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID
    settlement_amount = 10.05 # float | The transaction amount in USD $.
    settle_by_date = '2023-03-30' # date | The expected date that the funds, from the consumer’s account, will be moved to the receiving account.  `settleByDate` in ISO 8601 date format (YYYY-MM-DD). `settleByDate` dictates the number of days the model responds with. The response can range from 3-10 days, including `day0`. Details explained below: 1. If `settleByDate` is 9 or more days out from today, the response includes 10 days of data, `day0` through `day9`. 2. If `settleByDate` is between 3 and 8 days out from today, the response includes 4-9 days of data, `day3-8`. 3. If `settleByDate` is between today and 2 days out from today, the response includes 3 days of data, `day0` through `day2`.

    try:
        # Get Non-FCRA Payment Success Indicator (Legacy)
        api_response = api_instance.get_payment_success_indicator(customer_id, account_id, settlement_amount, settle_by_date)
        print("The response of PaymentSuccessIndicatorApi->get_payment_success_indicator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentSuccessIndicatorApi->get_payment_success_indicator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 
 **settlement_amount** | **float**| The transaction amount in USD $. | 
 **settle_by_date** | **date**| The expected date that the funds, from the consumer’s account, will be moved to the receiving account.  &#x60;settleByDate&#x60; in ISO 8601 date format (YYYY-MM-DD). &#x60;settleByDate&#x60; dictates the number of days the model responds with. The response can range from 3-10 days, including &#x60;day0&#x60;. Details explained below: 1. If &#x60;settleByDate&#x60; is 9 or more days out from today, the response includes 10 days of data, &#x60;day0&#x60; through &#x60;day9&#x60;. 2. If &#x60;settleByDate&#x60; is between 3 and 8 days out from today, the response includes 4-9 days of data, &#x60;day3-8&#x60;. 3. If &#x60;settleByDate&#x60; is between today and 2 days out from today, the response includes 3 days of data, &#x60;day0&#x60; through &#x60;day2&#x60;. | 

### Return type

[**PaymentSuccessIndicator**](PaymentSuccessIndicator.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The payment success indicator was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | Required details not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_success_indicators**
> PaymentSuccessIndicators get_payment_success_indicators(customer_id, account_id, pay_request_id, include_reasons=include_reasons)

Get Non-FCRA Payment Success Indicators by Pay Request ID

Get the Non-FCRA Payment Success Indicator scores that have been generated by a previous call to Generate Payment Success Indicators.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.payment_success_indicators import PaymentSuccessIndicators
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
    api_instance = openapi_client.PaymentSuccessIndicatorApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID
    pay_request_id = '476412776235977427' # str | Unique identifier of the Payments request
    include_reasons = true # bool | If this parameter is true, the reasons codes will be provided in the results. Otherwise, the reasons will be omitted. (optional)

    try:
        # Get Non-FCRA Payment Success Indicators by Pay Request ID
        api_response = api_instance.get_payment_success_indicators(customer_id, account_id, pay_request_id, include_reasons=include_reasons)
        print("The response of PaymentSuccessIndicatorApi->get_payment_success_indicators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentSuccessIndicatorApi->get_payment_success_indicators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 
 **pay_request_id** | **str**| Unique identifier of the Payments request | 
 **include_reasons** | **bool**| If this parameter is true, the reasons codes will be provided in the results. Otherwise, the reasons will be omitted. | [optional] 

### Return type

[**PaymentSuccessIndicators**](PaymentSuccessIndicators.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully requested to retrieve a Payment Success Indicators score |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |
**406** | Not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

