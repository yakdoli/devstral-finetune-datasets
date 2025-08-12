```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_314.jpeg
document_name: tools
page_number: 314
page_id: tools#page_314
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:06:22Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- Provides an overview of events and properties for AutoCompleteMatchItemEventArgs.
- Includes examples in C# and VB.NET for handling match operations.
- Focuses on frequently asked questions related to adding data rows at runtime.

### Content

#### AutoCompleteMatchItemEventArgs Properties

| Property             | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| Cancel               | Gets/Sets a value indicating whether the event should be canceled.         |
| CurrentText          | Returns the current text value to be matched.                              |
| PossibleMatch       | Returns the possible match value that needs to be compared against AutoCompleteMatchItemEventArgs.CurrentText by the event handler. |

#### C# Example

```csharp
private void autoCompletel_MatchItem(object sender, AutoCompleteMatchItemEventArgs args)
{
    // Cancels the match operation
    e.Cancel = true;
}
```

#### VB.NET Example

```vb.net
Private Sub autoCompletel_MatchItem(ByVal sender As Object, ByVal args As AutoCompleteMatchItemEventArgs)
    '//Cancels the match operation
    e.Cancel = true
    End Sub
```

### 3.5.1.1.5 Frequently Asked Questions

This section illustrates the solutions for various task-based queries about the control.

#### 3.5.1.1.5.1 How to add a new data row to the Data table at run time?

This is achieved by calling the `SetTableData()` method as follows. This method sets internal table data based on `AutoComplete.DataSource` property.

#### C# Example

```csharp
DataTable dt;
private void Form1_Load(object sender, System.EventArgs e)
{
    dt = new DataTable("select");
    dt.Columns.Add("Countries");
    dt.Columns.Add("states");
}
```

## API Reference

### Methods
- **SetTableData()**
  - Sets internal table data based on the `AutoComplete.DataSource` property.

## Code Examples

- **C# Example**

```csharp
private void autoCompletel_MatchItem(object sender, AutoCompleteMatchItemEventArgs args)
{
    // Cancels the match operation
    e.Cancel = true;
}
```

- **VB.NET Example**

```vb.net
Private Sub autoCompletel_MatchItem(ByVal sender As Object, ByVal args As AutoCompleteMatchItemEventArgs)
    '//Cancels the match operation
    e.Cancel = true
    End Sub
```

## Cross References

- See also: [AutoCompleteMatchItemEventArgs](#AutoCompleteMatchItemEventArgs), [SetTableData()](#SetTableData)

<!-- tags: [autoComplete, dataSource, matchItem, dataRow, eventArgs] keywords: [AutoCompleteMatchItemEventArgs, SetTableData, DataTable, C#, VB.NET, runtime] -->
```