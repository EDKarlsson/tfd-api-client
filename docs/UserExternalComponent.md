# UserExternalComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ouid** | **str** | OUID | [optional] 
**user_name** | **str** | Nickname | [optional] 
**external_component** | [**List[UserExternalComponentExternalComponentInner]**](UserExternalComponentExternalComponentInner.md) | External component information | [optional] 

## Example

```python
from tfd_api_client.models.user_external_component import UserExternalComponent

# TODO update the JSON string below
json = "{}"
# create an instance of UserExternalComponent from a JSON string
user_external_component_instance = UserExternalComponent.from_json(json)
# print the JSON string representation of the object
print(UserExternalComponent.to_json())

# convert the object into a dict
user_external_component_dict = user_external_component_instance.to_dict()
# create an instance of UserExternalComponent from a dict
user_external_component_from_dict = UserExternalComponent.from_dict(user_external_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


