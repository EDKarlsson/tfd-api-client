# UserDescendantCustomizingInnerPaintInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customizing_item_slot_id** | **str** | Paint customization slot identifier | [optional] 
**customizing_item_type** | **str** | Paint customization item identifier | [optional] 
**customizing_item_id** | **str** | Paint customization item identifier (Refer to /meta/customizing-item API) | [optional] 

## Example

```python
from tfd_api_client.models.user_descendant_customizing_inner_paint_inner import UserDescendantCustomizingInnerPaintInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserDescendantCustomizingInnerPaintInner from a JSON string
user_descendant_customizing_inner_paint_inner_instance = UserDescendantCustomizingInnerPaintInner.from_json(json)
# print the JSON string representation of the object
print(UserDescendantCustomizingInnerPaintInner.to_json())

# convert the object into a dict
user_descendant_customizing_inner_paint_inner_dict = user_descendant_customizing_inner_paint_inner_instance.to_dict()
# create an instance of UserDescendantCustomizingInnerPaintInner from a dict
user_descendant_customizing_inner_paint_inner_from_dict = UserDescendantCustomizingInnerPaintInner.from_dict(user_descendant_customizing_inner_paint_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


