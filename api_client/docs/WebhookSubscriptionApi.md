# openapi_client.WebhookSubscriptionApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_webhook_subscription_event_status**](WebhookSubscriptionApi.md#change_webhook_subscription_event_status) | **PUT** /notification-subscriptions/webhooks/{subscription_id}/events/{webhook_event_id}/status | Enable or disable Webhook Subscription Event
[**change_webhook_subscription_status**](WebhookSubscriptionApi.md#change_webhook_subscription_status) | **PUT** /notification-subscriptions/webhooks/{subscription_id}/status | Enable or disable all the webhook event under a given webhook subscription
[**create_webhook_subscription**](WebhookSubscriptionApi.md#create_webhook_subscription) | **POST** /notification-subscriptions/webhooks | Create Webhook Subscription
[**delete_webhook_subscription**](WebhookSubscriptionApi.md#delete_webhook_subscription) | **DELETE** /notification-subscriptions/webhooks/{subscription_id} | Delete Webhook Subscription
[**delete_webhook_subscription_event**](WebhookSubscriptionApi.md#delete_webhook_subscription_event) | **DELETE** /notification-subscriptions/webhooks/{subscription_id}/events/{webhook_event_id} | Delete Webhook Subscription Event
[**get_webhook_subscription_by_id**](WebhookSubscriptionApi.md#get_webhook_subscription_by_id) | **GET** /notification-subscriptions/webhooks/{subscription_id} | Get Webhook Subscription Details
[**list_available_webhook_subscription_events**](WebhookSubscriptionApi.md#list_available_webhook_subscription_events) | **GET** /notification-subscriptions/webhooks/events | List Available Webhook Subscription Events
[**list_webhook_subscriptions**](WebhookSubscriptionApi.md#list_webhook_subscriptions) | **GET** /notification-subscriptions/webhooks | List Webhook Subscriptions
[**test_webhook_subscription**](WebhookSubscriptionApi.md#test_webhook_subscription) | **GET** /notification-subscriptions/webhooks/{subscription_id}/test-subscriptions | Test Webhook Subscription Based on Subscription id
[**test_webhook_subscription_based_on_event_id**](WebhookSubscriptionApi.md#test_webhook_subscription_based_on_event_id) | **GET** /notification-subscriptions/webhooks/{subscription_id}/events/{webhook_event_id}/test-subscriptions | Test Webhook Subscription Based on Subscription id &amp; Webhook event id.
[**update_webhook_subscription**](WebhookSubscriptionApi.md#update_webhook_subscription) | **PUT** /notification-subscriptions/webhooks/{subscription_id} | Update Webhook Subscription
[**update_webhook_subscription_event**](WebhookSubscriptionApi.md#update_webhook_subscription_event) | **PUT** /notification-subscriptions/webhooks/{subscription_id}/events/{webhook_event_id} | Update Webhook Subscription Event


# **change_webhook_subscription_event_status**
> EventStatusUpdate change_webhook_subscription_event_status(subscription_id, webhook_event_id, event_status_update, x_external_request_id=x_external_request_id)

Enable or disable Webhook Subscription Event

Enables or disables a specific webhook event within a subscription identified by subscription ID and webhook event ID. Update the event's status to either active or inactive.


_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.event_status_update import EventStatusUpdate
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
    api_instance = openapi_client.WebhookSubscriptionApi(api_client)
    subscription_id = '661f3c48-f596-423b-81f5-d275d4dd1345' # str | A unique UUID identifier of a webhook subscription.
    webhook_event_id = '661f3c48-f596-423b-81f5-d275d4dd1346' # str | A unique UUID identifier of a webhook event.
    event_status_update = openapi_client.EventStatusUpdate() # EventStatusUpdate | Request body to an event active or inactive.
    x_external_request_id = 'f6250b41-8632-4fe1-9353-899f419ae67b' # str | A unique identifier for the request. (optional)

    try:
        # Enable or disable Webhook Subscription Event
        api_response = api_instance.change_webhook_subscription_event_status(subscription_id, webhook_event_id, event_status_update, x_external_request_id=x_external_request_id)
        print("The response of WebhookSubscriptionApi->change_webhook_subscription_event_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionApi->change_webhook_subscription_event_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| A unique UUID identifier of a webhook subscription. | 
 **webhook_event_id** | **str**| A unique UUID identifier of a webhook event. | 
 **event_status_update** | [**EventStatusUpdate**](EventStatusUpdate.md)| Request body to an event active or inactive. | 
 **x_external_request_id** | **str**| A unique identifier for the request. | [optional] 

### Return type

[**EventStatusUpdate**](EventStatusUpdate.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;App-Key\&quot; or \&quot;App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_webhook_subscription_status**
> EventStatusUpdate change_webhook_subscription_status(subscription_id, event_status_update, x_external_request_id=x_external_request_id)

Enable or disable all the webhook event under a given webhook subscription

Enables or disables all webhook subscription event for partner. Update the  status to either active or inactive. _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.event_status_update import EventStatusUpdate
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
    api_instance = openapi_client.WebhookSubscriptionApi(api_client)
    subscription_id = '661f3c48-f596-423b-81f5-d275d4dd1345' # str | A unique UUID identifier of a webhook subscription.
    event_status_update = openapi_client.EventStatusUpdate() # EventStatusUpdate | Request body to an event active or inactive.
    x_external_request_id = 'f6250b41-8632-4fe1-9353-899f419ae67b' # str | A unique identifier for the request. (optional)

    try:
        # Enable or disable all the webhook event under a given webhook subscription
        api_response = api_instance.change_webhook_subscription_status(subscription_id, event_status_update, x_external_request_id=x_external_request_id)
        print("The response of WebhookSubscriptionApi->change_webhook_subscription_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionApi->change_webhook_subscription_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| A unique UUID identifier of a webhook subscription. | 
 **event_status_update** | [**EventStatusUpdate**](EventStatusUpdate.md)| Request body to an event active or inactive. | 
 **x_external_request_id** | **str**| A unique identifier for the request. | [optional] 

### Return type

[**EventStatusUpdate**](EventStatusUpdate.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;App-Key\&quot; or \&quot;App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_webhook_subscription**
> SubscriptionDetail create_webhook_subscription(subscription, x_external_request_id=x_external_request_id)

Create Webhook Subscription

Creates a new webhook subscription for receiving event notifications. You can specify the URL for receiving notifications and select the events to subscribe to, including any conditions for filtering. Each partner can have multiple subscriptions, and each subscription can cover multiple events. The API supports URL overrides at the event level, ensuring that each subscription is tailored to specific events and their respective requirements.


_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.subscription import Subscription
from openapi_client.models.subscription_detail import SubscriptionDetail
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
    api_instance = openapi_client.WebhookSubscriptionApi(api_client)
    subscription = openapi_client.Subscription() # Subscription | Request body for creating event subscription.
    x_external_request_id = 'f6250b41-8632-4fe1-9353-899f419ae67b' # str | A unique identifier for the request. (optional)

    try:
        # Create Webhook Subscription
        api_response = api_instance.create_webhook_subscription(subscription, x_external_request_id=x_external_request_id)
        print("The response of WebhookSubscriptionApi->create_webhook_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionApi->create_webhook_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | [**Subscription**](Subscription.md)| Request body for creating event subscription. | 
 **x_external_request_id** | **str**| A unique identifier for the request. | [optional] 

### Return type

[**SubscriptionDetail**](SubscriptionDetail.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Subscription created successfully |  -  |
**400** | Bad Request |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;App-Key\&quot; or \&quot;App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_subscription**
> delete_webhook_subscription(subscription_id, x_external_request_id=x_external_request_id)

Delete Webhook Subscription

Deletes a subscription specified by its ID. Once deleted, the subscription and its associated events will no longer be active or receive notifications


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
    api_instance = openapi_client.WebhookSubscriptionApi(api_client)
    subscription_id = '661f3c48-f596-423b-81f5-d275d4dd1345' # str | A unique UUID identifier of a webhook subscription.
    x_external_request_id = 'f6250b41-8632-4fe1-9353-899f419ae67b' # str | A unique identifier for the request. (optional)

    try:
        # Delete Webhook Subscription
        api_instance.delete_webhook_subscription(subscription_id, x_external_request_id=x_external_request_id)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionApi->delete_webhook_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| A unique UUID identifier of a webhook subscription. | 
 **x_external_request_id** | **str**| A unique identifier for the request. | [optional] 

### Return type

void (empty response body)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Subscription deleted successfully |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;App-Key\&quot; or \&quot;App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_subscription_event**
> delete_webhook_subscription_event(subscription_id, webhook_event_id, x_external_request_id=x_external_request_id)

Delete Webhook Subscription Event

Deletes a specific webhook event from a subscription identified by subscription Id and webhook Event Id.


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
    api_instance = openapi_client.WebhookSubscriptionApi(api_client)
    subscription_id = '661f3c48-f596-423b-81f5-d275d4dd1345' # str | A unique UUID identifier of a webhook subscription.
    webhook_event_id = '661f3c48-f596-423b-81f5-d275d4dd1346' # str | A unique UUID identifier of a webhook event.
    x_external_request_id = 'f6250b41-8632-4fe1-9353-899f419ae67b' # str | A unique identifier for the request. (optional)

    try:
        # Delete Webhook Subscription Event
        api_instance.delete_webhook_subscription_event(subscription_id, webhook_event_id, x_external_request_id=x_external_request_id)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionApi->delete_webhook_subscription_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| A unique UUID identifier of a webhook subscription. | 
 **webhook_event_id** | **str**| A unique UUID identifier of a webhook event. | 
 **x_external_request_id** | **str**| A unique identifier for the request. | [optional] 

### Return type

void (empty response body)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Event deleted successfully |  -  |
**400** | Bad Request |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;App-Key\&quot; or \&quot;App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_subscription_by_id**
> SubscriptionDetail get_webhook_subscription_by_id(subscription_id, x_external_request_id=x_external_request_id)

Get Webhook Subscription Details

Retrieves detailed information about a specific webhook subscription using the provided subscription ID. The response includes subscription details such as the events, conditions, and current status.


_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.subscription_detail import SubscriptionDetail
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
    api_instance = openapi_client.WebhookSubscriptionApi(api_client)
    subscription_id = '661f3c48-f596-423b-81f5-d275d4dd1345' # str | A unique UUID identifier of a webhook subscription.
    x_external_request_id = 'f6250b41-8632-4fe1-9353-899f419ae67b' # str | A unique identifier for the request. (optional)

    try:
        # Get Webhook Subscription Details
        api_response = api_instance.get_webhook_subscription_by_id(subscription_id, x_external_request_id=x_external_request_id)
        print("The response of WebhookSubscriptionApi->get_webhook_subscription_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionApi->get_webhook_subscription_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| A unique UUID identifier of a webhook subscription. | 
 **x_external_request_id** | **str**| A unique identifier for the request. | [optional] 

### Return type

[**SubscriptionDetail**](SubscriptionDetail.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription detail by ID |  -  |
**400** | Bad Request |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;App-Key\&quot; or \&quot;App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_webhook_subscription_events**
> ListAvailableWebhookSubscriptionEvents200Response list_available_webhook_subscription_events(x_external_request_id=x_external_request_id)

List Available Webhook Subscription Events

Allows partners to retrieve a list of all event subscriptions supported by the Open Finance system.  This endpoint provides information about each subscription, including the webhook URL and associated events, enabling partners to understand all available subscription options.


_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.list_available_webhook_subscription_events200_response import ListAvailableWebhookSubscriptionEvents200Response
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
    api_instance = openapi_client.WebhookSubscriptionApi(api_client)
    x_external_request_id = 'f6250b41-8632-4fe1-9353-899f419ae67b' # str | A unique identifier for the request. (optional)

    try:
        # List Available Webhook Subscription Events
        api_response = api_instance.list_available_webhook_subscription_events(x_external_request_id=x_external_request_id)
        print("The response of WebhookSubscriptionApi->list_available_webhook_subscription_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionApi->list_available_webhook_subscription_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_external_request_id** | **str**| A unique identifier for the request. | [optional] 

### Return type

[**ListAvailableWebhookSubscriptionEvents200Response**](ListAvailableWebhookSubscriptionEvents200Response.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all available events. |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;App-Key\&quot; or \&quot;App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook_subscriptions**
> Subscriptions list_webhook_subscriptions(x_external_request_id=x_external_request_id, offset=offset, limit=limit)

List Webhook Subscriptions

Retrieves a list of all webhook subscriptions. The response includes details of each subscription, such as the subscription ID, URL, events, and their conditions. This API provides an overview of all active and inactive subscriptions.


_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.subscriptions import Subscriptions
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
    api_instance = openapi_client.WebhookSubscriptionApi(api_client)
    x_external_request_id = 'f6250b41-8632-4fe1-9353-899f419ae67b' # str | A unique identifier for the request. (optional)
    offset = 1 # int | Index of the page of results to return. (optional) (default to 1)
    limit = 10 # int | Maximum number of results per page. (optional) (default to 10)

    try:
        # List Webhook Subscriptions
        api_response = api_instance.list_webhook_subscriptions(x_external_request_id=x_external_request_id, offset=offset, limit=limit)
        print("The response of WebhookSubscriptionApi->list_webhook_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionApi->list_webhook_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_external_request_id** | **str**| A unique identifier for the request. | [optional] 
 **offset** | **int**| Index of the page of results to return. | [optional] [default to 1]
 **limit** | **int**| Maximum number of results per page. | [optional] [default to 10]

### Return type

[**Subscriptions**](Subscriptions.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all subscriptions with pagination and availability details. |  -  |
**400** | Bad Request |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;App-Key\&quot; or \&quot;App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_webhook_subscription**
> test_webhook_subscription(subscription_id, x_external_request_id=x_external_request_id)

Test Webhook Subscription Based on Subscription id

Test all the webhook event under the given webhook subscription using subscription_id. _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

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
    api_instance = openapi_client.WebhookSubscriptionApi(api_client)
    subscription_id = '661f3c48-f596-423b-81f5-d275d4dd1345' # str | A unique UUID identifier of a webhook subscription.
    x_external_request_id = 'f6250b41-8632-4fe1-9353-899f419ae67b' # str | A unique identifier for the request. (optional)

    try:
        # Test Webhook Subscription Based on Subscription id
        api_instance.test_webhook_subscription(subscription_id, x_external_request_id=x_external_request_id)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionApi->test_webhook_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| A unique UUID identifier of a webhook subscription. | 
 **x_external_request_id** | **str**| A unique identifier for the request. | [optional] 

### Return type

void (empty response body)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | test subscription submitted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;App-Key\&quot; or \&quot;App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_webhook_subscription_based_on_event_id**
> test_webhook_subscription_based_on_event_id(subscription_id, webhook_event_id, x_external_request_id=x_external_request_id)

Test Webhook Subscription Based on Subscription id & Webhook event id.

Test the webhook event under the given webhook subscription using subscription_id & webhook event id. _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

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
    api_instance = openapi_client.WebhookSubscriptionApi(api_client)
    subscription_id = '661f3c48-f596-423b-81f5-d275d4dd1345' # str | A unique UUID identifier of a webhook subscription.
    webhook_event_id = '661f3c48-f596-423b-81f5-d275d4dd1346' # str | A unique UUID identifier of a webhook event.
    x_external_request_id = 'f6250b41-8632-4fe1-9353-899f419ae67b' # str | A unique identifier for the request. (optional)

    try:
        # Test Webhook Subscription Based on Subscription id & Webhook event id.
        api_instance.test_webhook_subscription_based_on_event_id(subscription_id, webhook_event_id, x_external_request_id=x_external_request_id)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionApi->test_webhook_subscription_based_on_event_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| A unique UUID identifier of a webhook subscription. | 
 **webhook_event_id** | **str**| A unique UUID identifier of a webhook event. | 
 **x_external_request_id** | **str**| A unique identifier for the request. | [optional] 

### Return type

void (empty response body)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | test subscription submitted successfully. |  -  |
**400** | Bad Request |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;App-Key\&quot; or \&quot;App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_subscription**
> SubscriptionDetail update_webhook_subscription(subscription_id, subscription, x_external_request_id=x_external_request_id)

Update Webhook Subscription

Updates an existing webhook subscription with the specified subscription ID. You can modify the subscription URL and the events associated with it.


_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.subscription import Subscription
from openapi_client.models.subscription_detail import SubscriptionDetail
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
    api_instance = openapi_client.WebhookSubscriptionApi(api_client)
    subscription_id = '661f3c48-f596-423b-81f5-d275d4dd1345' # str | A unique UUID identifier of a webhook subscription.
    subscription = openapi_client.Subscription() # Subscription | Request body for updating event subscription.
    x_external_request_id = 'f6250b41-8632-4fe1-9353-899f419ae67b' # str | A unique identifier for the request. (optional)

    try:
        # Update Webhook Subscription
        api_response = api_instance.update_webhook_subscription(subscription_id, subscription, x_external_request_id=x_external_request_id)
        print("The response of WebhookSubscriptionApi->update_webhook_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionApi->update_webhook_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| A unique UUID identifier of a webhook subscription. | 
 **subscription** | [**Subscription**](Subscription.md)| Request body for updating event subscription. | 
 **x_external_request_id** | **str**| A unique identifier for the request. | [optional] 

### Return type

[**SubscriptionDetail**](SubscriptionDetail.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;App-Key\&quot; or \&quot;App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_subscription_event**
> WebhookEvent update_webhook_subscription_event(subscription_id, webhook_event_id, webhook_event, x_external_request_id=x_external_request_id)

Update Webhook Subscription Event

Updates a specific webhook event in a subscription. Use subscription Id and webhook Event Id to identify the event and modify its details.


_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.webhook_event import WebhookEvent
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
    api_instance = openapi_client.WebhookSubscriptionApi(api_client)
    subscription_id = '661f3c48-f596-423b-81f5-d275d4dd1345' # str | A unique UUID identifier of a webhook subscription.
    webhook_event_id = '661f3c48-f596-423b-81f5-d275d4dd1346' # str | A unique UUID identifier of a webhook event.
    webhook_event = openapi_client.WebhookEvent() # WebhookEvent | Request body to update Event
    x_external_request_id = 'f6250b41-8632-4fe1-9353-899f419ae67b' # str | A unique identifier for the request. (optional)

    try:
        # Update Webhook Subscription Event
        api_response = api_instance.update_webhook_subscription_event(subscription_id, webhook_event_id, webhook_event, x_external_request_id=x_external_request_id)
        print("The response of WebhookSubscriptionApi->update_webhook_subscription_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookSubscriptionApi->update_webhook_subscription_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| A unique UUID identifier of a webhook subscription. | 
 **webhook_event_id** | **str**| A unique UUID identifier of a webhook event. | 
 **webhook_event** | [**WebhookEvent**](WebhookEvent.md)| Request body to update Event | 
 **x_external_request_id** | **str**| A unique identifier for the request. | [optional] 

### Return type

[**WebhookEvent**](WebhookEvent.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;App-Key\&quot; or \&quot;App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

