```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_233.jpeg
document_name: tools
page_number: 233
page_id: tools#page_233
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:50:58Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Sample

### Overview
- Demonstrates the Linked Managers concept.
- Available in the sample installation path:

## Content

### Sample Installation Path

... My Documents\Syncfusion\EssentialStudio\\**Version Number**\Windows\Tools.Windows\Samples\2.0\Docking Package\LinkedManagers

### 3.4.3.8.9 ImageListChanged Event

#### Overview
- Triggered when the `imagelist` property is changed.
- Every docked control has a `SetDockIcon` property to set icons.
- The event is triggered when the `SetDockIcon` property is changed.

#### Member Description

| Member     | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| Control    | Gets the docked control for which the imagelist property is changed.     |

#### Code Examples

##### [C#]

```csharp
// Occurs when the ImageList property changes
private void dockingManager1_ImageListChanged(object sender, System.EventArgs e)
{
    Console.WriteLine("ImageList Changed Event Is Triggered");
    // Here the code which set the Docking Icon dynamically.
    dockingManager1.SetDockIcon(this.panel1, 0);
    dockingManager1.SetDockIcon(this.panel2, 1);
}
```

##### [VB.NET]

```vb
' Occurs when the ImageList property changes
Private Sub dockingManager1_ImageListChanged(ByVal sender As Object, ByVal e As System.EventArgs)
    Console.WriteLine("ImageList Changed Event Is Triggered")
    ' Here the code which set the Docking Icon dynamically.
    dockingManager1.SetDockIcon(Me.panel1, 0)
    dockingManager1.SetDockIcon(Me.panel2, 1)
End Sub
```

## Page-level Navigation/TOC (if applicable)
- This page focuses on the `ImageListChanged Event` and its implementation in C# and VB.NET.

## Cross References
- See also: Linked Managers concept for more details.

<!-- tags: [Syncfusion Winforms, Docking Package, Event Handling, ImageListChangeListener, C#, VB.NET] keywords: [imagelist, SetDockIcon, ImageListChangedEvent, controls, docked, icons] -->
```