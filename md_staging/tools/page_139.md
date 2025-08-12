```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_139.jpeg
document_name: tools
page_number: 139
page_id: tools#page_139
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:48:22Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The below image displays an autohidden docked control.

![](image.png)

*Figure 56: AutoHidden Docked Control*

The below properties control the autohiding feature of the docked controls.

| DockingManager Property           | Description                                                                                          |
|-----------------------------------|------------------------------------------------------------------------------------------------------|
| AutoHideActiveControl            | Gets or sets a value indicating whether to slide back selected auto hidden control.                  |
| AutoHideInterval                 | Specifies the time interval for showing or hiding an autohidden control.                           |
| AutoHideSelectionStyle           | Specifies the selection style for the autohidden windows. The styles are,                           |
|                                   |                                                                                                      |
|                                   | MouseHover - Allows the user to select an autohidden tab by mouse hovering over the tab.           |
|                                   | Click - Allows the user to select the autohidden tab by clicking on the tab.                        |

### Code Examples

#### C#

```csharp
this.dockingManager1.AutoHideActiveControl = true;
this.dockingManager1.AutoHideInterval = 500;
this.dockingManager1.AutoHideSelectionStyle = Syncfusion.Windows.Forms.Tools.AutoHideSelectionStyle.Click;
```

#### VB.NET
```vb
' [unclear] Code for VB.NET is not provided in the image.'
```

## Page-level Navigation/TOC (if applicable)
- None provided in the image.

## Cross References
- None provided in the image.

<!-- tags: [winforms, autohidden, docked control, Syncfusion, AutoHideActiveControl, AutoHideInterval, AutoHideSelectionStyle, Windows Forms] keywords: [AutoHideActiveControl, AutoHideInterval, AutoHideSelectionStyle, Windows Forms, Syncfusion] -->
```