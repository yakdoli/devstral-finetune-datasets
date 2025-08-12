```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_293.jpeg
document_name: tools
page_number: 293
page_id: tools#page_293
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:03:34Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

![Figure 124: PreferredHeight = "100"; PreferredWidth = "300"](image.png)
*Figure 124: PreferredHeight = "100"; PreferredWidth = "300"* 

## Overview
- Discusses data settings for the AutoComplete control.
- Explains properties like CategoryName and DataSource specific to data management in AutoComplete controls.

## Content
### 3.5.1.1.3.2 DataSource

This section will discuss the data settings for the AutoComplete control, in the below topics.

#### 3.5.1.1.3.2.1 Data Settings

The data for the autocompletion will be maintained by the AutoComplete control itself. This is referred to as a History Data List mode. The below properties deals with data settings.

| AutoComplete Properties | Description |
| --- | --- |
| CategoryName | Specifies a unique or shared name that can be given to an AutoComplete control so that it can persist the values under that name. For example, if the CategoryName "URL" is provided for an AutoComplete control on a particular form, all values persisted by that AutoComplete control will also be accessible to other AutoComplete controls on others forms or on the same form with the CategoryName "URL". |
| DataSource | Sets the Datasource to the Autocomplete control. The AutoComplete control automatically picks the "History Data List" mode or "Data source" mode based on the values set for the DataSource property. If the datasource property is set to NULL (default value is NULL), the control defaults to History Data List mode. It is to be |

## API Reference (if applicable)
- Sections describe properties like CategoryName and DataSource for managing data in AutoComplete controls.

## Code Examples (multi-language supported)
- No explicit code examples are present in this excerpt.

## Page-level Navigation/TOC (if applicable)
- This section is part of a detailed guide on AutoComplete control data settings.

## Cross References
- The section provides detailed explanations of CategoryName and DataSource properties.

## RAG Annotations
<!-- tags: AUTO_COMPLETE, DATA_SETTINGS, SYNCFUSION_WINFORMS, v11.4.0.26
keywords: AutoComplete control, CategoryName, DataSource, History Data List -->
```