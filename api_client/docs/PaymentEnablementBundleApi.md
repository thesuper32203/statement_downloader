# openapi_client.PaymentEnablementBundleApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_details_by_account_id**](PaymentEnablementBundleApi.md#get_account_details_by_account_id) | **GET** /aggregation/v1/paysuite/customers/{customerId}/accounts/{accountId} | Fetch all the requested details using the account ID
[**get_account_details_by_institution_login_id**](PaymentEnablementBundleApi.md#get_account_details_by_institution_login_id) | **GET** /aggregation/v1/paysuite/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts | Fetch all the requested field details using institution login ID


# **get_account_details_by_account_id**
> PaymentEnablementBundle get_account_details_by_account_id(customer_id, account_id, include=include, balance_cache_interval=balance_cache_interval)

Fetch all the requested details using the account ID

This bundled API will return any or all of the Payments endpoints in one API call using account ID. This includes, Account Simple details, ACH details, Account Owner, and Account Balance. This requires initial setup to determine which endpoints are included in the API response.
For Account Balance, You can define an additional query parameter `balance_cache_interval` to specify the time interval of the last cached balance.  This parameter will be used by the server to determine whether the cached balance is still valid or if it needs to be refreshed.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.payment_enablement_bundle import PaymentEnablementBundle
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
    api_instance = openapi_client.PaymentEnablementBundleApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID
    include = 'balanceDetails, paymentInstruction, accountIdentity' # str | If you do not require all API fields ( `balanceDetails`, `accountIdentity` and `paymentInstruction`) then mention specific API fields you are interested in.  For example, If you are interested in only `balanceDetails` and `paymentInstruction`, then send query string as include=`balanceDetails`,`paymentInstruction` (optional)
    balance_cache_interval = 30 # int | `balance_cache_interval` (in minutes) is used at server side to decide whether to return existing cached balance or retrieve from financial institution in real-time. Details explained below: 1. If the cached balance data at server is older than provided `balance_cache_interval` then live balance from financial institution will be retrieved. 2. If the cached balance data is within provided `balance_cache_interval` allowed interval then balance from cache will be returned. 3. If `balance_cache_interval` is not provided, then by default pre defined cache interval will be used to decide whether to return existing cached balance or retrieve from financial institution in real-time. (optional) (default to 30)

    try:
        # Fetch all the requested details using the account ID
        api_response = api_instance.get_account_details_by_account_id(customer_id, account_id, include=include, balance_cache_interval=balance_cache_interval)
        print("The response of PaymentEnablementBundleApi->get_account_details_by_account_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentEnablementBundleApi->get_account_details_by_account_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 
 **include** | **str**| If you do not require all API fields ( &#x60;balanceDetails&#x60;, &#x60;accountIdentity&#x60; and &#x60;paymentInstruction&#x60;) then mention specific API fields you are interested in.  For example, If you are interested in only &#x60;balanceDetails&#x60; and &#x60;paymentInstruction&#x60;, then send query string as include&#x3D;&#x60;balanceDetails&#x60;,&#x60;paymentInstruction&#x60; | [optional] 
 **balance_cache_interval** | **int**| &#x60;balance_cache_interval&#x60; (in minutes) is used at server side to decide whether to return existing cached balance or retrieve from financial institution in real-time. Details explained below: 1. If the cached balance data at server is older than provided &#x60;balance_cache_interval&#x60; then live balance from financial institution will be retrieved. 2. If the cached balance data is within provided &#x60;balance_cache_interval&#x60; allowed interval then balance from cache will be returned. 3. If &#x60;balance_cache_interval&#x60; is not provided, then by default pre defined cache interval will be used to decide whether to return existing cached balance or retrieve from financial institution in real-time. | [optional] [default to 30]

### Return type

[**PaymentEnablementBundle**](PaymentEnablementBundle.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | We successfully fetched the requested details |  -  |
**400** | We couldn&#39;t handle your request, see response payload for more information. |  -  |
**401** | The request lacks valid authentication credentials. Check Partner ID, Partner Secret or Finicity-App-Key. |  -  |
**404** | Customer ID or Account ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_details_by_institution_login_id**
> PaymentEnablementBundle get_account_details_by_institution_login_id(customer_id, institution_login_id, include=include, balance_cache_interval=balance_cache_interval)

Fetch all the requested field details using institution login ID

This bundled API returns any or all of the Payments endpoints in one API call using institution login ID. This includes, Account Simple details, ACH details, Account Owner, and Account Balance. This requires initial setup to determine which endpoints are included in the API response.
For Account Balance, You can define an additional query parameter `balance_cache_interval` to specify the time interval of the last cached balance.  This parameter is used by the server to determine whether the cached balance is still valid or if it needs to be refreshed.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.payment_enablement_bundle import PaymentEnablementBundle
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
    api_instance = openapi_client.PaymentEnablementBundleApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    institution_login_id = 1007302745 # int | The institution login ID
    include = 'balanceDetails, paymentInstruction, accountIdentity' # str | If you do not require all API fields ( `balanceDetails`, `accountIdentity` and `paymentInstruction`) then mention specific API fields you are interested in.  For example, If you are interested in only `balanceDetails` and `paymentInstruction`, then send query string as include=`balanceDetails`,`paymentInstruction` (optional)
    balance_cache_interval = 30 # int | `balance_cache_interval` (in minutes) is used at server side to decide whether to return existing cached balance or retrieve from financial institution in real-time. Details explained below: 1. If the cached balance data at server is older than provided `balance_cache_interval` then live balance from financial institution will be retrieved. 2. If the cached balance data is within provided `balance_cache_interval` allowed interval then balance from cache will be returned. 3. If `balance_cache_interval` is not provided, then by default pre defined cache interval will be used to decide whether to return existing cached balance or retrieve from financial institution in real-time. (optional) (default to 30)

    try:
        # Fetch all the requested field details using institution login ID
        api_response = api_instance.get_account_details_by_institution_login_id(customer_id, institution_login_id, include=include, balance_cache_interval=balance_cache_interval)
        print("The response of PaymentEnablementBundleApi->get_account_details_by_institution_login_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentEnablementBundleApi->get_account_details_by_institution_login_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **institution_login_id** | **int**| The institution login ID | 
 **include** | **str**| If you do not require all API fields ( &#x60;balanceDetails&#x60;, &#x60;accountIdentity&#x60; and &#x60;paymentInstruction&#x60;) then mention specific API fields you are interested in.  For example, If you are interested in only &#x60;balanceDetails&#x60; and &#x60;paymentInstruction&#x60;, then send query string as include&#x3D;&#x60;balanceDetails&#x60;,&#x60;paymentInstruction&#x60; | [optional] 
 **balance_cache_interval** | **int**| &#x60;balance_cache_interval&#x60; (in minutes) is used at server side to decide whether to return existing cached balance or retrieve from financial institution in real-time. Details explained below: 1. If the cached balance data at server is older than provided &#x60;balance_cache_interval&#x60; then live balance from financial institution will be retrieved. 2. If the cached balance data is within provided &#x60;balance_cache_interval&#x60; allowed interval then balance from cache will be returned. 3. If &#x60;balance_cache_interval&#x60; is not provided, then by default pre defined cache interval will be used to decide whether to return existing cached balance or retrieve from financial institution in real-time. | [optional] [default to 30]

### Return type

[**PaymentEnablementBundle**](PaymentEnablementBundle.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | We successfully fetched the requested details |  -  |
**400** | We couldn&#39;t handle your request, see response payload for more information. |  -  |
**401** | The request lacks valid authentication credentials. Check Partner ID, Partner Secret or Finicity-App-Key. |  -  |
**404** | The requested details do not match with the existing details or you requested something we don&#39;t have or was deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

