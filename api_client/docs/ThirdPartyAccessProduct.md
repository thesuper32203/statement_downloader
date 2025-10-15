# ThirdPartyAccessProduct

Product for which access token to be generated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Third party access token can be generated for the following product types:   * \&quot;moneyTransferDetails\&quot;: Retrieve account details for money transfer * \&quot;availableBalance\&quot;: Retrieves the latest cached available and cleared     account balances for an account. * \&quot;availableBalanceLive\&quot;: Retrieves the available and cleared account balances live from the financial institution * \&quot;accountOwner\&quot;: Retrieves names and addresses of the account owner from a financial institution. * \&quot;paymentIndicator\&quot;: Get the Payment Success Indicator response, scoring the likelihood of payment settlement | 
**payor_id** | **str** | The Finicity Partner ID who should be billed when the Requester requests data from Finicity. If no value specified, then the Recipient will be billed. | [optional] 
**max_calls** | **int** | Max number of calls to the consented product (consented API) | [optional] 
**account_id** | **str** | An account ID | 
**access_period** | [**ThirdPartyAccessPeriod**](ThirdPartyAccessPeriod.md) |  | 

## Example

```python
from openapi_client.models.third_party_access_product import ThirdPartyAccessProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyAccessProduct from a JSON string
third_party_access_product_instance = ThirdPartyAccessProduct.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyAccessProduct.to_json())

# convert the object into a dict
third_party_access_product_dict = third_party_access_product_instance.to_dict()
# create an instance of ThirdPartyAccessProduct from a dict
third_party_access_product_from_dict = ThirdPartyAccessProduct.from_dict(third_party_access_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


