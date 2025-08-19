# CoreSlotResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_slot_id** | **str** | Core slot identifier | [optional] 
**available_weapon_id** | **List[str]** | List of weapons that can unlock this core slot (refer to /meta/weapon API) | [optional] 
**available_external_component_id** | **List[str]** | List of external component that can unlock this core slot (refer to /meta/external-component API) | [optional] 
**available_core_type** | **List[str]** | List of specified core types (refer to /meta/core-type API) | [optional] 

## Example

```python
from tfd_api_client.models.core_slot_response_inner import CoreSlotResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoreSlotResponseInner from a JSON string
core_slot_response_inner_instance = CoreSlotResponseInner.from_json(json)
# print the JSON string representation of the object
print(CoreSlotResponseInner.to_json())

# convert the object into a dict
core_slot_response_inner_dict = core_slot_response_inner_instance.to_dict()
# create an instance of CoreSlotResponseInner from a dict
core_slot_response_inner_from_dict = CoreSlotResponseInner.from_dict(core_slot_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


