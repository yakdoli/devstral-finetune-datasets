```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_211.jpeg
document_name: diagram
page_number: 211
page_id: diagram#page_211
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:20:09Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### Overview
- This section explains the functionality and behavior of the **Magnification Event** in the context of Windows Forms.
- Focuses on the events triggered when the user zooms in or out, displaying the old and new magnification factors.
- Includes details about how to handle and retrieve magnification values.

## Content

### Magnification Event

When the control is zoomed in or out, the magnification events will be fired, displaying the old and new magnification factors.

**Magnification Events** are as follows:

| DiagramViewerEventSink               | Description                                      |
| ------------------------------------ | ------------------------------------------------ |
| MagnificationChanged                 | Fired when magnification value is changed.     |

Data can be retrieved or set using the following members.

#### MagnificationEventArgs Members

| MagnificationEventArgs Member       | Description                                      |
| ------------------------------------ | ------------------------------------------------ |
| NewMagnification                    | Returns the new magnification value.            |
| OriginalMagnification               | Returns the old magnification value before the zoom action. |

### Diagram

#### Figure 131: Origin Changed Stage

The diagram demonstrates the process flow, showing stages labeled as **PROCESS**, **CHECK**, and **END**.

## API Reference

### Event

```csharp
public event EventHandler<DiagramViewerMagnificationChangedEventArgs> MagnificationChanged;
```

**Parameters:**

- **e**: DiagramViewerMagnificationChangedEventArgs - Contains the new and original magnification values.

### Event Args

```csharp
public class DiagramViewerMagnificationChangedEventArgs : EventArgs
{
    public double NewMagnification { get; }
    public double OriginalMagnification { get; }
}
```

## Code Examples

#### C#

```csharp
// Subscribe to the MagnificationChanged event
diagramViewer.MagnificationChanged += DiagramViewer_MagnificationChanged;

private void DiagramViewer_MagnificationChanged(object sender, DiagramViewerMagnificationChangedEventArgs e)
{
    Console.WriteLine($"Magnification changed from {e.OriginalMagnification} to {e.NewMagnification}");
}
```

## RAG Annotations

<!-- tags: [Windows Forms, Essential Diagram, Magnification Event, Events, User Interaction, Diagram Viewer] -->
<!-- keywords: [MagnificationChanged, NewMagnification, OriginalMagnification, DiagramViewerEventSink, DiagramViewerMagnificationChangedEventArgs] -->
```