# CustomizingItemResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customizing_item_id** | **str** | Customization item identifier | [optional] 
**customizing_item_name** | **str** | Customization item name | [optional] 
**customizing_item_type** | **str** | Customization item type | [optional] 
**customizing_item_tier_id** | **str** | Customization item tier (Refer to /meta/tier API) | [optional] 
**customizing_item_description** | **str** | Customization item description | [optional] 
**customizing_item_image_url** | **str** | Customization item image path | [optional] 
**customizing_item_evolution_stage** | [**List[CustomizingItemResponseInnerCustomizingItemEvolutionStageInner]**](CustomizingItemResponseInnerCustomizingItemEvolutionStageInner.md) | Evolution stage information of the customization item | [optional] 
**available_descendant** | **List[str]** | Applicable descendant list (Refer to /meta/descendant API) | [optional] 

## Example

```python
from tfd_api_client.models.customizing_item_response_inner import CustomizingItemResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizingItemResponseInner from a JSON string
customizing_item_response_inner_instance = CustomizingItemResponseInner.from_json(json)
# print the JSON string representation of the object
print(CustomizingItemResponseInner.to_json())

# convert the object into a dict
customizing_item_response_inner_dict = customizing_item_response_inner_instance.to_dict()
# create an instance of CustomizingItemResponseInner from a dict
customizing_item_response_inner_from_dict = CustomizingItemResponseInner.from_dict(customizing_item_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


