```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_830.jpeg
document_name: tools
page_number: 830
page_id: tools#page_830
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:28Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Describes how to enable AutoComplete functionality in a TextBoxArea of an EditableList control in Syncfusion WinForms.
- Outlines the steps required to associate an AutoComplete feature with the editing TextBox of an EditableList.

## AutoComplete in TextBoxArea

### [VB.NET]

```vb
Me.editableList1.WantButton = True
```

### 3.5.8.7.3.3 Enabling AutoComplete in TextBoxArea
We can associate an AutoComplete with the editing TextBox of the EditableList. The following steps help to achieve this:

1. Create an instance of the AutoComplete.
2. Append the AutoComplete source.
3. In the Form load event, place the code.

#### Code Example: AutoComplete in Form Load Event

##### [C#]
```csharp
private void form1_Load(object sender, EventArgs e)
{
    // Sets the AutoComplete.
    autoCompletel.DataSource = editableList1.ListBox.Items;
    autoCompletel.SetAutoComplete(editableList1.TextBox, AutoCompleteModes.Both);
}
```

##### [VB.NET]
```vb
Private Sub form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    ' Sets the AutoComplete.
    autoCompletel.DataSource = editableList1.ListBox.Items
    autoCompletel.SetAutoComplete(editableList1.TextBox, AutoCompleteModes.Both)
End Sub
```

### Data Source Considerations
The data source may vary according to your choice.

## API Reference

- **DataSource Property**: Specifies the data source for the AutoComplete feature.
- **SetAutoComplete Method**: Configures the AutoComplete behavior for the TextBox.

## Code Examples

### C# Example
```csharp
// Setting AutoComplete for the editableList1 TextBox
autoCompletel.DataSource = editableList1.ListBox.Items;
autoCompletel.SetAutoComplete(editableList1.TextBox, AutoCompleteModes.Both);
```

### VB.NET Example
```vb
' Setting AutoComplete for the editableList1 TextBox
autoCompletel.DataSource = editableList1.ListBox.Items
autoCompletel.SetAutoComplete(editableList1.TextBox, AutoCompleteModes.Both)
```

### See also:
- [EditableList Control Overview](#editablelist-control-overview)
- [AutoComplete Modes](#autocomplete-modes)

<!-- tags: [WinForms, EditableList, AutoComplete, TextBoxArea] keywords: [AutoComplete, EditableList, TextBox, DataSource, AutoCompleteModes] -->
```