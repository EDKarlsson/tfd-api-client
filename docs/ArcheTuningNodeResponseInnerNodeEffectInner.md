# ArcheTuningNodeResponseInnerNodeEffectInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stat_id** | **str** | Stat identifier (Refer to /meta/stat API) | [optional] 
**stat_value** | **float** | Stat effect value | [optional] 
**operator_type** | **str** | Stat operation type (Add:addition, Multiply:multiplication) | [optional] 

## Example

```python
from tfd_api_client.models.arche_tuning_node_response_inner_node_effect_inner import ArcheTuningNodeResponseInnerNodeEffectInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArcheTuningNodeResponseInnerNodeEffectInner from a JSON string
arche_tuning_node_response_inner_node_effect_inner_instance = ArcheTuningNodeResponseInnerNodeEffectInner.from_json(json)
# print the JSON string representation of the object
print(ArcheTuningNodeResponseInnerNodeEffectInner.to_json())

# convert the object into a dict
arche_tuning_node_response_inner_node_effect_inner_dict = arche_tuning_node_response_inner_node_effect_inner_instance.to_dict()
# create an instance of ArcheTuningNodeResponseInnerNodeEffectInner from a dict
arche_tuning_node_response_inner_node_effect_inner_from_dict = ArcheTuningNodeResponseInnerNodeEffectInner.from_dict(arche_tuning_node_response_inner_node_effect_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


