```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_164.jpeg
document_name: tools
page_number: 164
page_id: tools#page_164
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:02:53Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## ActiveCaptionForeground Property

| Property                        | Description                                                                   |
|---------------------------------|-----------------------------------------------------------------------------|
| ActiveCaptionForeground        | Indicates the color of the caption text in the active state.               |

### Notes

**Note:** These settings will effect only with DockingManager.VisualStyle property set as Default.

#### Code Examples

- **C#**
  ```csharp
  this.dockingManager1.ActiveCaptionFont = new System.Drawing.Font("Trebuchet MS", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));
  this.dockingManager1.ActiveCaptionForeground = System.Drawing.Color.Red;
  ```

- **VB.NET**
  ```vb.net
  Me.dockingManager1.ActiveCaptionFont = New System.Drawing.Font("Trebuchet MS", 9.75!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
  Me.DockingManager1.ActiveCaptionForeground = System.Drawing.Color.Red
  ```

### Figure: Docked Window with Active Caption Foreground Set

![Docked Window with Active Caption Foreground Set](https://example.com/image.png)
*Figure 79: Docked Window with Active Caption Foreground Set*

### Inactive Caption Settings

#### Overview
By setting the `InactiveCaptionFont` and `InactiveCaptionForeground` properties, the caption foreground appearance of the inactive controls among the docked controls can be customized.

### API Reference

- **Properties**
  - `InactiveCaptionFont`
  - `InactiveCaptionForeground`

### Code Examples

#### Example of Setting `InactiveCaptionFont` and `InactiveCaptionForeground`

```csharp
// C#
this.dockingManager1.InactiveCaptionFont = new System.Drawing.Font("Trebuchet MS", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));
this.dockingManager1.InactiveCaptionForeground = System.Drawing.Color.Gray;
```

```vb.net
' VB.NET
Me.dockingManager1.InactiveCaptionFont = New System.Drawing.Font("Trebuchet MS", 9.75!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
Me.DockingManager1.InactiveCaptionForeground = System.Drawing.Color.Gray
```

### Page-level Navigation

- **Page Navigation:** This page provides details on customizing caption foreground colors for both active and inactive docked controls in Syncfusion WinForms.

---

<!-- tags: [Syncfusion WinForms, DockingManager, ActiveCaptionForeground, InactiveCaptionForeground, Customization] keywords: [Customize, Active, Inactive, Caption, Foreground, Docked Controls, Syncfusion, 11.4.0.26] -->
```