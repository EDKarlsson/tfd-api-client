# ResearchInnerResearchMaterialInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_type** | **str** | Metadata type of the research material item | [optional] 
**meta_id** | **str** | Identifier of the research material item | [optional] 
**material_count** | **float** | Quantity of the research material item | [optional] 
**research_id** | **List[str]** | Research identifier of the research material item (refer to /meta/research API) | [optional] 

## Example

```python
from tfd_api_client.models.research_inner_research_material_inner import ResearchInnerResearchMaterialInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResearchInnerResearchMaterialInner from a JSON string
research_inner_research_material_inner_instance = ResearchInnerResearchMaterialInner.from_json(json)
# print the JSON string representation of the object
print(ResearchInnerResearchMaterialInner.to_json())

# convert the object into a dict
research_inner_research_material_inner_dict = research_inner_research_material_inner_instance.to_dict()
# create an instance of ResearchInnerResearchMaterialInner from a dict
research_inner_research_material_inner_from_dict = ResearchInnerResearchMaterialInner.from_dict(research_inner_research_material_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


