```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: Olap Common
page_number: 035
page_id: Olap Common#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:29Z
fidelity: lossless
-->

### Overview
- Describes how to specify dimension, hierarchy, and level names for filtering.
- Explains methods to add a range for filter elements in slicer fields.
- Includes examples in C# and VB for implementing range filters.

### Content

#### Filter Specifications

| DimensionName | Specify the dimension name | None | String | NA |
|---------------|---------------------------|------|--------|----|
| HierarchyName | Specify the hierarchy name | None | String | NA |
| LevelName     | Specify the level name    | None | String | NA |
| StartValue    | Specify the unique name or name of the member element* | None | String | NA |
| EndValue      | Specify the unique name or name of the member element* | None | String | NA |

* **Note**: Name of the member element can be specified only when the name is formed with dimension name, hierarchy name, and level name.

#### Adding a Range for Filter Elements in Slicer Field

There are two methods to add range for the filter elements in a slicer field.

1. **First Method**: Specify the unique name for start and end value.
   Example in C#:
   ```csharp
   olapReport.SlicerRangeFilters.Add(new SlicerRangeFiltersInfo("[TimeFlat].[201010100031]", "[TimeFlat].[201010100037]"));
   ```

   Example in VB:
   ```vb
   olapReport.SlicerRangeFilters.Add(New SlicerRangeFiltersInfo("[TimeFlat].[201010100031]", "[TimeFlat].[201010100037]"))
   ```

2. **Second Method**: Specify the member name along with dimension name, hierarchy name, and level name. Entering the unique name for start and end value is not mandatory.
   Example in C#:
   ```csharp
   olapReport.SlicerRangeFilters.Add(new SlicerRangeFiltersInfo { DimensionName = "TimeFlat", HierarchyName = "TimeFlat", LevelName = "TimeId", StartValue = "201010100031", EndValue = "201010100037" });
   ```

#### Conclusion

This section covers the essential aspects of specifying filter elements in an OLAP report, including the use of dimension, hierarchy, and level names, as well as adding ranges to filter elements in slicer fields. The provided code examples help illustrate the implementation in C# and VB.

<!-- tags: [Syncfusion, Winforms, OLAP, Slicer Filters, Dimension, Hierarchy, Level, Range] keywords: [DimensionName, HierarchyName, LevelName, StartValue, EndValue, SlicerRangeFilters, SlicerRangeFiltersInfo] -->
```