```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: Olap Common
page_number: 036
page_id: Olap Common#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:50Z
fidelity: lossless
-->

### Essential OlapCommon

```vb
[VB]
olapReport.SlicerRangeFilters.Add(New SlicerRangeFiltersInfo With {.DimensionName = "TimeFlat", .HierarchyName = "TimeFlat", .LevelName = "TimeId", .StartValue = "201010100031", .EndValue = "201010100037"})
```

|  | Number of failed connections |  |
| --- | --- | --- |
|  | Austria | Brazil | England | Germany | Poland | United States | Total |
| #null | 2 | 0 | 1 | 1 |  |  | 4 |
| Linux |  | 0 | 1 |  |  | 1 | 2 |
| Mac Os | 1 | 1 | 1 | 1 |  |  | 4 |
| Solaris |  |  |  |  |  |  | 1 |
| Windows |  | 1 | 0 | 1 | 0 |  | 2 |
| Total | 3 | 2 | 3 | 3 | 1 | 1 | 14 |

**Figure 6: Before applying range for filtering**

|  | Number of failed connections |  |
| --- | --- | --- |
|  | Austria | Brazil | England | Germany | Poland | United States | Total |
| #null | 0 |  | 1 |  |  |  | 1 |
| Linux |  | 0 | 1 |  |  |  | 1 |
| Mac Os |  |  | 1 |  |  |  | 1 |
| Solaris |  |  |  |  |  |  | 1 |
| Windows |  | 0 |  |  | 0 |  | 0 |
| Total | 0 | 0 | 3 | 0 |  | 1 | 5 |

**Figure 7: After applying range for filtering**

#### 4.3.11 Creating the OlapReport

**To create a report:**

1. **Instantiate a new object for `OlapReport`.**
2. **Create the required elements like dimension element, measure elements.**
3. **Add the created element in the desired axis (Column or Categorical, Row or Series, Filter or Slicer) elements.**
4. **Then bind the created report to the `OlapDataManager` using the `SetCurrentReport()` method or assign the report to `OlapDataManager`'s current report property.**

##### 4.3.11.1 Sample Reports for OLAP data

This section gives you the code snippet to generate different types of report for `OlapDataManager`.
```