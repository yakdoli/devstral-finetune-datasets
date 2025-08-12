```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_143.jpeg
document_name: tools
page_number: 143
page_id: tools#page_143
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:51:10Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Figure 59: Illustrates CaptionBar in a Docked Control

The following topics will guide the end users on how to effectively use the caption bar settings for the docked controls.

#### 3.4.3.2.1 Label and Image for CaptionBar

##### Caption Label

Docking Manager lets you set the caption label using **DockLabel** property of the particular control, through designer, and programmatically by using **SetDockLabel** method. Alignment of these labels can be specified using **DockLabelAlignment** property.

| DockingManager Property         | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| DockLabelAlignment              | Sets the dock label alignment. The different alignments options are, <br><br> - **Left**, <br> - **Right**, <br> - **Center**. |

#### Code Examples

##### C#

```csharp
this.dockingManager.SetDockLabel(this.listBox1, "Syncfusion ASP.NET products");
this.dockingManager1.DockLabelAlignment = 
Syncfusion.Windows.Forms.Tools.DockLabelAlignmentStyle.Left;
```

##### VB.NET

```vb
Me.dockingManager.SetDockLabel(Me.listBox1, "Syncfusion ASP.NET products")
Me.dockingManager1.DockLabelAlignment = 
Syncfusion.Windows.Forms.Tools.DockLabelAlignmentStyle.Left
```

## API Reference

- **DockLabelAlignment**  
  - Sets the dock label alignment. The different alignment options are: **Left**, **Right**, and **Center**.

### Cross References

- **DockLabel** property
- **SetDockLabel** method
- **DockLabelAlignmentStyle** enum

<!-- tags: [DockingManager, CaptionBar, DockLabel, DockLabelAlignment, C#, VB.NET, Windows Forms, Syncfusion, Tools] keywords: [DockLabelAlignment, SetDockLabel, CaptionBar, DockLabel, DockManager, alignment, GUI, C#, VB.NET, WinForms, tools, designer, programmatically] -->
``` 
