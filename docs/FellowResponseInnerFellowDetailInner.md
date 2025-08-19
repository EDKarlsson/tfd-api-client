# FellowResponseInnerFellowDetailInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fellow_level** | **float** | Fellow level | [optional] 
**search_radius_value** | **float** | Search radius values for fellow items by level | [optional] 
**stat_effect** | [**List[FellowResponseInnerFellowDetailInnerStatEffectInner]**](FellowResponseInnerFellowDetailInnerStatEffectInner.md) | Stat effect by level | [optional] 

## Example

```python
from tfd_api_client.models.fellow_response_inner_fellow_detail_inner import FellowResponseInnerFellowDetailInner

# TODO update the JSON string below
json = "{}"
# create an instance of FellowResponseInnerFellowDetailInner from a JSON string
fellow_response_inner_fellow_detail_inner_instance = FellowResponseInnerFellowDetailInner.from_json(json)
# print the JSON string representation of the object
print(FellowResponseInnerFellowDetailInner.to_json())

# convert the object into a dict
fellow_response_inner_fellow_detail_inner_dict = fellow_response_inner_fellow_detail_inner_instance.to_dict()
# create an instance of FellowResponseInnerFellowDetailInner from a dict
fellow_response_inner_fellow_detail_inner_from_dict = FellowResponseInnerFellowDetailInner.from_dict(fellow_response_inner_fellow_detail_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


