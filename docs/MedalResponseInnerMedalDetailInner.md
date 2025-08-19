# MedalResponseInnerMedalDetailInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medal_level** | **float** | Medal grade | [optional] 
**medal_name** | **str** | Medal name | [optional] 
**medal_tier_id** | **str** | Medal grade (Refer to /meta/tier API) | [optional] 
**medal_image_url** | **str** | Medal image path | [optional] 

## Example

```python
from tfd_api_client.models.medal_response_inner_medal_detail_inner import MedalResponseInnerMedalDetailInner

# TODO update the JSON string below
json = "{}"
# create an instance of MedalResponseInnerMedalDetailInner from a JSON string
medal_response_inner_medal_detail_inner_instance = MedalResponseInnerMedalDetailInner.from_json(json)
# print the JSON string representation of the object
print(MedalResponseInnerMedalDetailInner.to_json())

# convert the object into a dict
medal_response_inner_medal_detail_inner_dict = medal_response_inner_medal_detail_inner_instance.to_dict()
# create an instance of MedalResponseInnerMedalDetailInner from a dict
medal_response_inner_medal_detail_inner_from_dict = MedalResponseInnerMedalDetailInner.from_dict(medal_response_inner_medal_detail_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


