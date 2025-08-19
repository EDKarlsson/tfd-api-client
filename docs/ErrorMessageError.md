# ErrorMessageError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Error name | [optional] 
**message** | **str** | Error message | [optional] 

## Example

```python
from tfd_api_client.models.error_message_error import ErrorMessageError

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorMessageError from a JSON string
error_message_error_instance = ErrorMessageError.from_json(json)
# print the JSON string representation of the object
print(ErrorMessageError.to_json())

# convert the object into a dict
error_message_error_dict = error_message_error_instance.to_dict()
# create an instance of ErrorMessageError from a dict
error_message_error_from_dict = ErrorMessageError.from_dict(error_message_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


