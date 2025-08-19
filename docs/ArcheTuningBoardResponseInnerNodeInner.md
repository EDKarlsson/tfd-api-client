# ArcheTuningBoardResponseInnerNodeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Node identifier (Refer to /meta/arche-tuning-node API) | [optional] 
**position_row** | **float** | Row coordinates of the node | [optional] 
**position_column** | **float** | Column coordinates of the node | [optional] 

## Example

```python
from tfd_api_client.models.arche_tuning_board_response_inner_node_inner import ArcheTuningBoardResponseInnerNodeInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArcheTuningBoardResponseInnerNodeInner from a JSON string
arche_tuning_board_response_inner_node_inner_instance = ArcheTuningBoardResponseInnerNodeInner.from_json(json)
# print the JSON string representation of the object
print(ArcheTuningBoardResponseInnerNodeInner.to_json())

# convert the object into a dict
arche_tuning_board_response_inner_node_inner_dict = arche_tuning_board_response_inner_node_inner_instance.to_dict()
# create an instance of ArcheTuningBoardResponseInnerNodeInner from a dict
arche_tuning_board_response_inner_node_inner_from_dict = ArcheTuningBoardResponseInnerNodeInner.from_dict(arche_tuning_board_response_inner_node_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


