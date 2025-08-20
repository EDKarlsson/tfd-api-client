# AmorphousRewardsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amorphous_reward_id** | **str** | Identifier for Amorphous Material open reward | [optional] 
**open_reward** | [**List[AmorphousRewardsInnerOpenRewardInner]**](AmorphousRewardsInnerOpenRewardInner.md) | Information about Amorphous Material open rewards | [optional] 

## Example

```python
from tfd_api_client.models.amorphous_rewards_inner import AmorphousRewardsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AmorphousRewardsInner from a JSON string
amorphous_rewards_inner_instance = AmorphousRewardsInner.from_json(json)
# print the JSON string representation of the object
print(AmorphousRewardsInner.to_json())

# convert the object into a dict
amorphous_rewards_inner_dict = amorphous_rewards_inner_instance.to_dict()
# create an instance of AmorphousRewardsInner from a dict
amorphous_rewards_inner_from_dict = AmorphousRewardsInner.from_dict(amorphous_rewards_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


