# RewardsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_id** | **str** | Map identifier | [optional] 
**map_name** | **str** | Map name | [optional] 
**battle_zone** | [**List[RewardsInnerBattleZoneInner]**](RewardsInnerBattleZoneInner.md) | Battlefield information | [optional] 

## Example

```python
from tfd_api_client.models.rewards_inner import RewardsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RewardsInner from a JSON string
rewards_inner_instance = RewardsInner.from_json(json)
# print the JSON string representation of the object
print(RewardsInner.to_json())

# convert the object into a dict
rewards_inner_dict = rewards_inner_instance.to_dict()
# create an instance of RewardsInner from a dict
rewards_inner_from_dict = RewardsInner.from_dict(rewards_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


