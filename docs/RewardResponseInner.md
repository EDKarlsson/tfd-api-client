# RewardResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_id** | **str** | Map identifier | [optional] 
**map_name** | **str** | Map name | [optional] 
**battle_zone** | [**List[RewardResponseInnerBattleZoneInner]**](RewardResponseInnerBattleZoneInner.md) | Battlefield information | [optional] 

## Example

```python
from tfd_api_client.models.reward_response_inner import RewardResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RewardResponseInner from a JSON string
reward_response_inner_instance = RewardResponseInner.from_json(json)
# print the JSON string representation of the object
print(RewardResponseInner.to_json())

# convert the object into a dict
reward_response_inner_dict = reward_response_inner_instance.to_dict()
# create an instance of RewardResponseInner from a dict
reward_response_inner_from_dict = RewardResponseInner.from_dict(reward_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


