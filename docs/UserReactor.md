# UserReactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ouid** | **str** | OUID | [optional] 
**user_name** | **str** | Nickname | [optional] 
**reactor_id** | **str** | Reactor identifier (Refer to /meta/reactor API) | [optional] 
**reactor_slot_id** | **str** | Reactor slot identifier | [optional] 
**reactor_level** | **float** | Reactor level | [optional] 
**reactor_additional_stat** | [**List[UserReactorReactorAdditionalStatInner]**](UserReactorReactorAdditionalStatInner.md) | Reactor information | [optional] 
**reactor_enchant_level** | **float** | Reactor enchantment level | [optional] 

## Example

```python
from tfd_api_client.models.user_reactor import UserReactor

# TODO update the JSON string below
json = "{}"
# create an instance of UserReactor from a JSON string
user_reactor_instance = UserReactor.from_json(json)
# print the JSON string representation of the object
print(UserReactor.to_json())

# convert the object into a dict
user_reactor_dict = user_reactor_instance.to_dict()
# create an instance of UserReactor from a dict
user_reactor_from_dict = UserReactor.from_dict(user_reactor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


