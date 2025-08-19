# UserDescendantCustomizingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customizing_item_slot_id** | **str** | Customization item slot identifier | [optional] 
**customizing_item_type** | **str** | Customization item type | [optional] 
**customizing_item_id** | **str** | Customization item identifier (Refer to /meta/customizing-item API) | [optional] 
**customizing_item_evolution_stage** | **float** | Evolution stage of the customization item | [optional] 
**customizing_item_current_evolution_stage** | **float** | Currently selected evolution stage of the customization item | [optional] 
**paint** | [**List[UserDescendantCustomizingInnerPaintInner]**](UserDescendantCustomizingInnerPaintInner.md) | Paint information | [optional] 

## Example

```python
from tfd_api_client.models.user_descendant_customizing_inner import UserDescendantCustomizingInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserDescendantCustomizingInner from a JSON string
user_descendant_customizing_inner_instance = UserDescendantCustomizingInner.from_json(json)
# print the JSON string representation of the object
print(UserDescendantCustomizingInner.to_json())

# convert the object into a dict
user_descendant_customizing_inner_dict = user_descendant_customizing_inner_instance.to_dict()
# create an instance of UserDescendantCustomizingInner from a dict
user_descendant_customizing_inner_from_dict = UserDescendantCustomizingInner.from_dict(user_descendant_customizing_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


