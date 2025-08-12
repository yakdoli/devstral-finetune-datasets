```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_682.jpeg
document_name: tools
page_number: 682
page_id: tools#page_682
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:32Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes orientation settings for panels within the Windows Forms application.
- Details resizing and collapsing functionalities for panels in a split container.

## Content

### Panel Orientation
The panel orientation can be set to either horizontal or vertical. The orientation is controlled using the `System.Windows.Forms.Orientation.Vertical` property.

![Panel Orientation](https://example.com/image424.png)
*Figure 424: Panel Orientation*

### Resizing the Panels
While resizing the control at design time or at run time, we can make one panel as fixed and resize the other panel alone. Select the panel which needs to be fixed, in the `FixedPanel` property.

#### Example Code

**[C#]**
```csharp
this.SplitContainerAdv1.FixedPanel = Syncfusion.Windows.Forms.Tools.Enums.FixedPanel.Panel1
```

**[VB.NET]**
```vb
Me.SplitContainerAdv1.FixedPanel = Syncfusion.Windows.Forms.Tools.Enums.FixedPanel.Panel1
```

### Collapsing a Panel
We can make any of the panels to be collapsed at run time. The below properties help you to do that.

#### SplitContainerAdv Properties and Description

| SplitContainerAdv Properties | Description |
|-----------------------------|-------------|
| Panel1                      | Gives properties of the panel1 which represents the first panel to the left of the Splitter. |
| Panel1Collapsed             | Indicates if the Panel1 is collapsed or not. |
| Panel2                      | Gives properties of the panel2 which represents the last or the second panel to the right of the |
