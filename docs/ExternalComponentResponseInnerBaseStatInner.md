# ExternalComponentResponseInnerBaseStatInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | External component level | [optional] 
**stat_id** | **str** | External component effect type | [optional] 
**stat_value** | **float** | External component effect value | [optional] 

## Example

```python
from tfd_api_client.models.external_component_response_inner_base_stat_inner import ExternalComponentResponseInnerBaseStatInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalComponentResponseInnerBaseStatInner from a JSON string
external_component_response_inner_base_stat_inner_instance = ExternalComponentResponseInnerBaseStatInner.from_json(json)
# print the JSON string representation of the object
print(ExternalComponentResponseInnerBaseStatInner.to_json())

# convert the object into a dict
external_component_response_inner_base_stat_inner_dict = external_component_response_inner_base_stat_inner_instance.to_dict()
# create an instance of ExternalComponentResponseInnerBaseStatInner from a dict
external_component_response_inner_base_stat_inner_from_dict = ExternalComponentResponseInnerBaseStatInner.from_dict(external_component_response_inner_base_stat_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


