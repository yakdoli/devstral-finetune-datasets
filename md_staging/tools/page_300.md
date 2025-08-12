```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_300.jpeg
document_name: tools
page_number: 300
page_id: tools#page_300
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:04:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Specify an external datasource for the AutoComplete control.
- Set AutoComplete mode to AutoSuggest and configure the DataSource property.
- Handle the AutoCompleteItemSelected event to display corresponding information.

## Content

You can specify an external datasource for the AutoComplete control to use as the history list. This can be specified through the `AutoComplete.DataSource` property. The object specified for this property can be any object that implements `IList` or `IListSource`.

### Setting Up the Data Source

1. **Set AutoComplete mode to AutoSuggest.**
2. **Set the DataSource in the form's Load event as follows.**

#### C#

```csharp
private void Form1_Load(object sender, System.EventArgs e)
{
    // Set up the datasource on the Autocomplete control.
    this.oleDbDataAdapter1.Fill(this.dataSet11.organisation);
    this.autoComplete1.DataSource = this.dataSet11.organisation;
}
```

#### VB.NET

```vb
Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)

    ' Set up the datasource on the Autocomplete control .
    Me.oleDbDataAdapter1.Fill(Me.dataSet11.organisation)
    Me.autoComplete1.DataSource = Me.dataSet11.organisation
End Sub
```

### Handling the AutoCompleteItemSelected Event

3. **AutoCompleteItemSelected** event is raised when a new item has been selected by the user when the AutoComplete drop-down list is displayed. In this event, for the tutorial purpose, the code to display corresponding OrgID of the OrganisationName on the label is included. The below code retrieves the corresponding item from the datasource, for the selected item in the AutoComplete control.

#### C#

```csharp
private void autoComplete1_AutoCompleteItemSelected(object sender, Syncfusion.Windows.Forms.Tools.AutoCompleteItemEventArgs args)
{
    // Displays corresponding OrgID of the OrganisationName on the label.
    this.label1.Text = args.ItemArray[0].ToString();
}
```

#### VB.NET

```vb
Private Sub autoComplete1_AutoCompleteItemSelected(ByVal sender As Object, ByVal args As Syncfusion.Windows.Forms.Tools.AutoCompleteItemEventArgs

## API Reference

### Namespace
- `Syncfusion.Windows.Forms.Tools`

### Events
- **AutoCompleteItemSelected**: Triggered when a new item is selected, providing details about the selected item.

### Methods
- `Fill`: Used to populate the dataset with data from a data adapter.

### Properties
- **DataSource**: Property specifying the source of data for the AutoComplete control.

## Code Examples

### C#

```csharp
private void autoComplete1_AutoCompleteItemSelected(object sender, Syncfusion.Windows.Forms.Tools.AutoCompleteItemEventArgs args)
{
    // Displays corresponding OrgID of the OrganisationName on the label.
    this.label1.Text = args.ItemArray[0].ToString();
}
```

### VB.NET

```vb
Private Sub autoComplete1_AutoCompleteItemSelected(ByVal sender As Object, ByVal args As Syncfusion.Windows.Forms.Tools.AutoCompleteItemEventArgs

## Page-level Navigation/TOC (if applicable)
- [Setting Up the Data Source](#setting-up-the-data-source)
- [Handling the AutoCompleteItemSelected Event](#handling-the-autocompleteitemselected-event)

### Cross References
See also:
- `AutoComplete.DataSource`
- `AutoCompleteItemEventArgs`
- `IList`
- `IListSource`
- `DataSource` property setup

<!-- tags: [AutoComplete, DataSource, Windows Forms, C#, VB.NET, AutoCompleteItemSelected, Syncfusion, WinForms, Control, AutoSuggest] keywords: [AutoComplete, DataSource, drop-down list, OrganisationName, OrgID, label, AutoCompleteItemSelected, data adapter, data source, event handling] -->
```