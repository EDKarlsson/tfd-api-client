# ExternalComponentsInnerBaseStatInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | External component level | [optional] 
**stat_id** | **str** | External component effect type | [optional] 
**stat_value** | **float** | External component effect value | [optional] 

## Example

```python
from tfd_api_client.models.external_components_inner_base_stat_inner import ExternalComponentsInnerBaseStatInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalComponentsInnerBaseStatInner from a JSON string
external_components_inner_base_stat_inner_instance = ExternalComponentsInnerBaseStatInner.from_json(json)
# print the JSON string representation of the object
print(ExternalComponentsInnerBaseStatInner.to_json())

# convert the object into a dict
external_components_inner_base_stat_inner_dict = external_components_inner_base_stat_inner_instance.to_dict()
# create an instance of ExternalComponentsInnerBaseStatInner from a dict
external_components_inner_base_stat_inner_from_dict = ExternalComponentsInnerBaseStatInner.from_dict(external_components_inner_base_stat_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


