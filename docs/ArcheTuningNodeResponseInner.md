# ArcheTuningNodeResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Node identifier | [optional] 
**node_name** | **str** | Node name | [optional] 
**node_image_url** | **str** | Node image URL | [optional] 
**node_type** | **str** | Node type | [optional] 
**tier_id** | **str** | Node tier identifier (Refer to /meta/tier API) | [optional] 
**required_tuning_point** | **float** | Required points | [optional] 
**node_effect** | [**List[ArcheTuningNodeResponseInnerNodeEffectInner]**](ArcheTuningNodeResponseInnerNodeEffectInner.md) |  | [optional] 

## Example

```python
from tfd_api_client.models.arche_tuning_node_response_inner import ArcheTuningNodeResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArcheTuningNodeResponseInner from a JSON string
arche_tuning_node_response_inner_instance = ArcheTuningNodeResponseInner.from_json(json)
# print the JSON string representation of the object
print(ArcheTuningNodeResponseInner.to_json())

# convert the object into a dict
arche_tuning_node_response_inner_dict = arche_tuning_node_response_inner_instance.to_dict()
# create an instance of ArcheTuningNodeResponseInner from a dict
arche_tuning_node_response_inner_from_dict = ArcheTuningNodeResponseInner.from_dict(arche_tuning_node_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


