# ReactorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reactor_id** | **str** | Reactor identifier | [optional] 
**reactor_name** | **str** | Reactor name | [optional] 
**image_url** | **str** | Reactor image path | [optional] 
**reactor_tier_id** | **str** | Reactor tier (Refer to /meta/tier API) | [optional] 
**reactor_skill_power** | [**List[ReactorsInnerReactorSkillPowerInner]**](ReactorsInnerReactorSkillPowerInner.md) | Skill Power by level information | [optional] 
**optimized_condition_type** | **str** | Optimization Condition | [optional] 

## Example

```python
from tfd_api_client.models.reactors_inner import ReactorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReactorsInner from a JSON string
reactors_inner_instance = ReactorsInner.from_json(json)
# print the JSON string representation of the object
print(ReactorsInner.to_json())

# convert the object into a dict
reactors_inner_dict = reactors_inner_instance.to_dict()
# create an instance of ReactorsInner from a dict
reactors_inner_from_dict = ReactorsInner.from_dict(reactors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


