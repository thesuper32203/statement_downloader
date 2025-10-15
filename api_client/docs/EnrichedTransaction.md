# EnrichedTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_customer_id** | **str** | A unique identifier assigned to the customer for a particular institution. | [optional] 
**external_account_id** | **str** | A unique identifier assigned to the accounts for a particular institution. | [optional] 
**account_type** | **str** | Indicates the type of account associated with the transaction. Listed below are the current account types supported:  \&quot;checking\&quot;, \&quot;savings\&quot;, \&quot;creditCard\&quot;, \&quot;brokerageAccount\&quot;, \&quot;investment\&quot;, \&quot;healthSavingsAccount\&quot;, \&quot;unknown\&quot;  NOTE : If \&quot;unknown\&quot; is provided, the enrichment service will assume it is a \&quot;checking\&quot; account. An incorrect assumption could impact the results from the enrichment service.  | [optional] 
**external_transaction_id** | **str** | A unique identifier for the transaction that assists in linking data back to your systems. | [optional] 
**posted_timestamp** | **str** | The date and time when the transaction was officially recorded in the account.  Supported formats are yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;, yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;, yyyy-MM-dd HH:mm:ss.0, yyyy-MM-dd.  | [optional] 
**transaction_timestamp** | **str** | The exact date and time when the transaction was initiated or occurred.  Supported formats are yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;, yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;, yyyy-MM-dd HH:mm:ss.0, yyyy-MM-dd.  | [optional] 
**description** | **str** | Description of the transaction. | [optional] 
**memo** | **str** | Memo of the transaction. | [optional] 
**amount** | **float** | Value amount for transaction. | [optional] 
**transaction_fee** | **float** | A charge applied to the transaction. | [optional] 
**transaction_category** | **str** | Transaction Category for the transaction. | [optional] 
**transaction_category_score** | **float** | A confidence score between 0 – 100.0 for the transaction category. | [optional] 
**transaction_category_group** | **str** | The parent group that a transaction category belongs to. | [optional] 
**type** | **str** | Type for transaction. | [optional] 
**direction_indicator** | **str** | - The directionIndicator should be from the perspective of the account holder. - If you always send us positive amount values, you MUST send us corresponding directionIndicator values to ensure the categorization logic works as intended. - If you have internal logic to provide the amount field as either positive or negative, do not send us data in the directionIndicator.  - Listed below are the current directionIndicator types supported:   - \&quot;Debit\&quot;   - \&quot;Credit\&quot;  | [optional] 
**entities** | [**List[EntitiesInner]**](EntitiesInner.md) | Entities refer to the distinct parties involved in the transaction. | [optional] 
**address** | [**DESAddress**](DESAddress.md) |  | [optional] 
**additional_details** | **Dict[str, str]** | A dictionary containing additional details of the transaction being returned in the enrichment response. - This object should not contain any PII. - The max number of allowed keys are 30. - The key max length should be 100. - The value max length should be 255.  | [optional] 
**card_acceptor_id** | **str** | Also known as CAID, Merchant ID, or DE42, cardAcceptorId is an alphanumeric string assigned by the acquiring bank (Acquirer) to a merchant or merchant location. It serves as a unique identifier for the point of transaction origin, such as a physical store, payment terminal, or online checkout page. | [optional] 
**input_is_recurring_transaction** | **bool** | A flag in the input indicating whether the transaction is recurring or not. | [optional] 
**input_merchant_information** | [**InputMerchantInformation**](InputMerchantInformation.md) |  | [optional] 
**is_recurring_transaction** | **bool** | A flag indicating whether the transaction is recurring or not. | [optional] 
**location_id** | **float** | The Mastercard assigned location id representing this merchant location. | [optional] 
**is_ecommerce** | **bool** | A flag indicating whether the business location is ecommerce or not. | [optional] 
**is_brick_and_mortar** | **bool** | A boolean value indicating if the identified merchant is a brick and mortar location. | [optional] 
**match_confidence_score** | **float** | If the merchantDescriptor is used to select the locationId and location details, a matchConfidenceScore is returned, indicating the score between the merchantDescriptor and the selected information from our internal data on merchants. | [optional] 

## Example

```python
from openapi_client.models.enriched_transaction import EnrichedTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedTransaction from a JSON string
enriched_transaction_instance = EnrichedTransaction.from_json(json)
# print the JSON string representation of the object
print(EnrichedTransaction.to_json())

# convert the object into a dict
enriched_transaction_dict = enriched_transaction_instance.to_dict()
# create an instance of EnrichedTransaction from a dict
enriched_transaction_from_dict = EnrichedTransaction.from_dict(enriched_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


