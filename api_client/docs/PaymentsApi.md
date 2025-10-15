# openapi_client.PaymentsApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_ach_details**](PaymentsApi.md#get_account_ach_details) | **GET** /aggregation/v1/customers/{customerId}/accounts/{accountId}/details | Get Account ACH Details
[**get_account_owner**](PaymentsApi.md#get_account_owner) | **GET** /aggregation/v1/customers/{customerId}/accounts/{accountId}/owner | Get Account Owner
[**get_account_owner_details**](PaymentsApi.md#get_account_owner_details) | **GET** /aggregation/v3/customers/{customerId}/accounts/{accountId}/owner | Get Account Owner Details
[**get_account_payment_instruction_details**](PaymentsApi.md#get_account_payment_instruction_details) | **GET** /aggregation/v3/customers/{customerId}/accounts/{accountId}/details | Get Account ACH Details with RTP
[**get_available_balance**](PaymentsApi.md#get_available_balance) | **GET** /aggregation/v1/customers/{customerId}/accounts/{accountId}/availableBalance | Get Available Balance - Cached
[**get_available_balance_live**](PaymentsApi.md#get_available_balance_live) | **GET** /aggregation/v1/customers/{customerId}/accounts/{accountId}/availableBalance/live | Get Available Balance
[**get_loan_payment_details**](PaymentsApi.md#get_loan_payment_details) | **GET** /aggregation/v2/customers/{customerId}/accounts/{accountId}/loanDetails | Get Loan Payment Details


# **get_account_ach_details**
> ACHDetails get_account_ach_details(customer_id, account_id)

Get Account ACH Details

Return the real account number and routing number details for an ACH payment.

Note: this is a premium service, billable per every successful API call.

_Supported account types_: "checking", "savings", "moneyMarket","certificateOfDeposit"

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.ach_details import ACHDetails
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
    api_instance = openapi_client.PaymentsApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID

    try:
        # Get Account ACH Details
        api_response = api_instance.get_account_ach_details(customer_id, account_id)
        print("The response of PaymentsApi->get_account_ach_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_account_ach_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 

### Return type

[**ACHDetails**](ACHDetails.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account ACH details were successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_owner**
> AccountOwner get_account_owner(customer_id, account_id)

Get Account Owner

Retrieve the names and addresses of the account owner from a financial institution.

Note: this is a premium service, billable per every successful API call.

This service retrieves account data from the institution. This usually returns quickly, but in some scenarios may take a few minutes to complete. In the event of a timeout condition, retry the call.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.account_owner import AccountOwner
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
    api_instance = openapi_client.PaymentsApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID

    try:
        # Get Account Owner
        api_response = api_instance.get_account_owner(customer_id, account_id)
        print("The response of PaymentsApi->get_account_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_account_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 

### Return type

[**AccountOwner**](AccountOwner.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The account owner was successfully retrieved |  -  |
**203** | The request was unsuccessful due to a required Multi-Factor Authentication (MFA) challenge. There is no further action that can be taken to resolve this error. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_owner_details**
> AccountOwnerHolders get_account_owner_details(customer_id, account_id, with_insights=with_insights, meta_data=meta_data)

Get Account Owner Details

This service retrieves the account details for an account holder from an institution. The following data objects are available.

* Account holders

* Addresses

* Emails

* Phones

* Documentations

* Identity Insights


Note: The data returned varies from institution to institution as not all of them make the same data available. This is a premium service, billable per each successful API call.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.account_owner_holders import AccountOwnerHolders
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
    api_instance = openapi_client.PaymentsApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID
    with_insights = false # bool | If this parameter is true, Identity Insights data will be returned along with the account owner information (optional)
    meta_data = 'program=OBAO' # str | OBAO is a program that is being offered to Mastercard issuers where when the new account is issued a Mastercard Debit or Prepaid account. OBAO offered partners will not be charged for ACH, AOV, and Balance API. (optional)

    try:
        # Get Account Owner Details
        api_response = api_instance.get_account_owner_details(customer_id, account_id, with_insights=with_insights, meta_data=meta_data)
        print("The response of PaymentsApi->get_account_owner_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_account_owner_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 
 **with_insights** | **bool**| If this parameter is true, Identity Insights data will be returned along with the account owner information | [optional] 
 **meta_data** | **str**| OBAO is a program that is being offered to Mastercard issuers where when the new account is issued a Mastercard Debit or Prepaid account. OBAO offered partners will not be charged for ACH, AOV, and Balance API. | [optional] 

### Return type

[**AccountOwnerHolders**](AccountOwnerHolders.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The account owner was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_payment_instruction_details**
> PaymentInstructions get_account_payment_instruction_details(customer_id, account_id)

Get Account ACH Details with RTP

Return the real account number and routing number details for an ACH payment along with the supported payment instruction details. If the RTP (Real Time Payment) value for “transferInEnabled” is true, then the account can receive RTPs. If the value for “transferOutEnabled” is true, then the account can send RTPs

Note: this is a premium service, billable per every successful API call.

_Supported account types_: "checking", "savings", "moneyMarket"

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.payment_instructions import PaymentInstructions
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
    api_instance = openapi_client.PaymentsApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID

    try:
        # Get Account ACH Details with RTP
        api_response = api_instance.get_account_payment_instruction_details(customer_id, account_id)
        print("The response of PaymentsApi->get_account_payment_instruction_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_account_payment_instruction_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 

### Return type

[**PaymentInstructions**](PaymentInstructions.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account ACH details were successfully retrieved |  -  |
**400** | The request was rejected due to validation failures |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_balance**
> AvailableBalance get_available_balance(customer_id, account_id)

Get Available Balance - Cached

_This endpoint will no longer be available after June 2025. You must transition to using the regular Get Available Balance endpoint, which can return either live or cached data depending on your requirements._

Retrieve the latest cached available and cleared account balances for a customer. Since we update and store balances throughout the day, this is the most accurate balance information available when a connection to a financial institution is unavailable or when a faster response is needed. Only deposit account types are supported: Checking, Savings, Money Market, and CD.

Note: this is a premium service, billable per every successful API call. Enrollment is required.

_Supported account types_: "checking", "savings", "moneyMarket", "cd"

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.available_balance import AvailableBalance
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
    api_instance = openapi_client.PaymentsApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID

    try:
        # Get Available Balance - Cached
        api_response = api_instance.get_available_balance(customer_id, account_id)
        print("The response of PaymentsApi->get_available_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_available_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 

### Return type

[**AvailableBalance**](AvailableBalance.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The balance was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_balance_live**
> AvailableBalance get_available_balance_live(customer_id, account_id, balance_cache_interval=balance_cache_interval)

Get Available Balance

Retrieve the available and cleared account balances for a single account in real-time directly from a financial institution.
You can define an additional query parameter `balance_cache_interval` to specify the time interval of the last cached balance. This parameter is used by the server to determine whether the cached balance is still valid or if it needs to be refreshed.


Note: this is a premium service, billable per every successful API call.

_Supported account types_: "checking", "savings", "moneyMarket", "cd"

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.available_balance import AvailableBalance
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
    api_instance = openapi_client.PaymentsApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID
    balance_cache_interval = 0 # int | `balance_cache_interval` (in minutes) is used to decide whether to return existing cached balance or retrieve from financial institution in real-time. Details explained below: 1. If the cached balance data at server is older than provided `balance_cache_interval` then live balance from financial institution will be retrieved. 2. If the cached balance data is within provided `balance_cache_interval` allowed interval then balance from cache will be returned. 3. If `balance_cache_interval` is 0 or not provided, then live balance from financial institution will be retrieved. (optional) (default to 0)

    try:
        # Get Available Balance
        api_response = api_instance.get_available_balance_live(customer_id, account_id, balance_cache_interval=balance_cache_interval)
        print("The response of PaymentsApi->get_available_balance_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_available_balance_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 
 **balance_cache_interval** | **int**| &#x60;balance_cache_interval&#x60; (in minutes) is used to decide whether to return existing cached balance or retrieve from financial institution in real-time. Details explained below: 1. If the cached balance data at server is older than provided &#x60;balance_cache_interval&#x60; then live balance from financial institution will be retrieved. 2. If the cached balance data is within provided &#x60;balance_cache_interval&#x60; allowed interval then balance from cache will be returned. 3. If &#x60;balance_cache_interval&#x60; is 0 or not provided, then live balance from financial institution will be retrieved. | [optional] [default to 0]

### Return type

[**AvailableBalance**](AvailableBalance.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The live balance was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_payment_details**
> LoanPaymentDetails get_loan_payment_details(customer_id, account_id)

Get Loan Payment Details

Return the loan payment details of the customer for a loan-type account.

Note: this is a premium service, billable per every successful API call.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.loan_payment_details import LoanPaymentDetails
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
    api_instance = openapi_client.PaymentsApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID

    try:
        # Get Loan Payment Details
        api_response = api_instance.get_loan_payment_details(customer_id, account_id)
        print("The response of PaymentsApi->get_loan_payment_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_loan_payment_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 

### Return type

[**LoanPaymentDetails**](LoanPaymentDetails.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The loan payment details were successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

