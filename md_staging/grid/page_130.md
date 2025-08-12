```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_130.jpeg
document_name: grid
page_number: 130
page_id: grid#page_130
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:45:30Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- The page covers accessibility features and a list of controls provided by the Essential Grid for Windows Forms, focusing on support for assistive technologies and motor control constraints.
- It details the requirement for modes of operation and information retrieval that do not necessitate speech or fine motor skills, ensuring accessibility for users with disabilities.
- It provides information on various grid controls and their functionalities within the Syncfusion Essential Grid.

## Content

### Accessibility Features

| Criteria                                                                                                              | Supporting Features     | Remarks and explanations                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| for assistive hearing devices shall be provided.                                                                      |                          |                                                                                                                                                                                                                         |
| (e) At least one mode of operation and information retrieval that does not require user-speech shall be provided, or support for Assistive Technology used by people with disabilities shall be provided. | Fully Supported          | Existing grid specific APIs can be used to retrieve enough information without user speech.                                                                 |
| (f) At least one mode of operation and information retrieval that does not require fine motor control or simultaneous actions and that is operable with limited reach and strength shall be provided. | Fully Supported          | Essential Grid controls provide functionality that conforms to these criteria.                                                                                               |

### Additional Information
For more information on the accessibility features of Syncfusion products, visit Syncfusion’s accessibility web site at [http://www.syncfusion.com/accessibility](http://www.syncfusion.com/accessibility).

### 3.2 List of Controls

Essential Grid provides the following controls.

#### Grid Control
- This class is derived from GridControlBase. It is the primary class that encapsulates both the state persistence (including data persistence) and the rendering of the grid.
- Unless you are using one of the special grids (Grid Data Bound Grid, Grid Grouping control, or Grid List control), GridControl is the class you will use.
- This is a cell-oriented grid which will easily allow you to set both row and column properties, as well as set cell specific properties for the grid to hold the data.
- It can also be used in a virtual mode where the data is provided on demand or the Grid control can physically hold the data for you.

#### Grid Data Bound Grid
- This class is also derived from GridControlBase. This control is more column-oriented than the Grid control.
- It is primarily used as a grid bound to a data source that supports either IList or IDataSource. Classes such as ArrayList, DataTable, and DataView are included in this collection of possible data sources.
- Grid Data Bound Grid has a collection property called GridBoundColumns, that maintains the column...

## Page-level Navigation/TOC (if applicable)
- The page includes an overview of accessibility features for users with disabilities and a detailed description of the controls available in the Syncfusion Essential Grid.

## Cross References
- Visit Syncfusion’s accessibility web site for more information on accessibility features.
- Refer to property names such as GridBoundColumns for further details on data binding.

## RAG Annotations
<!-- tags: [accessibility, grid controls, motor control, assistive technologies, Syncfusion Essential Grid, Windows Forms, GridControlBase, Grid Data Bound Grid, GridBoundColumns] keywords: [user-speech, fine motor control, state persistence, cell-oriented grid, data persistence, virtual mode, column-oriented grid, data binding, property grid] -->
```