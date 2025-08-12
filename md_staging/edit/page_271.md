```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_271.jpeg
document_name: edit
page_number: 271
page_id: edit#page_271
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:58Z
fidelity: lossless
-->

## Overview

- The document discusses an event handler that receives a `TextChangingEventArgs` argument, detailing its members and usage in C# and VB.NET.
- It provides information about the Line modification events in the Edit control in Windows Forms.
- The text includes examples of handling the `TextChanging` event and describes the types of line modifications that trigger specific events.

## Content

### TextChangingEvent Members

The event handler receives an argument of type `TextChangingEventArgs`. The following `TextChangingEventArgs` members provide information specific to this event.

| **Member**     | **Description**                                                                 |
|----------------|----------------------------------------------------------------------------------|
| **Cancel**     | Gets/sets the value indicating whether text change has been canceled.           |
| **StartColumn**| Gets/sets virtual column of Insert/Delete start.                                 |
| **StartLine**  | Gets/sets virtual line of Insert/Delete start.                                   |
| **Text**       | Gets/sets event's text.                                                        |
| **Type**       | Gets/sets type of the event (Changed/Insert/Delete). It includes the below given options. |

### C# Code Example

```csharp
private void editControl1_TextChanging(object sender, Syncfusion.Windows.Forms.Edit.TextChangingEventArgs e)
{
    e.Type = Syncfusion.Windows.Forms.Edit.Enums.TextChange.Deleted;

    // The below statement can be seen in the output window at runtime when the text of the Edit Control is deleted.
    Console.WriteLine(" TextChanging event is raised ");
}
```

### VB.NET Code Example

```vb
Private Sub editControl1_TextChanging(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.TextChangingEventArgs)
    e.Type = Syncfusion.Windows.Forms.Edit.Enums.TextChange.Deleted

    ' The below statement can be seen in the output window at runtime when the text of the Edit Control is deleted.
    Console.WriteLine(" TextChanging event is raised ")
End Sub
```

### Line Modification Events

#### Overview of Line Modification Events

The line modification events occur whenever a line in the Edit control is subjected to a change by modifying the text of an existing line, inserting a line, or removing a line in the editor.

The following events are triggered from the control when the editor is modified:

## API Reference (if applicable)

### Members of TextChangingEventArgs

- **Cancel**: Gets/sets the value indicating whether text change has been canceled.
- **StartColumn**: Gets/sets the virtual column of Insert/Delete start.
- **StartLine**: Gets/sets the virtual line of Insert/Delete start.
- **Text**: Gets/sets the event's text.
- **Type**: Gets/sets the type of the event (Changed/Insert/Delete).

### Types of Events

- **Changed**: Indicates a change in the text.
- **Inserted**: Indicates an insertion of text.
- **Deleted**: Indicates a deletion of text.

## Code Examples (multi-language supported)

### C# Example

```csharp
Console.WriteLine(" TextChanging event is raised ");
```

### VB.NET Example

```vb
Console.WriteLine(" TextChanging event is raised ")
```

## RAG Annotations

<!-- tags: [TextChangingEventArgs, LineModificationEvents, WindowsForms, SyncfusionWinforms, 11.4.0.26] keywords: [edit control, text changing event, event handling, line modification, text change, start column, start line, text, event type] -->
```