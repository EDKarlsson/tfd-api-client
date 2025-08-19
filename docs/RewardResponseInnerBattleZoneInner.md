# RewardResponseInnerBattleZoneInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battle_zone_id** | **str** | Battlefield identifier | [optional] 
**battle_zone_name** | **str** | Battlefield name | [optional] 
**reward** | [**List[RewardResponseInnerBattleZoneInnerRewardInner]**](RewardResponseInnerBattleZoneInnerRewardInner.md) | Reward rotation information | [optional] 

## Example

```python
from tfd_api_client.models.reward_response_inner_battle_zone_inner import RewardResponseInnerBattleZoneInner

# TODO update the JSON string below
json = "{}"
# create an instance of RewardResponseInnerBattleZoneInner from a JSON string
reward_response_inner_battle_zone_inner_instance = RewardResponseInnerBattleZoneInner.from_json(json)
# print the JSON string representation of the object
print(RewardResponseInnerBattleZoneInner.to_json())

# convert the object into a dict
reward_response_inner_battle_zone_inner_dict = reward_response_inner_battle_zone_inner_instance.to_dict()
# create an instance of RewardResponseInnerBattleZoneInner from a dict
reward_response_inner_battle_zone_inner_from_dict = RewardResponseInnerBattleZoneInner.from_dict(reward_response_inner_battle_zone_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


