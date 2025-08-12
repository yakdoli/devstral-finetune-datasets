```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_145.jpeg
document_name: tools
page_number: 145
page_id: tools#page_145
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:51:26Z
fidelity: lossless
-->

## Caption Images and DockIcons in WinForms Docking System

### Overview
- Explains how to display caption icons and set dock icons for docked controls in Windows Forms using the `DockManager` properties.
- Provides a step-by-step guide to achieve this through the designer and how to programmatically set the `DockIcon`.

### Content

```csharp
[C#]
this.dockingManager1.ShowCaptionImages = true;
```

```vb
[VB.NET]
Me.dockingManager1.ShowCaptionImages = True
```

The caption icons / the images can be set using this DockIcon property of the docked control. To achieve this through designer, follow the below steps.

1. Create a docked window.
2. Add ImageList and add the images to it.
3. Select the image list through the `ImageList` property of the docking manager.
4. Now go to the property of the docked control to which you have to set the dock icon.
5. Give the image index value to the DockIcon property.
6. Run the application.
7. The corresponding control will be displayed with the icon that is set.
8. To disable displaying the icon, set the value as -1.

| DockedControl Property | Description                                      |
|------------------------|--------------------------------------------------|
| DockIcon               | Index of the image associated with this docking window. |

```csharp
[C#]
this.dockingManager1.SetDockIcon(this.listBox1, 2);
```

```vb
[VB.NET]
Me.DockingManager1.SetDockIcon(Me.ListBox1, 2)
```

### API Reference

- **Properties:**
  - `DockManager.ShowCaptionImages`: Controls the visibility of caption images.
  - `DockManager.DockIcon`: Sets the index of the image associated with a docked window.

## Code Examples

- **Setting DockIcon Programmatically:**

```csharp
this.dockingManager1.SetDockIcon(this.listBox1, 2);
```

```vb
Me.DockingManager1.SetDockIcon(Me.ListBox1, 2)
```

### Page-level Navigation/TOC (if applicable)
- This page provides detailed guidance on setting and displaying dock icons for controls in a Windows Forms application.

### Cross References
- Refer to the documentation on `DockManager` and `ImageList` for additional details.

<!-- tags: [winforms, dockmanager, captionimages, dockicon, visualstudio, designer, imageindex, softwaredevelopment] keywords: [CaptionImages, DockIcons, DockManager, ImageList, Visual Studio, Docked Control, DockIcon Property, Windows Forms, .NET Framework, Syncfusion] -->
```