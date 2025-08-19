# VoidBattleResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**void_battle_id** | **str** | Void Intercept Battle identifier | [optional] 
**void_battle_name** | **str** | Void Intercept Battle name | [optional] 

## Example

```python
from tfd_api_client.models.void_battle_response_inner import VoidBattleResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of VoidBattleResponseInner from a JSON string
void_battle_response_inner_instance = VoidBattleResponseInner.from_json(json)
# print the JSON string representation of the object
print(VoidBattleResponseInner.to_json())

# convert the object into a dict
void_battle_response_inner_dict = void_battle_response_inner_instance.to_dict()
# create an instance of VoidBattleResponseInner from a dict
void_battle_response_inner_from_dict = VoidBattleResponseInner.from_dict(void_battle_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


