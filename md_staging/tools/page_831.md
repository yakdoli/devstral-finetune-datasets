```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_831.jpeg
document_name: tools
page_number: 831
page_id: tools#page_831
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:38:28Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- The page introduces the **EditableList** control with AutoCompletion capability.
- Discusses the event handling in the **EditableList** control, highlighting its compatibility with Windows Button, TextBox, and ListBox controls.
- Describes the various events associated with the **EditableList** control and how they can be used effectively for drag-and-drop operations and external object handling.

### Content

#### Figure 530: EditableList With AutoCompletion Capability

![EditableList With AutoCompletion Capability](image)

**3.5.8.7.4 Event Handling**

- **EditableList controls** contain events that are similar to those in the Windows Button, TextBox, and ListBox.

##### EditableList.ListBox.SelectedValueChanged

- This event is triggered when the value of the `SelectedValue` property is changed on the list control.

##### EditableList.TextBox.TextChanged

- This event is triggered when the value of the `Text` property is changed on the list control.

##### EditableList.DragDrop

- This event is triggered when the drag-and-drop operation is completed.

##### EditableList.DragEnter

- This event is triggered when a object is dragged into the control's bounds.

##### 3.5.8.7.4.1 Handling Drag drop events

- **DragDrop** and **DragEnter** events can be handled to drag and drop external objects into the **EditableList** control.

## API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Tools`
- **Class**: `EditableList`
- **Events**:
  - `ListBox.SelectedValueChanged`
  - `TextBox.TextChanged`
  - `DragDrop`
  - `DragEnter`

## Code Examples

- C# Example for handling `DragDrop` and `DragEnter` events:

```csharp
private void EditableList_DragDrop(object sender, DragEventArgs e)
{
    if (e.Data.GetDataPresent(DataFormats.FileDrop))
    {
        string[] files = (string[])e.Data.GetData(DataFormats.FileDrop);
        // Perform drag-and-drop operation
    }
}

private void EditableList_DragEnter(object sender, DragEventArgs e)
{
    if (e.Data.GetDataPresent(DataFormats.FileDrop))
    {
        e.Effect = DragDropEffect.Copy;
    }
}
```

## Cross References

- **See also**: List control documentation, Windows Forms drag-and-drop operations.

<!-- tags: [editablelist, windows forms, control, event handling, drag and drop] keywords: [editablelist, selectedvaluechanged, textchanged, dragdrop, dragenter, windowsforms, syncfusion] -->
```