# ArcheTuningNodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Node identifier | [optional] 
**node_name** | **str** | Node name | [optional] 
**node_image_url** | **str** | Node image URL | [optional] 
**node_type** | **str** | Node type | [optional] 
**tier_id** | **str** | Node tier identifier (Refer to /meta/tier API) | [optional] 
**required_tuning_point** | **float** | Required points | [optional] 
**node_effect** | [**List[ArcheTuningNodesInnerNodeEffectInner]**](ArcheTuningNodesInnerNodeEffectInner.md) |  | [optional] 

## Example

```python
from tfd_api_client.models.arche_tuning_nodes_inner import ArcheTuningNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArcheTuningNodesInner from a JSON string
arche_tuning_nodes_inner_instance = ArcheTuningNodesInner.from_json(json)
# print the JSON string representation of the object
print(ArcheTuningNodesInner.to_json())

# convert the object into a dict
arche_tuning_nodes_inner_dict = arche_tuning_nodes_inner_instance.to_dict()
# create an instance of ArcheTuningNodesInner from a dict
arche_tuning_nodes_inner_from_dict = ArcheTuningNodesInner.from_dict(arche_tuning_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


