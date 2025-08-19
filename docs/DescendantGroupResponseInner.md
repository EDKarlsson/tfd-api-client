# DescendantGroupResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descendant_group_id** | **str** | Descendant group identifier | [optional] 
**descendant_group_name** | **str** | Descendant group name | [optional] 

## Example

```python
from tfd_api_client.models.descendant_group_response_inner import DescendantGroupResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of DescendantGroupResponseInner from a JSON string
descendant_group_response_inner_instance = DescendantGroupResponseInner.from_json(json)
# print the JSON string representation of the object
print(DescendantGroupResponseInner.to_json())

# convert the object into a dict
descendant_group_response_inner_dict = descendant_group_response_inner_instance.to_dict()
# create an instance of DescendantGroupResponseInner from a dict
descendant_group_response_inner_from_dict = DescendantGroupResponseInner.from_dict(descendant_group_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


