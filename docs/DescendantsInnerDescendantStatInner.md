# DescendantsInnerDescendantStatInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | Level | [optional] 
**stat_detail** | [**List[DescendantsInnerDescendantStatInnerStatDetailInner]**](DescendantsInnerDescendantStatInnerStatDetailInner.md) | Descendant details | [optional] 

## Example

```python
from tfd_api_client.models.descendants_inner_descendant_stat_inner import DescendantsInnerDescendantStatInner

# TODO update the JSON string below
json = "{}"
# create an instance of DescendantsInnerDescendantStatInner from a JSON string
descendants_inner_descendant_stat_inner_instance = DescendantsInnerDescendantStatInner.from_json(json)
# print the JSON string representation of the object
print(DescendantsInnerDescendantStatInner.to_json())

# convert the object into a dict
descendants_inner_descendant_stat_inner_dict = descendants_inner_descendant_stat_inner_instance.to_dict()
# create an instance of DescendantsInnerDescendantStatInner from a dict
descendants_inner_descendant_stat_inner_from_dict = DescendantsInnerDescendantStatInner.from_dict(descendants_inner_descendant_stat_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


