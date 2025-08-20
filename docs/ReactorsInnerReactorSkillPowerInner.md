# ReactorsInnerReactorSkillPowerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | Reactor level | [optional] 
**skill_atk_power** | **float** | Skill Power | [optional] 
**sub_skill_atk_power** | **float** | Sub Attack Power | [optional] 
**skill_power_coefficient** | [**List[ReactorsInnerReactorSkillPowerInnerSkillPowerCoefficientInner]**](ReactorsInnerReactorSkillPowerInnerSkillPowerCoefficientInner.md) | Skill Power Boost Ratio information | [optional] 
**enchant_effect** | [**List[ReactorsInnerReactorSkillPowerInnerEnchantEffectInner]**](ReactorsInnerReactorSkillPowerInnerEnchantEffectInner.md) | Enchantment effect by level information | [optional] 

## Example

```python
from tfd_api_client.models.reactors_inner_reactor_skill_power_inner import ReactorsInnerReactorSkillPowerInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReactorsInnerReactorSkillPowerInner from a JSON string
reactors_inner_reactor_skill_power_inner_instance = ReactorsInnerReactorSkillPowerInner.from_json(json)
# print the JSON string representation of the object
print(ReactorsInnerReactorSkillPowerInner.to_json())

# convert the object into a dict
reactors_inner_reactor_skill_power_inner_dict = reactors_inner_reactor_skill_power_inner_instance.to_dict()
# create an instance of ReactorsInnerReactorSkillPowerInner from a dict
reactors_inner_reactor_skill_power_inner_from_dict = ReactorsInnerReactorSkillPowerInner.from_dict(reactors_inner_reactor_skill_power_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


