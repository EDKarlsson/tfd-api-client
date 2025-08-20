# ConsumableMaterialsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumable_material_id** | **str** | Consumable Item identifier | [optional] 
**image_url** | **str** | Consumable Item image path | [optional] 
**consumable_material_name** | **str** | Consumable Item name | [optional] 
**required_mastery_rank_level** | **float** | Required Mastery Rank | [optional] 
**material_type** | **str** | Material type | [optional] 
**acquisition_detail** | **List[str]** | Acquisition source (refer to /meta/acquisition-detail API) | [optional] 
**amorphous_reward** | **List[str]** | Amorphous Material open reward (refer to /meta/amorphous-reward API) | [optional] 
**amorphous_open_condition** | **List[str]** | Amorphous Material opening location (refer to /meta/amorphous-open-condition-description API) | [optional] 

## Example

```python
from tfd_api_client.models.consumable_materials_inner import ConsumableMaterialsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumableMaterialsInner from a JSON string
consumable_materials_inner_instance = ConsumableMaterialsInner.from_json(json)
# print the JSON string representation of the object
print(ConsumableMaterialsInner.to_json())

# convert the object into a dict
consumable_materials_inner_dict = consumable_materials_inner_instance.to_dict()
# create an instance of ConsumableMaterialsInner from a dict
consumable_materials_inner_from_dict = ConsumableMaterialsInner.from_dict(consumable_materials_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


