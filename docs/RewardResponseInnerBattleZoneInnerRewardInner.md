# RewardResponseInnerBattleZoneInnerRewardInner


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
from tfd_api_client.models.reward_response_inner_battle_zone_inner_reward_inner import RewardResponseInnerBattleZoneInnerRewardInner

# TODO update the JSON string below
json = "{}"
# create an instance of RewardResponseInnerBattleZoneInnerRewardInner from a JSON string
reward_response_inner_battle_zone_inner_reward_inner_instance = RewardResponseInnerBattleZoneInnerRewardInner.from_json(json)
# print the JSON string representation of the object
print(RewardResponseInnerBattleZoneInnerRewardInner.to_json())

# convert the object into a dict
reward_response_inner_battle_zone_inner_reward_inner_dict = reward_response_inner_battle_zone_inner_reward_inner_instance.to_dict()
# create an instance of RewardResponseInnerBattleZoneInnerRewardInner from a dict
reward_response_inner_battle_zone_inner_reward_inner_from_dict = RewardResponseInnerBattleZoneInnerRewardInner.from_dict(reward_response_inner_battle_zone_inner_reward_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


