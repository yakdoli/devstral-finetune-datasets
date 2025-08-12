```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_329.jpeg
document_name: tools
page_number: 329
page_id: tools#page_329
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:42Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Introduces the **AutoCompleteControl** properties and their configuration using the ComboBoxAutoComplete Property Grid.
- Details setting a **DataView** as the **DataSource** for ComboBoxAutoComplete.

## Content

### AutoCompleteControl Properties

The AutoCompleteControl properties can be accessed through the ComboBoxAutoComplete Property Grid.

#### Figure: AutoCompleteControl Properties Accessed Through ComboBoxAutoComplete Property Grid
![Figure 142: AutoCompleteControl Properties Accessed Through ComboBoxAutoComplete Property Grid](image.png)

### Setting DataSource

#### See Also
- **DataSource**

#### 3.5.1.2.3.3 Datasource
The following steps set a DataView as the DataSource of ComboBoxAutoComplete.

1. Drag and drop **SqlDataAdapter or OleDbDataAdapter** tool from the **Data tab** of the Toolbox onto the form. This will appear in the component tray under the form. The **Data Adapter Configuration Wizard** will be automatically launched to assist you.
2. **SqlConnection object and associated Command objects** will be created to support the Data Adapter.
3. Select the DataView you created and click the "Generate DataSet" option at the bottom of the properties window.
4. This will enable you to create a DataSet object, which will contain the DataTable/DataView, which wraps the record set you configured in the Wizard.
5. Create a name for your DataSet object and select the table(s) to include.

## API Reference (if applicable)
Not applicable for this specific content.

## Code Examples (multi-language supported)
Not applicable for this specific content.

## Page-level Navigation/TOC (if applicable)
Not applicable for this specific content.

## Cross References
- **See Also:** DataSource

## RAG Annotations
<!-- tags: [AutoCompleteControl, ComboBoxAutoComplete, PropertyGrid, DataSource, DataView, SqlAdapter, OleDbAdapter, Syncfusion Winforms, version:11.4.0.26] keywords: [AutoCompleteControl properties, DataSource configuration, DataView, ComboBoxAutoComplete, DataGrid, Wizard, table wrapping] -->
```