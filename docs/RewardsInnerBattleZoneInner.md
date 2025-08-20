# RewardsInnerBattleZoneInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battle_zone_id** | **str** | Battlefield identifier | [optional] 
**battle_zone_name** | **str** | Battlefield name | [optional] 
**reward** | [**List[RewardsInnerBattleZoneInnerRewardInner]**](RewardsInnerBattleZoneInnerRewardInner.md) | Reward rotation information | [optional] 

## Example

```python
from tfd_api_client.models.rewards_inner_battle_zone_inner import RewardsInnerBattleZoneInner

# TODO update the JSON string below
json = "{}"
# create an instance of RewardsInnerBattleZoneInner from a JSON string
rewards_inner_battle_zone_inner_instance = RewardsInnerBattleZoneInner.from_json(json)
# print the JSON string representation of the object
print(RewardsInnerBattleZoneInner.to_json())

# convert the object into a dict
rewards_inner_battle_zone_inner_dict = rewards_inner_battle_zone_inner_instance.to_dict()
# create an instance of RewardsInnerBattleZoneInner from a dict
rewards_inner_battle_zone_inner_from_dict = RewardsInnerBattleZoneInner.from_dict(rewards_inner_battle_zone_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


