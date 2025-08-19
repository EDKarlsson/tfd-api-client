# UserExternalComponentExternalComponentInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_component_slot_id** | **str** | External component slot identifier | [optional] 
**external_component_id** | **str** | External component identifier (Refer to /meta/external-component API) | [optional] 
**external_component_level** | **float** | External component level | [optional] 
**external_component_additional_stat** | [**List[UserExternalComponentExternalComponentInnerExternalComponentAdditionalStatInner]**](UserExternalComponentExternalComponentInnerExternalComponentAdditionalStatInner.md) | External component random option information | [optional] 
**core_unlock_flag** | **str** | Core unlock status (0:Locked | 1:Unlocked) | [optional] 
**core** | [**List[UserWeaponWeaponInnerCoreInner]**](UserWeaponWeaponInnerCoreInner.md) | Core option information | [optional] 

## Example

```python
from tfd_api_client.models.user_external_component_external_component_inner import UserExternalComponentExternalComponentInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserExternalComponentExternalComponentInner from a JSON string
user_external_component_external_component_inner_instance = UserExternalComponentExternalComponentInner.from_json(json)
# print the JSON string representation of the object
print(UserExternalComponentExternalComponentInner.to_json())

# convert the object into a dict
user_external_component_external_component_inner_dict = user_external_component_external_component_inner_instance.to_dict()
# create an instance of UserExternalComponentExternalComponentInner from a dict
user_external_component_external_component_inner_from_dict = UserExternalComponentExternalComponentInner.from_dict(user_external_component_external_component_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


