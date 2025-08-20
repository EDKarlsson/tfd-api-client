# RewardsInnerBattleZoneInnerRewardInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rotation** | **float** | Reward rotation | [optional] 
**reward_type** | **str** | Reward type | [optional] 
**reactor_element_type** | **str** | Skill type | [optional] 
**weapon_rounds_type** | **str** | Weapon rounds type | [optional] 
**arche_type** | **str** | Arche type | [optional] 

## Example

```python
from tfd_api_client.models.rewards_inner_battle_zone_inner_reward_inner import RewardsInnerBattleZoneInnerRewardInner

# TODO update the JSON string below
json = "{}"
# create an instance of RewardsInnerBattleZoneInnerRewardInner from a JSON string
rewards_inner_battle_zone_inner_reward_inner_instance = RewardsInnerBattleZoneInnerRewardInner.from_json(json)
# print the JSON string representation of the object
print(RewardsInnerBattleZoneInnerRewardInner.to_json())

# convert the object into a dict
rewards_inner_battle_zone_inner_reward_inner_dict = rewards_inner_battle_zone_inner_reward_inner_instance.to_dict()
# create an instance of RewardsInnerBattleZoneInnerRewardInner from a dict
rewards_inner_battle_zone_inner_reward_inner_from_dict = RewardsInnerBattleZoneInnerRewardInner.from_dict(rewards_inner_battle_zone_inner_reward_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


