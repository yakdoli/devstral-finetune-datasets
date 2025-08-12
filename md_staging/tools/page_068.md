```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: tools
page_number: 068
page_id: tools#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:18:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

| DockState | Gets / sets the current dock or float state for the <br/> CommandBar. |
|-----------|-------------------------------------------------------------------------|
| ShowDockModeText | Indicates whether the text caption should be <br/> displayed on a docked CommandBar. |

**Note:** The DisableDocking property must be set to 'False' for the above settings to take effect.

The docked state of the CommandBar can be disabled by setting the **DisableDocking** property to **'True'**.

## EnabledDockBorders

This CommandBarController property allows you to dock the CommandBar to the edges of the form. The **AllowedDockBorders** property doesn't take any effect when this property is set to **'None'**.

### Table 7: CommandBarController

| CommandBarController Property | Description |
|-------------------------------|-------------|
| EnabledDockBorders | Gets / sets the edges of the form along which <br/> the CommandBars are allowed to dock. The <br/> options included are given below.<br/><br/>**Bottom,**<br/>**Left,**<br/>**Right,**<br/>**Top and**<br/>**None.** |

## Code Examples (C#)

```csharp
this.commandBar1.AllowedDockBorders =
    ((Syncfusion.Windows.Forms.Tools.CommandBarDockBorder) ((Syncfusion.Windows.F
    orms.Tools.CommandBarDockBorder.Top |
    Syncfusion.Windows.Forms.Tools.CommandBarDockBorder.Bottom) |
    Syncfusion.Windows.Forms.Tools.CommandBarDockBorder.Left));
this.commandBar1.AlwaysLeadingEdge = true;
this.commandBar1.AlwaysTrailingEdge = true;
```

## API Reference

### Properties
- **EnabledDockBorders**:  
  Gets / sets the edges of the form along which CommandBars are allowed to dock.  
  Options:  
  - **Bottom**,  
  - **Left**,  
  - **Right**,  
  - **Top**,  
  - **None**.

## Page-level Navigation/TOC
- [DockState](#dockstate)
- [ShowDockModeText](#showdockmodetext)
- [EnabledDockBorders](#enableddockborders)

### See also:
- [CommandBar Controller Overview](#commandbar-controller-overview)
- [Docking and Floating Modes](#docking-and-floating-modes)

<!-- tags: [syncfusion, winforms, commandbar] keywords: [docking, float, edges, allowed dock borders, always leading edge, always trailing edge] -->
```