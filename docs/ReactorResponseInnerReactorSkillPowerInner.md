# ReactorResponseInnerReactorSkillPowerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | Reactor level | [optional] 
**skill_atk_power** | **float** | Skill Power | [optional] 
**sub_skill_atk_power** | **float** | Sub Attack Power | [optional] 
**skill_power_coefficient** | [**List[ReactorResponseInnerReactorSkillPowerInnerSkillPowerCoefficientInner]**](ReactorResponseInnerReactorSkillPowerInnerSkillPowerCoefficientInner.md) | Skill Power Boost Ratio information | [optional] 
**enchant_effect** | [**List[ReactorResponseInnerReactorSkillPowerInnerEnchantEffectInner]**](ReactorResponseInnerReactorSkillPowerInnerEnchantEffectInner.md) | Enchantment effect by level information | [optional] 

## Example

```python
from tfd_api_client.models.reactor_response_inner_reactor_skill_power_inner import ReactorResponseInnerReactorSkillPowerInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReactorResponseInnerReactorSkillPowerInner from a JSON string
reactor_response_inner_reactor_skill_power_inner_instance = ReactorResponseInnerReactorSkillPowerInner.from_json(json)
# print the JSON string representation of the object
print(ReactorResponseInnerReactorSkillPowerInner.to_json())

# convert the object into a dict
reactor_response_inner_reactor_skill_power_inner_dict = reactor_response_inner_reactor_skill_power_inner_instance.to_dict()
# create an instance of ReactorResponseInnerReactorSkillPowerInner from a dict
reactor_response_inner_reactor_skill_power_inner_from_dict = ReactorResponseInnerReactorSkillPowerInner.from_dict(reactor_response_inner_reactor_skill_power_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


