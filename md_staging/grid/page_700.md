```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_700.jpeg
document_name: grid
page_number: 700
page_id: grid#page_700
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:52Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates handling unbound checkbox columns in a grid.
- Explains using `QueryValue` and `SaveValue` events to manage checkbox states.
- Shows code examples in both C# and VB.NET for implementing these events.

## Content

### Handling Unbound Checkbox Columns

The following code demonstrates how to handle the states of unbound checkbox columns in a grid using the `QueryValue` and `SaveValue` events. These events allow you to retrieve and save the checkbox states dynamically.

```csharp
{
    if (e.Field.Name == "CheckboxCol")
    {
        string key = e.Record.GetValue("Col1").ToString();
        if (key != null)
        {
            object val = unboundValues[key];
            e.Value = val;
        }
    }
}

private void gridGroupingControl1_SaveValue(object sender, FieldValueEventArgs e)
{
    if (e.Field.Name == "CheckboxCol")
    {
        string key = e.Record.GetValue("Col1").ToString();
        if (key != null)
        {
            object val = e.Value;
            unboundValues[key] = val;
        }
    }
}
```

#### [VB.NET]

```vb
Hashtable(unboundValues = New Hashtable())

Private Sub gridGroupingControl1_QueryValue(ByVal sender As Object, ByVal e As FieldValueEventArgs) Handles gridGroupingControl1.QueryValue
    If e.Field.Name = "CheckboxCol" Then
        Dim key As String = e.Record.GetValue("Col1").ToString()
        If Not key Is Nothing Then
            Dim val As Object = unboundValues(key)
            e.Value = val
        End If
    End If
End Sub

Private Sub gridGroupingControl1_SaveValue(ByVal sender As Object, ByVal e As FieldValueEventArgs) Handles gridGroupingControl1.SaveValue
    If e.Field.Name = "CheckboxCol" Then
        Dim key As String = e.Record.GetValue("Col1").ToString()
        If Not key Is Nothing Then
            Dim val As Object = e.Value
            unboundValues(key) = val
        End If
    End If
End Sub
```

### Explanation
- **QueryValue Event**: Used to retrieve the current value of an unbound checkbox column for a specific record.
  - `e.Field.Name` checks if the field is the checkbox column (`"CheckboxCol"`).
  - The `key` is derived from the value in the `"Col1"` column, ensuring each record has a unique identifier.
  - The `unboundValues` hashtable is used to store and retrieve the checkbox states.

- **SaveValue Event**: Used to save the checkbox state of an unbound column when it is changed.
  - Similar to `QueryValue`, it checks if the field is the checkbox column and retrieves the key from `"Col1"`.
  - The current value of the checkbox is stored in the `unboundValues` hashtable.

### Notes
- Ensure that the `unboundValues` hashtable is properly initialized and accessible within the scope of the events.
- This implementation assumes that `"Col1"` contains unique values for each row to serve as keys for the hashtable.

## API Reference

### Methods
- `gridGroupingControl1_QueryValue`: Handles retrieving the checkbox state.
- `gridGroupingControl1_SaveValue`: Handles saving the checkbox state.

### Properties
- `unboundValues`: A Hashtable used to store the states of the unbound checkboxes.

## Code Examples
- C# examples: Show how to implement the `QueryValue` and `SaveValue` events.
- VB.NET examples: Provide a translation of the C# implementation, demonstrating the same functionality.

<!-- tags: [grid, unbound checkbox, queryvalue, savevalue, windows forms, essential grid] keywords: [syncfusion, checkbox column, unbound data, grid control, event handling] -->
```