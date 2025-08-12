```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: Olap Common
page_number: 024
page_id: Olap Common#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:07Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Describes the properties and functionalities of OlapReport related to calculations, categorical elements, current cube name, filter elements, and report settings.
- Defines settings for display options such as showing or hiding empty column/row data, expanders, and slicer elements.

## Content

### Properties Table

The following table lists the properties of the `OlapReport` and their respective descriptions, types, accepted values, and reference links:

| Name                  | Description                                                                                           | Type     | Value it accepts | Reference Link           |
|-----------------------|-------------------------------------------------------------------------------------------------------|----------|------------------|--------------------------|
| CalculatedMembers     | Used to set and get the calculated members of the `OlapReport`.                                      | Items    | Items            | CalculatedMembers        |
| CategoricalElements   | Contains the element that are said to be in categorical axis. We can add an element and get the collection of elements that comes under the categorical axis.                    | Items    | Items            | -                        |
| CurrentCubeName      | Used to set or get the current cube name of the Report.                                               | string   | String           | -                        |
| FilterElements       | Contains elements that are subjected to Filter constraints and a filter expression along the measure on which the filter expression is built.                             | Items    | Items            | FilterElements           |
| Name                 | Used to set or get the report name.                                                                    | string   | String           | -                        |
| SeriesElements       | Contains elements that are said to be in series axis. We can add an element and get the collection of elements that comes under the categorical axis.                          | Items    | Items            | -                        |
| ShowEmptyColumnData  | Used to show/hide the empty column in the result set.                                                  | bool     | True/False       | -                        |
| ShowemptyRowData     | Used to show/hide the empty row in the result set.                                                     | bool     | True/False       | -                        |
| ShowExpanders        | Used to show/hide the expander buttons in the Olap controls.                                           | bool     | True/False       | ShowExpanders            |
| SliceElements        | Contains the element that are said to be in slicer axis. We can add an element and get the                                                                            | Items    | Items            | -                        |

## Page-level Navigation/TOC (if applicable)
- If the page contains a local Table of Contents, it should be listed here as a bullet or numbered list.

## Cross References
- See also: OlapReport, CalculatedMembers, FilterElements, Report Settings

## RAG Annotations
<!-- tags: [product, syncfusion-winforms, olapreport, olapcommon, reportsettings] keywords: [calculated members, categorical elements, current cube name, filter elements, report name, series elements, show empty column data, show empty row data, show expanders, slice elements] -->
```