# DescendantGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descendant_group_id** | **str** | Descendant group identifier | [optional] 
**descendant_group_name** | **str** | Descendant group name | [optional] 

## Example

```python
from tfd_api_client.models.descendant_groups_inner import DescendantGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DescendantGroupsInner from a JSON string
descendant_groups_inner_instance = DescendantGroupsInner.from_json(json)
# print the JSON string representation of the object
print(DescendantGroupsInner.to_json())

# convert the object into a dict
descendant_groups_inner_dict = descendant_groups_inner_instance.to_dict()
# create an instance of DescendantGroupsInner from a dict
descendant_groups_inner_from_dict = DescendantGroupsInner.from_dict(descendant_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


