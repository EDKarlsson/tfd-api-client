# FellowsInnerFellowDetailInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fellow_level** | **float** | Fellow level | [optional] 
**search_radius_value** | **float** | Search radius values for fellow items by level | [optional] 
**stat_effect** | [**List[FellowsInnerFellowDetailInnerStatEffectInner]**](FellowsInnerFellowDetailInnerStatEffectInner.md) | Stat effect by level | [optional] 

## Example

```python
from tfd_api_client.models.fellows_inner_fellow_detail_inner import FellowsInnerFellowDetailInner

# TODO update the JSON string below
json = "{}"
# create an instance of FellowsInnerFellowDetailInner from a JSON string
fellows_inner_fellow_detail_inner_instance = FellowsInnerFellowDetailInner.from_json(json)
# print the JSON string representation of the object
print(FellowsInnerFellowDetailInner.to_json())

# convert the object into a dict
fellows_inner_fellow_detail_inner_dict = fellows_inner_fellow_detail_inner_instance.to_dict()
# create an instance of FellowsInnerFellowDetailInner from a dict
fellows_inner_fellow_detail_inner_from_dict = FellowsInnerFellowDetailInner.from_dict(fellows_inner_fellow_detail_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


