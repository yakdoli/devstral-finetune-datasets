```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_176.jpeg
document_name: tools
page_number: 176
page_id: tools#page_176
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:11:24Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview

- Standard (Default value - no arrows appear for this option)
- VS2005,
- WhidBey and
- VS2008.

### Content

#### DragProviderStyle Settings

DragProviderStyle allows various styles for displaying arrows when dragging controls. Here are the code examples for setting the styles in both C# and VB.NET:

##### C#

```csharp
this.dockingManager1.DragProviderStyle =
    Syncfusion.Windows.Forms.Tools.DragProviderStyle.VS2008;
```

##### VB.NET

```vbnet
Me.dockingManager1.DragProviderStyle =
    Syncfusion.Windows.Forms.Tools.DragProviderStyle.VS2008
```

#### Figure: VS 2005 DragProviderStyle

![VS 2005 DragProviderStyle](https://user-images.githubusercontent.com/11505654/203918194-aed0e88f-5d8c-4fce-874e-df4bce347f9c.png)

*Figure 89: VS 2005 DragProviderStyle*

### API Reference

#### DragProviderStyle Enum

The `DragProviderStyle` enum provides the following options:

- **Standard**: The default option with no arrows.
- **VS2005**: Displays arrows similar to the VS2005 style.
- **WhidBey**: Displays arrows in a specific style.
- **VS2008**: Displays arrows similar to the VS2008 style.

#### Properties

- **dockingManager1**: The instance of `DockingManager` which manages the drag functionality.
- **DragProviderStyle**: The property to set the style of the drag arrows.

### Code Examples

The provided code examples demonstrate how to set the `DragProviderStyle` property to `VS2008` in both C# and VB.NET.

### Cross References

- See also: [Syncfusion Windows Forms Docking Manager](#syncfusion-windows-forms-docking-manager)

### Footer

© 2013 Syncfusion. All rights reserved.

---

<!-- tags: [winforms, dragproviderstyle, dockingmanager, syncfusion] keywords: [dragproviderstyle, vs2005, vs2008, whidbey, standard] -->
```