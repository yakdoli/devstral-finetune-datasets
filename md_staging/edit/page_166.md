```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_166.jpeg
document_name: edit
page_number: 166
page_id: edit#page_166
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:20Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Context Choice Events

The following are the events associated with the ContextChoice:

### ContextChoiceItemSelected

This event is raised when an item is selected within a `ContextChoice`. The following code snippet demonstrates how to handle this event in VB.NET and C#.

#### VB.NET
```vb
Private Sub editControl1_ContextChoiceItemSelected(ByVal sender As Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController, ByVal e As Syncfusion.Windows.Forms.Edit.ContextChoiceItemSelectedEventArgs) Handles EditControl1.ContextChoiceItemSelected
    ' Gets the selected item.
    Dim controller As IContextChoiceController = sender
    Dim selectedItemText As String = e.SelectedItem.Text
End Sub
```

#### C#
```csharp
private void editControl1_ContextChoiceSelectedTextInsert(Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController sender, Syncfusion.Windows.Forms.Edit.ContextChoiceTextInsertEventArgs e)
{
    IContextChoiceController controller = sender as IContextChoiceController;

    // Gets the displayed text.
    string displayText = e.DisplayText;

    // Gets the text to be inserted.
    string insertText = e.InsertText;

    // Gets the item selected.
    string selectedItemText = e.SelectedItem.Text;
}
```

### ContextChoiceSelectedTextInsert

This event is raised when an item is selected within a `ContextChoice` and text is inserted into the control. The following code snippet demonstrates how to handle this event in VB.NET.

#### VB.NET
```vb
Private Sub editControl1_ContextChoiceSelectedTextInsert(ByVal sender As Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController, ByVal e As Syncfusion.Windows.Forms.Edit.ContextChoiceTextInsertEventArgs) Handles EditControl1.ContextChoiceSelectedTextInsert
    Dim controller As IContextChoiceController = sender

    ' Gets the displayed text.
    Dim displayText As String = e.DisplayText

    ' Gets the text to be inserted.
    Dim insertText As String = e.InsertText

    ' Gets the item selected.
    Dim selectedItemText As String = e.SelectedItem.Text
End Sub 'editControl1_ContextChoiceSelectedTextInsert
```

## API Reference

### Namespaces and Classes

- **Namespace**: Syncfusion.Windows.Forms.Edit
- **Class**: IContextChoiceController
- **EventArgs**: ContextChoiceItemSelectedEventArgs, ContextChoiceTextInsertEventArgs

### Methods and Events

- **Method**: `editControl1_ContextChoiceItemSelected`
  - **Parameters**:
    - `sender`: Object of type `IContextChoiceController`.
    - `e`: Object of type `ContextChoiceItemSelectedEventArgs`.
  - **Purpose**: Handles the event when an item is selected.

- **Method**: `editControl1_ContextChoiceSelectedTextInsert`
  - **Parameters**:
    - `sender`: Object of type `IContextChoiceController`.
    - `e`: Object of type `ContextChoiceTextInsertEventArgs`.
  - **Purpose**: Handles the event when text is inserted after an item selection.

### Parameters

- **displayText**: The text currently displayed in the control.
- **insertText**: The text to be inserted into the control.
- **selectedItemText**: The text of the selected item from the `ContextChoice`.

## Code Examples

The provided code snippets demonstrate how to handle the `ContextChoiceItemSelected` and `ContextChoiceSelectedTextInsert` events in both VB.NET and C#. These examples show how to access the selected item's text, the display text, and the text to be inserted.

### Conclusion

Understanding and implementing the `ContextChoice` events in Windows Forms with Syncfusion controls enhances the flexibility and functionality of the control, allowing developers to monitor and respond to user interactions dynamically.

<!-- tags: [Syncfusion Winforms, ContextChoice, Events, editControl, edit, windows forms] keywords: [ContextChoiceItemSelected, ContextChoiceSelectedTextInsert, IContextChoiceController, EventArgs, displayText, insertText, selectedItemText] -->
```