```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_172.jpeg
document_name: tools
page_number: 172
page_id: tools#page_172
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:08:16Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to set the visual style of docked controls using the DockingManager in Syncfusion WinForms.
- Includes examples in both C# and VB.NET.
- Explores various visual styles for docking functionality, such as Default, Office XP, Office 2003, Visual Studio 2005, Office 2007, and Office 2007 Outlook.
- Describes how to use the Office2007Theme property to control color schemes in the Office 2007 visual style.

## Content

### Setting the Visual Style of Docked Controls

```csharp
this.dockingManager.VisualStyle =
Syncfusion.Windows.Forms.VisualStyle.VisualStyle.Office2003;
```

```vb
' Set the visual style of the docked controls
Me.dockingManager.VisualStyle =
Syncfusion.Windows.Forms.VisualStyle.Office2003
```

#### Figure 85: Visual Styles for Docking

The following figures illustrate different visual styles for docking in Syncfusion WinForms:

```plaintext
Default                   Office XP                   Office 2003
```

```plaintext
VS 2005                   Office 2007                 Office 2007 Outlook
```

#### Office2007 Color Schemes

DockingManager supports all three color schemes in Office 2007 visual style. This can be controlled using the **Office2007Theme** property.

### API Reference

#### Properties
- **VisualStyle**: Specifies the visual style of the docked controls. Example values include `VisualStyle.Office2003`.
- **Office2007Theme**: Specifies the color scheme for the Office 2007 visual style.

## Code Examples

```csharp
[C#]
this.dockingManager.VisualStyle = 
Syncfusion.Windows.Forms.VisualStyle.VisualStyle.Office2007;
this.dockingManager.Office2007Theme = 
Syncfusion.Windows.Forms.Theme.Blue;
```

```vb
[VB.NET]
Me.dockingManager.VisualStyle = 
Syncfusion.Windows.Forms.VisualStyle.VisualStyle.Office2007
Me.dockingManager.Office2007Theme = 
Syncfusion.Windows.Forms.Theme.Blue
```

## Tags and Keywords
<!-- tags: [product, module, control, api, version?] keywords: [Syncfusion Winforms, DockingManager, VisualStyle, Office2007Theme, C#, VB.NET, Office 2003, Office 2007] -->
```