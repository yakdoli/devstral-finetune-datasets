```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_301.jpeg
document_name: tools
page_number: 301
page_id: tools#page_301
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:04:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses the AutoComplete control and its functionality for managing data sources.
- Explores external data sources and the configuration of multiple columns for data retrieval.
- Provides examples and detailed descriptions of the AutoComplete control properties.

## Content

```vb
Syncfusion.Windows.Forms.Tools.AutoCompleteItemEventArgs)
    ' Displays corresponding OrgID of the OrganisationName on the label.
    Me.label1.Text = args.ItemArray(0).ToString()
End Sub
```

### Figure 129: External Data Source set for the AutoComplete Control
![External Data Source set for the AutoComplete Control](#external-data-source)

Refer to **Multiple Columns** section for more information on configuring data sources with multiple columns.

### 3.5.1.1.3.3 Multiple Columns

The AutoComplete control allows users to display multiple columns of information for each matching entry in the AutoSuggest mode of operation. Columns can be configured through the **AutoComplete.Columns** property.

| **AutoComplete Properties** | **Description** |
|-----------------------------|------------------|
| **Columns**                  | Specifies the collection of columns in the auto complete dropdown, when **AutoCompleteModes** enumerator value is **AutoSuggest**. Each column is represented by an **AutoCompleteDataColumnInfo** object. This class includes a definition for specifying whether the column is the matching column or the image column. |
| **MatchMode**                | Specifies the modes in which the **AutoCompleteControl** fills the history list for the current text in the current edit control. The values are: |

## API Reference (if applicable)
### Properties
- **AutoCompleteMode**: Gets or sets the mode in which the AutoCompleteControl fills the history list for the current text in the current edit control.

### Methods
- **BeginInvoke(Delegate, Object[])**: Executes the specified delegate asynchronously on the thread that the control's underlying handle was created on.

### Events
- **ItemSelected**: Occurs when an item has been selected from the dropdown list.

## Code Examples

```csharp
// Example usage of AutoComplete control
private void Form1_Load(object sender, EventArgs e)
{
    // Set properties
    autoCompleteControl.AutoCompleteMode = Syncfusion.Windows.Forms.Tools.AutoCompleteMode.AutoCompleteImmediate;
    autoCompleteControl.AutoCompleteColumns = new AutoCompleteDataColumnInfo[]
    {
        new AutoCompleteDataColumnInfo("OrgName", 100, true),
        new AutoCompleteDataColumnInfo("OrgID", 80, false)
    };
}
```

## Cross References
- See also: [Multiple Columns] section for more on configuring data sources.

<!-- tags: [Windows Forms, AutoCompleteControl, Syncfusion, Multiple Columns, AutoSuggest, AutoComplete] keywords: [orgname, orgid, dropdown, datacolumns, matchmode, autocompletecontrol] -->
```