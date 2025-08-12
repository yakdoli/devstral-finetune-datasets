```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_034.jpeg
document_name: Olap Common
page_number: 034
page_id: Olap Common#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:47Z
fidelity: lossless
-->

## Filtering slicer elements by range

### Overview
- This feature allows you to specify a range for filter elements in the slicer field by setting a start and end value.
- Multiple ranges can be added to the filter elements in the slicer field.
- It eliminates the need to manually enter each member, making filtering easier.

### Content

#### Use Case Scenarios
It is not required to enter each member manually. This makes filtering easy.

#### Class

| Name                    | Description                                                                                                                                                                                                                      |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SlicerRangeFiltersInfo  | Used to filter values from one range to another. Unique name of the member element for start and end value need to be specified. The name of the member element can also be specified for start and end value when customer builds the unique name*. |

*Note: The name of the member element can be specified only when the name is formed with the dimension name, hierarchy name, and level name.*

#### Constructor

| Syntax                                                                      | Description                                                                                   | Parameter                                                                                       |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| SlicerRangeFiltersInfo(string startValueUniqueName, string endValueUniqueName) | Initializes SlicerRangeFiltersInfo with unique name as star and end values.                | Unique name for start and end value.                                                           |
| SlicerRangeFiltersInfo(string dimensionName, string hierarchyName, string levelName, string startValueName, string endValueName) | Initializes SlicerRangeFiltersInfo with name of dimension, hierarchy, level, star value and end value. | Name for dimension, hierarchy, level, start value and end value. |

#### Properties

The following table consists of the SlicerRangeFiltersInfo class's properties:

| Property     | Description | Type    | Data Type | Reference links |
|--------------|-------------|---------|-----------|-----------------|
|              |             |         |           |                 |

## Page-level Navigation/TOC (if applicable)
- [ ] None explicitly mentioned on the page.

## Cross References
- See also: None explicitly mentioned on the page.

<!-- tags: [Olap Common, filtering, slicer, WinForms,-range, ranges, SlicerRangeFiltersInfo] keywords: [slicer elements, range filtering, unique name, dimension name, hierarchy name, level name, SlicerRangeFiltersInfo, properties] -->
```