# ExternalComponentResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_component_id** | **str** | External component identifier | [optional] 
**external_component_name** | **str** | External component name | [optional] 
**image_url** | **str** | External component image path | [optional] 
**external_component_equipment_type** | **str** | External component equipment part | [optional] 
**external_component_tier_id** | **str** | External components tier  (Refer to /meta/tier API) | [optional] 
**available_core_slot** | **str** | List of unlockable core slots (Refer to the /meta/core-slot API) | [optional] 
**base_stat** | [**List[ExternalComponentResponseInnerBaseStatInner]**](ExternalComponentResponseInnerBaseStatInner.md) | External component effect by level information | [optional] 
**set_option_detail** | [**List[ExternalComponentResponseInnerSetOptionDetailInner]**](ExternalComponentResponseInnerSetOptionDetailInner.md) | External component set option information | [optional] 

## Example

```python
from tfd_api_client.models.external_component_response_inner import ExternalComponentResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalComponentResponseInner from a JSON string
external_component_response_inner_instance = ExternalComponentResponseInner.from_json(json)
# print the JSON string representation of the object
print(ExternalComponentResponseInner.to_json())

# convert the object into a dict
external_component_response_inner_dict = external_component_response_inner_instance.to_dict()
# create an instance of ExternalComponentResponseInner from a dict
external_component_response_inner_from_dict = ExternalComponentResponseInner.from_dict(external_component_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


