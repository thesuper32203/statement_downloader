# Card

Structure of the user card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The user title for the card in use | 
**number** | **str** | The card number used for bill payment. Should be between 15-19 digits | 
**expiry** | **str** | The expiry date for the card in mm/yy format | 
**cvv** | **str** | The CVV / CVC number associated to the card | 
**brand** | **str** | The Brand of card in use. Possible values include mastercard, visa, american-express, or discover. | [optional] 

## Example

```python
from openapi_client.models.card import Card

# TODO update the JSON string below
json = "{}"
# create an instance of Card from a JSON string
card_instance = Card.from_json(json)
# print the JSON string representation of the object
print(Card.to_json())

# convert the object into a dict
card_dict = card_instance.to_dict()
# create an instance of Card from a dict
card_from_dict = Card.from_dict(card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


