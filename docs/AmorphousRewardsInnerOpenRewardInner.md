# AmorphousRewardsInnerOpenRewardInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reward_type** | **str** | Reward type (Default, Upgrade) | [optional] 
**required_stabilizer** | **str** | Identifier of the Shape Stabilizer required for upgrade (refer to /meta/consumable-material API) | [optional] 
**reward_item** | [**List[AmorphousRewardsInnerOpenRewardInnerRewardItemInner]**](AmorphousRewardsInnerOpenRewardInnerRewardItemInner.md) | Information about items from Amorphous Material open rewards | [optional] 

## Example

```python
from tfd_api_client.models.amorphous_rewards_inner_open_reward_inner import AmorphousRewardsInnerOpenRewardInner

# TODO update the JSON string below
json = "{}"
# create an instance of AmorphousRewardsInnerOpenRewardInner from a JSON string
amorphous_rewards_inner_open_reward_inner_instance = AmorphousRewardsInnerOpenRewardInner.from_json(json)
# print the JSON string representation of the object
print(AmorphousRewardsInnerOpenRewardInner.to_json())

# convert the object into a dict
amorphous_rewards_inner_open_reward_inner_dict = amorphous_rewards_inner_open_reward_inner_instance.to_dict()
# create an instance of AmorphousRewardsInnerOpenRewardInner from a dict
amorphous_rewards_inner_open_reward_inner_from_dict = AmorphousRewardsInnerOpenRewardInner.from_dict(amorphous_rewards_inner_open_reward_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


