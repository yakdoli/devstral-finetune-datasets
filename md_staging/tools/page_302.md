```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_302.jpeg
document_name: tools
page_number: 302
page_id: tools#page_302
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:40Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to add DataColumns to the AutoCompletePopup using the AutoCompleteDataColumn properties.
- Explains various properties of AutoCompleteDataColumn and their usage.
- Provides an illustration of the AutoCompleteDataColumnInfo Collection Editor.

## Content

### AutoCompleteDataColumn Properties

Below are the AutoCompleteDataColumn properties and their descriptions:

| **AutoCompleteDataColumn Properties** | **Description** |
|---------------------------------------|-----------------|
| **ColumnHeaderText**                 | Represents the text for the column header. |
| **MatchingColumn**                   | Column that will be used by the AutoComplete control to perform matching with the current content (at runtime) of the target control. |
| **ImageColumn**                      | Column which is filled with data that is just the index into the image list that has been assigned to the AutoComplete control. See Image Settings for Details. |
| **MinColumnWidth**                   | Set minimum width for the column. |
| **Visible**                          | Shows or hides the column at runtime. |

### Figure 130: Adding DataColumns to the AutoCompletePopup

The screenshot below shows the "AutoCompleteDataColumnInfo Collection Editor" interface where you can add and configure DataColumns to be used with the AutoComplete-popup feature.

![AutoCompleteDataColumn Collection Editor](Figure_130.png)

#### Description of Properties Shown in the Figure
- **autoCompleteDataColumnInfo3**:
  - **ColumnHeaderText**: Title
  - **ColumnName**: Title
  - **ImageColumn**: False
  - **MatchingColumn**: True
  - **MinColumnWidth**: 100
  - **Visible**: True

- **autoCompleteDataColumnInfo4**:
  - Similar properties can be configured for additional columns.

### Page-level Navigation/TOC (if applicable)
- This section focuses on configuring and using DataColumns with the AutoComplete control in Windows Forms applications.

### Cross References
- Refer to the "Image Settings" section for details on handling ImageColumn properties.

### Code Examples
- No specific code is shown in this section, but configuration can be done through the AutoCompleteDataColumnInfo editor or programmatically.

### API Reference
- Namespace: Syncfusion.Windows.Forms.Tools
- Class: AutoCompleteDataColumn
- Properties:
  - **ColumnHeaderText**: string
  - **MatchingColumn**: bool
  - **ImageColumn**: bool
  - **MinColumnWidth**: int
  - **Visible**: bool

<!-- tags: [essential-tools, windows-forms, autocompletetoolkit, autocomplete-popup, autocompletedatacolumninfo, autocompletedatacolumn, properties, configuration] keywords: [auto-complete, data-columns, matching-column, image-column, min-column-width, visibility, runtime, toolkit] -->
```