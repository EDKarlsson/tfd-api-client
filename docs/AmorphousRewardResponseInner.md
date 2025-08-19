# AmorphousRewardResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amorphous_reward_id** | **str** | Identifier for Amorphous Material open reward | [optional] 
**open_reward** | [**List[AmorphousRewardResponseInnerOpenRewardInner]**](AmorphousRewardResponseInnerOpenRewardInner.md) | Information about Amorphous Material open rewards | [optional] 

## Example

```python
from tfd_api_client.models.amorphous_reward_response_inner import AmorphousRewardResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AmorphousRewardResponseInner from a JSON string
amorphous_reward_response_inner_instance = AmorphousRewardResponseInner.from_json(json)
# print the JSON string representation of the object
print(AmorphousRewardResponseInner.to_json())

# convert the object into a dict
amorphous_reward_response_inner_dict = amorphous_reward_response_inner_instance.to_dict()
# create an instance of AmorphousRewardResponseInner from a dict
amorphous_reward_response_inner_from_dict = AmorphousRewardResponseInner.from_dict(amorphous_reward_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


