```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_168.jpeg
document_name: tools
page_number: 168
page_id: tools#page_168
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:05:31Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

![Caption Background = "PatternStyle"](pattern_style.png)
*Figure 81: Caption Background = "PatternStyle"*

## InactiveCaption settings

By setting the `InactiveCaptionBackground` properties, the caption appearance of the inactive control in the docked controls can be customized.

### DockingManager Property Description
| DockingManager Property              | Description                                                                                                                                                 |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `InactiveCaptionBackground`          | Sets caption background of the inactive docked control using `BrushInfo` object.                                                                              |

### Note:
*This setting will effect only with DockingManager.VisualStudio property set as Default.*

### Code Examples

#### [C#]

```csharp
this.dockingManager1.InActiveCaptionBackground = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Horizontal, System.Drawing.Color.Ivory, System.Drawing.SystemColors.Control);
```

#### [VB.NET]

```vb
Me.DockingManager1.InActiveCaptionBackground = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Horizontal, System.Drawing.Color.Ivory, System.Drawing.SystemColors.Control)
```

### See Also
- Visual Styles

---

<!-- tags: [inactivecaption, captionbackground, visualstyles, syncfusionwinforms, 11.4.0.26] keywords: [dockmanager, gradientstyle, ivory, control, inactivecaptionbackground, visualstyles, csharp, vb.net, docked controls] -->
```