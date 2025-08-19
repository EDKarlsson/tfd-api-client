# AcquisitionDetailResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquisition_detail_id** | **str** | Identifier of the acquisition source | [optional] 
**acquisition_detail_name** | **str** | Acquisition source name | [optional] 

## Example

```python
from tfd_api_client.models.acquisition_detail_response_inner import AcquisitionDetailResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AcquisitionDetailResponseInner from a JSON string
acquisition_detail_response_inner_instance = AcquisitionDetailResponseInner.from_json(json)
# print the JSON string representation of the object
print(AcquisitionDetailResponseInner.to_json())

# convert the object into a dict
acquisition_detail_response_inner_dict = acquisition_detail_response_inner_instance.to_dict()
# create an instance of AcquisitionDetailResponseInner from a dict
acquisition_detail_response_inner_from_dict = AcquisitionDetailResponseInner.from_dict(acquisition_detail_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


