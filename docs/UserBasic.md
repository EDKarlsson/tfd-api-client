# UserBasic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ouid** | **str** | OUID | [optional] 
**user_name** | **str** | Nickname | [optional] 
**platform_type** | **str** | Platform type | [optional] 
**mastery_rank_level** | **float** | Mastery Rank | [optional] 
**mastery_rank_exp** | **float** | Mastery Rank EXP | [optional] 
**title_prefix_id** | **str** | Prefix title identifier (Refer to /meta/title API) | [optional] 
**title_suffix_id** | **str** | Suffix title identifier (Refer to /meta/title API) | [optional] 
**os_language** | **str** | OS language setting | [optional] 
**game_language** | **str** | Game language setting | [optional] 
**medal_id** | **str** | Medal identifier | [optional] 
**medal_level** | **float** | Medal grade | [optional] 

## Example

```python
from tfd_api_client.models.user_basic import UserBasic

# TODO update the JSON string below
json = "{}"
# create an instance of UserBasic from a JSON string
user_basic_instance = UserBasic.from_json(json)
# print the JSON string representation of the object
print(UserBasic.to_json())

# convert the object into a dict
user_basic_dict = user_basic_instance.to_dict()
# create an instance of UserBasic from a dict
user_basic_from_dict = UserBasic.from_dict(user_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


