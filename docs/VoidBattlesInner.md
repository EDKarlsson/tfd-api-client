# VoidBattlesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**void_battle_id** | **str** | Void Intercept Battle identifier | [optional] 
**void_battle_name** | **str** | Void Intercept Battle name | [optional] 

## Example

```python
from tfd_api_client.models.void_battles_inner import VoidBattlesInner

# TODO update the JSON string below
json = "{}"
# create an instance of VoidBattlesInner from a JSON string
void_battles_inner_instance = VoidBattlesInner.from_json(json)
# print the JSON string representation of the object
print(VoidBattlesInner.to_json())

# convert the object into a dict
void_battles_inner_dict = void_battles_inner_instance.to_dict()
# create an instance of VoidBattlesInner from a dict
void_battles_inner_from_dict = VoidBattlesInner.from_dict(void_battles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


