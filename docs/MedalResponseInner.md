# MedalResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medal_id** | **str** | Medal identifier | [optional] 
**medal_detail** | [**List[MedalResponseInnerMedalDetailInner]**](MedalResponseInnerMedalDetailInner.md) | Description by medal grade | [optional] 

## Example

```python
from tfd_api_client.models.medal_response_inner import MedalResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of MedalResponseInner from a JSON string
medal_response_inner_instance = MedalResponseInner.from_json(json)
# print the JSON string representation of the object
print(MedalResponseInner.to_json())

# convert the object into a dict
medal_response_inner_dict = medal_response_inner_instance.to_dict()
# create an instance of MedalResponseInner from a dict
medal_response_inner_from_dict = MedalResponseInner.from_dict(medal_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


