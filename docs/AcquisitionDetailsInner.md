# AcquisitionDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquisition_detail_id** | **str** | Identifier of the acquisition source | [optional] 
**acquisition_detail_name** | **str** | Acquisition source name | [optional] 

## Example

```python
from tfd_api_client.models.acquisition_details_inner import AcquisitionDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AcquisitionDetailsInner from a JSON string
acquisition_details_inner_instance = AcquisitionDetailsInner.from_json(json)
# print the JSON string representation of the object
print(AcquisitionDetailsInner.to_json())

# convert the object into a dict
acquisition_details_inner_dict = acquisition_details_inner_instance.to_dict()
# create an instance of AcquisitionDetailsInner from a dict
acquisition_details_inner_from_dict = AcquisitionDetailsInner.from_dict(acquisition_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


