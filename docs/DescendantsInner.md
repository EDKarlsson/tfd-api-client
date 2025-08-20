# DescendantsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descendant_id** | **str** | Descendant identifier | [optional] 
**descendant_name** | **str** | Descendant name | [optional] 
**descendant_group_id** | **str** | Descendant group identifier (Refer to /meta/descendant-group API) | [optional] 
**descendant_image_url** | **str** | Descendant image path | [optional] 
**descendant_stat** | [**List[DescendantsInnerDescendantStatInner]**](DescendantsInnerDescendantStatInner.md) | Descendant stat information | [optional] 
**descendant_skill** | [**List[DescendantsInnerDescendantSkillInner]**](DescendantsInnerDescendantSkillInner.md) | Descendant skill information | [optional] 

## Example

```python
from tfd_api_client.models.descendants_inner import DescendantsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DescendantsInner from a JSON string
descendants_inner_instance = DescendantsInner.from_json(json)
# print the JSON string representation of the object
print(DescendantsInner.to_json())

# convert the object into a dict
descendants_inner_dict = descendants_inner_instance.to_dict()
# create an instance of DescendantsInner from a dict
descendants_inner_from_dict = DescendantsInner.from_dict(descendants_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


