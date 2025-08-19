# DescendantResponseInnerDescendantStatInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | Level | [optional] 
**stat_detail** | [**List[DescendantResponseInnerDescendantStatInnerStatDetailInner]**](DescendantResponseInnerDescendantStatInnerStatDetailInner.md) | Descendant details | [optional] 

## Example

```python
from tfd_api_client.models.descendant_response_inner_descendant_stat_inner import DescendantResponseInnerDescendantStatInner

# TODO update the JSON string below
json = "{}"
# create an instance of DescendantResponseInnerDescendantStatInner from a JSON string
descendant_response_inner_descendant_stat_inner_instance = DescendantResponseInnerDescendantStatInner.from_json(json)
# print the JSON string representation of the object
print(DescendantResponseInnerDescendantStatInner.to_json())

# convert the object into a dict
descendant_response_inner_descendant_stat_inner_dict = descendant_response_inner_descendant_stat_inner_instance.to_dict()
# create an instance of DescendantResponseInnerDescendantStatInner from a dict
descendant_response_inner_descendant_stat_inner_from_dict = DescendantResponseInnerDescendantStatInner.from_dict(descendant_response_inner_descendant_stat_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


