# DescendantsInnerDescendantSkillInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill_type** | **str** | Skill type (active/passive) | [optional] 
**skill_name** | **str** | Skill name | [optional] 
**element_type** | **str** | Skill type | [optional] 
**arche_type** | **str** | Arche type | [optional] 
**skill_image_url** | **str** | Skill icon image path | [optional] 
**skill_description** | **str** | Skill description | [optional] 

## Example

```python
from tfd_api_client.models.descendants_inner_descendant_skill_inner import DescendantsInnerDescendantSkillInner

# TODO update the JSON string below
json = "{}"
# create an instance of DescendantsInnerDescendantSkillInner from a JSON string
descendants_inner_descendant_skill_inner_instance = DescendantsInnerDescendantSkillInner.from_json(json)
# print the JSON string representation of the object
print(DescendantsInnerDescendantSkillInner.to_json())

# convert the object into a dict
descendants_inner_descendant_skill_inner_dict = descendants_inner_descendant_skill_inner_instance.to_dict()
# create an instance of DescendantsInnerDescendantSkillInner from a dict
descendants_inner_descendant_skill_inner_from_dict = DescendantsInnerDescendantSkillInner.from_dict(descendants_inner_descendant_skill_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


