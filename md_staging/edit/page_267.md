```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_267.jpeg
document_name: edit
page_number: 267
page_id: edit#page_267
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:43Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Content

### 4.14.21.1 HorizontalScroll Event

This event is raised when the user scrolls the window horizontally.

The event handler receives an argument of type **ScrollEventArgs**. The following ScrollEventArgs members provide information specific to this event.

| Member            | Description                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------|
| `NewValue`        | Gets / sets the new System.Windows.Forms.ScrollBar.Value for the scrollbar.                     |
| `OldValue`        | Gets / sets the old System.Windows.Forms.ScrollBar.Value for the scrollbar.                     |
| `ScrollOrientation` | Gets the scrollbar orientation that raised the scroll event.                                 |
| `Type`            | Gets the type of scroll event that occurred.                                                   |

#### Code Examples

```csharp
[C#]

private void editControl1_HorizontalScroll(object sender, ScrollEventArgs e)
{
    Console.WriteLine(" HorizontalScroll event is raised ");
}
```

```vb
[VB.NET]

Private Sub editControl1_HorizontalScroll(ByVal sender As Object, ByVal e As ScrollEventArgs)
    Console.WriteLine(" HorizontalScroll event is raised ")
End Sub
```

### 4.14.21.2 VerticalScroll Event

This event is raised when the user scrolls the window vertically.

The event handler receives an argument of type **ScrollEventArgs**. The following ScrollEventArgs members provide information specific to this event.

| Member            | Description                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------|
| `NewValue`        | Gets / sets the new System.Windows.Forms.ScrollBar.Value for the scrollbar.                     |
| `OldValue`        | Gets / sets the old System.Windows.Forms.ScrollBar.Value for the scrollbar.                     |
| `ScrollOrientation` | Gets the scrollbar orientation that raised the scroll event.                                 |
| `Type`            | Gets the type of scroll event that occurred.                                                   |

## API Reference

- **Namespace:** System.Windows.Forms
- **Class:** ScrollEventArgs
- **Members:**
  - `NewValue`: Gets / sets the new System.Windows.Forms.ScrollBar.Value for the scrollbar.
  - `OldValue`: Gets / sets the old System.Windows.Forms.ScrollBar.Value for the scrollbar.
  - `ScrollOrientation`: Gets the scrollbar orientation that raised the scroll event.
  - `Type`: Gets the type of scroll event that occurred.

## Code Examples

The example code demonstrates how to handle the `HorizontalScroll` event in both C# and VB.NET. Similar implementations can be created for the `VerticalScroll` event.

<!-- tags: [syncfusion, winforms, scroll, eventargs, horizontalscroll, verticalscroll, scrollbar] keywords: [horizontal scroll, vertical scroll, event handler, scroll eventargs, scrollbar orientation, windows forms, event handling] -->
```