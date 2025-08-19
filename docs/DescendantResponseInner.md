# DescendantResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descendant_id** | **str** | Descendant identifier | [optional] 
**descendant_name** | **str** | Descendant name | [optional] 
**descendant_group_id** | **str** | Descendant group identifier (Refer to /meta/descendant-group API) | [optional] 
**descendant_image_url** | **str** | Descendant image path | [optional] 
**descendant_stat** | [**List[DescendantResponseInnerDescendantStatInner]**](DescendantResponseInnerDescendantStatInner.md) | Descendant stat information | [optional] 
**descendant_skill** | [**List[DescendantResponseInnerDescendantSkillInner]**](DescendantResponseInnerDescendantSkillInner.md) | Descendant skill information | [optional] 

## Example

```python
from tfd_api_client.models.descendant_response_inner import DescendantResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of DescendantResponseInner from a JSON string
descendant_response_inner_instance = DescendantResponseInner.from_json(json)
# print the JSON string representation of the object
print(DescendantResponseInner.to_json())

# convert the object into a dict
descendant_response_inner_dict = descendant_response_inner_instance.to_dict()
# create an instance of DescendantResponseInner from a dict
descendant_response_inner_from_dict = DescendantResponseInner.from_dict(descendant_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


