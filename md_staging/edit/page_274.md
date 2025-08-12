```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_274.jpeg
document_name: edit
page_number: 274
page_id: edit#page_274
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:21Z
fidelity: lossless
-->

## Overview
- Explains the `LineDeleted` event in Syncfusion Windows Forms.
- Demonstrates handling the `LineDeleted` event in both C# and VB.NET.
- Introduces the `UnreachableTextFound` event.

## Content

### 4.14.24.3.3 Line Deleted
The `LineDeleted` event will be fired when any line is removed from the Edit control.

#### C#
```csharp
// Handle the LineDeleted event.
this.editControl.LineDeleted += new
Syncfusion.Windows.Forms.Edit.LineDeletedEventHandler(editControl1_LineDeleted);

void editControl1_LineDeleted(object sender,
Syncfusion.Windows.Forms.Edit.LinesEventArgs e)
{
    // The following statement can be seen in the output window
    // at run time.
    Console.WriteLine("Line Deleted");
}
```

#### VB.NET
```vbnet
'Handle the LineDeleted event.
AddHandler Me.editControl.LineDeleted, AddressOf Me.editControl1_LineDeleted

Private Sub editControl1_LineDeleted(ByVal sender As Object,
ByVal e As Syncfusion.Windows.Forms.Edit.LinesEventArgs)
    'The following statement can be seen in the output window at run time.
    Console.WriteLine("Line Deleted")
End Sub
```

### 4.14.25 UnreachableTextFound Event

## API Reference (if applicable)
### WinForms-Specific Event
- **Namespace**: `Syncfusion.Windows.Forms.Edit`
- **Event Name**: `LineDeleted`
- **Parameters**:
  - `sender`: The object that triggered the event.
  - `LinesEventArgs e`: The event data containing details about the line being deleted.
- **Remarks**: This event is raised when a line is deleted from the Edit control.

### WinForms-Specific Event
- **Namespace**: `Syncfusion.Windows.Forms.Edit`
- **Event Name**: `UnreachableTextFound`
- **Parameters**:
  - Not explicitly detailed in this section but is related to conditions where text is unreachable within the Edit control.

## Code Examples (multi-language supported)
### C# Example for Handling LineDeleted Event
```csharp
this.editControl.LineDeleted += (sender, e) =>
    Console.WriteLine("Line Deleted");
```

### VB.NET Example for Handling LineDeleted Event
```vbnet
AddHandler editControl.LineDeleted,
Sub(sender, e)
    Console.WriteLine("Line Deleted")
End Sub
```

## Cross References
- See also: Event handling in Syncfusion Windows Forms controls.

<!-- tags: [syncfusion windows forms, line deleted event, unreachable text found event, event handling] keywords: [Syncfusion.Windows.Forms.Edit, LineDeleted, UnreachableTextFound, EventHandler, C#, VB.NET] -->
```