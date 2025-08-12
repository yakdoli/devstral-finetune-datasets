```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_045.jpeg
document_name: diagram
page_number: 045
page_id: diagram#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:29Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This page explains how to add an Overview Control to a Windows Forms form using both the designer and programmatically.
- Demonstrates the process of integrating the Syncfusion Overview Control into a .NET Windows Forms application.
- Provides a step-by-step guide to programmatically creating an Overview control.

## Content

### Designer Form Window Added with Overview Control

#### Figure 22: Designer Form Window Added with Overview Control
![Designer Form Window Added with Overview Control](image.png)

The figure shows the Designer Form Window with an Overview Control integrated. Key elements are labeled:
- **OverviewControl**: The main control in the design view.
- **Smart Tag**: Options for configuring the control.
- **Diagram**: The interactive graphic area.
- **Diagram reference to the OverviewControl**: Highlighting the relationship and reference in the properties.

### 3.2.4.2 Creating an Overview Control through Code

#### Creating an Overview Control through Code

This section shows the step-by-step procedure to create an Overview control programmatically in a .NET Windows Forms application.

**To create an Overview control using code:**

1. Create a new Windows Forms application.
2. Add the following basic dependent Syncfusion assemblies to the project:
   - Syncfusion.Core.dll
   - Syncfusion.Diagram.Base.dll
   - Syncfusion.Diagram.Windows.dll
   - Syncfusion.Shared.Base.dll

3. Create an Overview control using the following code.

## Code Examples

Alternatively, the user can click on the `Add Component` option from the `Project` menu and choose Syncfusion Overview Control. After selecting, the Overview Control will be added to the form and its reference will be added to the `References` section of the Solution Explorer.

```csharp
private void CreateOverviewControl()
{
    // Step 1: Create a new Windows Forms application.

    // Step 2: Add Syncfusion overview control
    var overviewControl = new OverviewControl();
    this.Controls.Add(overviewControl);

    // Optional customization and assignment
    overviewControl.Dock = DockStyle.Fill;
    overviewControl.BackColor = Color.LightGray;
    overviewControl.ForeColor = Color.DarkGray;
}
```

## References
- Syncfusion.Core.dll
- Syncfusion.Diagram.Base.dll
- Syncfusion.Diagram.Windows.dll
- Syncfusion.Shared.Base.dll

<!-- tags: Windows Forms, control, diagram, overview, Syncfusion, Windows Forms User Guide, version: 11.4.0.26 -->
```