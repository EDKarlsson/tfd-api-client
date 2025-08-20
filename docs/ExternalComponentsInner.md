# ExternalComponentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_component_id** | **str** | External component identifier | [optional] 
**external_component_name** | **str** | External component name | [optional] 
**image_url** | **str** | External component image path | [optional] 
**external_component_equipment_type** | **str** | External component equipment part | [optional] 
**external_component_tier_id** | **str** | External components tier  (Refer to /meta/tier API) | [optional] 
**available_core_slot** | **str** | List of unlockable core slots (Refer to the /meta/core-slot API) | [optional] 
**base_stat** | [**List[ExternalComponentsInnerBaseStatInner]**](ExternalComponentsInnerBaseStatInner.md) | External component effect by level information | [optional] 
**set_option_detail** | [**List[ExternalComponentsInnerSetOptionDetailInner]**](ExternalComponentsInnerSetOptionDetailInner.md) | External component set option information | [optional] 

## Example

```python
from tfd_api_client.models.external_components_inner import ExternalComponentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalComponentsInner from a JSON string
external_components_inner_instance = ExternalComponentsInner.from_json(json)
# print the JSON string representation of the object
print(ExternalComponentsInner.to_json())

# convert the object into a dict
external_components_inner_dict = external_components_inner_instance.to_dict()
# create an instance of ExternalComponentsInner from a dict
external_components_inner_from_dict = ExternalComponentsInner.from_dict(external_components_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


