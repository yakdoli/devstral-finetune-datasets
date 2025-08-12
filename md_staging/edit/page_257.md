```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_257.jpeg
document_name: edit
page_number: 257
page_id: edit#page_257
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:04Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview

- Discusses the MenuFill Event and its use in customizing context menus.
- Explains the OperationStarted Event and other operation events in Windows Forms.
- Provides examples of handling the OperationStarted Event in C# and VB.NET.

## Content

### 4.14.13 MenuFill Event

This event is discussed in the **Customizable Context Menu** topic.

### 4.14.14 Operation Events

This section discusses the below given operation events.

#### 4.14.14.1 OperationStarted Event

This event occurs when an operation starts.

The event handler receives an argument of type **ILongOperation**. The following **ILongOperation** members provide information specific to this event.

| Member       | Description                          |
|--------------|--------------------------------------|
| ID           | Gets ID of the operation.           |
| IsRunning    | Gets value indicating whether operation is running now. |
| Name         | Gets name of the operation.         |
| RunningTime  | Gets time of the operation activity.|

#### Event Handling Examples

**[C#]**

```csharp
private void editControl_OperationStarted(Syncfusion.Windows.Forms.Edit.Interfaces.ILongOperation operation)
{
    Console.WriteLine(" OperationStarted event is raised ");
}
```

**[VB.NET]**

```vb
Private Sub editControl_OperationStarted(ByVal operation As Syncfusion.Windows.Forms.Edit.Interfaces.ILongOperation)
    Console.WriteLine(" OperationStarted event is raised ")
End Sub
```

### API Reference

- **Namespace**: Syncfusion.Windows.Forms.Edit.Interfaces
- **Event**: OperationStarted
- **Argument**: ILongOperation

### Code Examples

The above code snippets demonstrate how to handle the **OperationStarted** event in both C# and VB.NET for Windows Forms applications.

## Page-level Navigation/TOC

- 4.14.13 MenuFill Event
- 4.14.14 Operation Events
  - 4.14.14.1 OperationStarted Event

## Cross References

See also:
- **Customizable Context Menu** (for more information on MenuFill Event)
- Related topics on handling long operations in Windows Forms.

### RAG Annotations

<!-- tags: [Syncfusion Winforms, OperationStarted Event, ILongOperation, event handling, C#, VB.NET] keywords: [OperationStarted, MenuFill Event, ILongOperation, Windows Forms, custom context menu, code examples] -->
```