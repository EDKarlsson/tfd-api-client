# ExternalComponentResponseInnerSetOptionDetailInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set_option** | **str** | External component set option type | [optional] 
**set_count** | **float** | Number of external component sets | [optional] 
**set_option_effect** | **str** | External component set option set effect | [optional] 

## Example

```python
from tfd_api_client.models.external_component_response_inner_set_option_detail_inner import ExternalComponentResponseInnerSetOptionDetailInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalComponentResponseInnerSetOptionDetailInner from a JSON string
external_component_response_inner_set_option_detail_inner_instance = ExternalComponentResponseInnerSetOptionDetailInner.from_json(json)
# print the JSON string representation of the object
print(ExternalComponentResponseInnerSetOptionDetailInner.to_json())

# convert the object into a dict
external_component_response_inner_set_option_detail_inner_dict = external_component_response_inner_set_option_detail_inner_instance.to_dict()
# create an instance of ExternalComponentResponseInnerSetOptionDetailInner from a dict
external_component_response_inner_set_option_detail_inner_from_dict = ExternalComponentResponseInnerSetOptionDetailInner.from_dict(external_component_response_inner_set_option_detail_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


