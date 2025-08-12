---
title: "Gauge - Syncfusion SDK Documentation"
type: "api-documentation"
framework: "syncfusion"
version: "v11"
processing_mode: "Process Isolation (프로세스 격리)"
extracted_date: "1754716537.4107857"
optimized_for: ["llm-training", "rag-retrieval"]
scaling_approach: "3"
---

<!-- 페이지 1 -->

```md
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_001.jpeg
document_name: Gauge
page_number: 001
page_id: Gauge#page_001
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:22Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- Documentation for the Essential Gauge control in the Syncfusion Windows Forms framework.
- Provides functionalities and features for creating and customizing gauge controls within Windows Forms applications.
- Version v.11.4.0.26 of Essential Studio 2013 Volume 4.

## Content
### Introduction
The Essential Gauge for Windows Forms is a versatile control that allows developers to create interactive and visually appealing gauge elements within their Windows-based applications. This control supports various gauge types and provides extensive customization options to meet specific user requirements.

### Features
- Supports multiple gauge types such as Circular, Semi Circular, Linear, and more.
- Customizable appearance options, including colors, styles, and labels.
- Integration with data binding and automation features for real-time data display.

### Getting Started
To begin using the Essential Gauge in your Windows Forms application:
1. Install the Syncfusion Gauge NuGet package.
2. Add a reference to the Gauge control in your project.
3. Drag and drop the Gauge control onto your Windows Form.

### Configuration
- **Customization Options**:
  - Adjust the gauge range, scale, and appearance settings.
  - Implement dynamic changes using event handlers and methods.

- **Example Code**:
  ```csharp
  // Creating and Configuring a Circular Gauge
  using Syncfusion.Windows.Forms.GaugeControl;

  CircularGauge circularGauge = new CircularGauge();
  circularGauge.Minimum = 0;
  circularGauge.Maximum = 100;
  circularGauge.Value = 50;

  // Adding the gauge to the form
  this.Controls.Add(circularGauge);
  ```

### Advanced Usage
- **Data Binding**: Bind the gauge to external data sources for real-time updates.
- **Interaction Events**: Handle user interactions such as mouse over, click, and pointer changes.

### API Reference
#### Properties
- **Value**: Gets or sets the current value displayed on the gauge.
- **Minimum**: Gets or sets the minimum value for the gauge range.
- **Maximum**: Gets or sets the maximum value for the gauge range.
- **Scale**: Provides access to scale customization options.

#### Methods
- **Refresh()**: Updates the display of the gauge.

### Troubleshooting
- Ensure that the necessary references and assemblies are included in the project.
- Verify that the gauge control is properly added to the form's control collection.
- Check for compatibility issues with other controls or libraries.

### Cross References
See also:
- [Syncfusion Documentation: Windows Forms](https://help.syncfusion.com/windowsforms)
- [Syncfusion Support Forum](https://www.syncfusion.com/forums/windowsforms)

<!-- tags: [syncfusion, windowsforms, gauge, control, api, documentation] keywords: [circulargauge, semicircular, lineargauge, customization, data binding, windows forms, version v.11.4.0.26] -->
``` 


---

<!-- 페이지 2 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_005.jpeg
document_name: Gauge
page_number: 005
page_id: Gauge#page_005
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:42Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview

This section provides information on installation, viewing samples through the sample browser, and the locations of samples and source code.

## Installation and Deployment

This section covers information on installation, the process of viewing samples through the sample browser, and the locations of samples and source code.

### 2.1 Installation

For step-by-step installation procedure for the installation of Essential Studio, refer to the Installation topic under Installation and Deployment in the Common UG.

**See Also**

For licensing, patches, and information on adding or removing selective components, refer to the following topics in Common UG under Installation and Deployment:

- Licensing
- Patches
- Add/Remove Components

### 2.2 Samples and Location

This section covers the location of the installed samples and describes the procedure to run the samples through the Sample Browser and online. It also provides the location of the source code.

### 2.2.1 Samples Installation Location

The Gauge samples are installed in the following location locally on the disk:

#### Windows XP:
`C:\Syncfusion\Essential Studio<version number>\Windows\Gauge.Windows\Samples`

#### Windows 7/Vista:
`C:\Users\<user name>\AppData\Local\Syncfusion\EssentialStudio\<version number>\Windows\Gauge.Windows\Samples`

### 2.2.2 Viewing Samples

Use the following steps to view the samples:

1. Click Start > All Programs > Syncfusion > Essential Studio <version number> > Dashboard

The Essential Studio Enterprise Edition window will be displayed.

---

<!-- tags: [Gauge, installation, samples, location] keywords: [installation procedure, sample browser, source code location, licensing, patches, components, Essential Studio, Windows XP, Windows 7/Vista, Sample Installation Location, Viewing Samples] -->
```

---

<!-- 페이지 3 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_009.jpeg
document_name: Gauge
page_number: 009
page_id: Gauge#page_009
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:54Z
fidelity: lossless
-->

## Deployment Requirements

### 2.3.1 DLL List

While deploying an application that references a Syncfusion Windows Forms Gauge control assembly, the following dependencies must be included in the distribution:

- Syncfusion.Core.dll
- Syncfusion.Gauge.Windows.dll
- Syncfusion.Shared.base.dll

```
<!-- tags: [Syncfusion, Winforms, Gauge, deployment, DLL, dependencies] keywords: [Syncfusion.Core.dll, Syncfusion.Gauge.Windows.dll, Syncfusion.Shared.base.dll, deployment requirements, DLL list, Windows Forms, control assembly] -->
```

---

<!-- 페이지 4 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_013.jpeg
document_name: Gauge
page_number: 013
page_id: Gauge#page_013
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:01Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- Demonstrates the default style of the Radial Gauge control in Windows Forms.
- Explains how to add a Radial Gauge to a Windows Forms application using code.

## Content

### Radial Gauge

![Default Radial Gauge](image.png)
*Figure 6: Default Radial Gauge*

As soon as the control is dropped, it will be loaded with its default style.

### Through Code:

#### C# Code Example

```csharp
private Syncfusion.Windows.Forms.Gauge.RadialGauge radialGauge1;
this.radialGauge1 = new Syncfusion.Windows.Forms.Gauge.RadialGauge();
this.radialGauge1.Name = "radialGauge1";
this.radialGauge1.Size = new System.Drawing.Size(230, 230);
this.Controls.Add(this.radialGauge1);
```

#### VB Code Example

```vb
Private radialGauge1 As Syncfusion.Windows.Forms.Gauge.RadialGauge
Me.radialGauge1 = New Syncfusion.Windows.Forms.Gauge.RadialGauge()
Me.radialGauge1.Name = "radialGauge1"
Me.radialGauge1.Size = New System.Drawing.Size(230, 230)
Me.Controls.Add(Me.radialGauge1)
```

### Summary
This section describes how to add a Syncfusion Radial Gauge control to a Windows Forms application, either by dropping it onto the form or by programmatically creating and adding it using C# or VB.Net code.

## Cross References
- See also: ["Syncfusion WinForms Controls Overview"](reference-link)

<!-- tags: [syncfusion, winforms, gauge, radial gauge, windows forms, control, api, version 11.4.0.26] keywords: [Essential Gauge, Radial Gauge, Windows Forms, C#, VB.Net] -->
```


---

<!-- 페이지 5 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_017.jpeg
document_name: Gauge
page_number: 017
page_id: Gauge#page_017
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:14Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- Demonstrates customizing the frame type and background frame of a Radial Gauge.
- Explains the importance of scales in controlling element placement and value ranges.
- Provides code examples in both C# and VB for configuring the Radial Gauge.

## Content

### Setting Frame Type

The following code snippet sets the frame type of the radial gauge to a half-circle.

```csharp
Me.radialGauge1.FrameType = 
Syncfusion.Windows.Forms.Gauge.FrameType.HalfCircle
```

### Configuring ShowBackgroundFrame

The following figure shows the Radial Gauge with `ShowBackgroundFrame` set to `false`, resulting in transparency.

![Figure: ShowBackgroundFrame as False(Transparency)](https://user-images.githubusercontent.com/88415645/233167458-66242e37-537a-4708-9a63-0f8934baf986.png)
*Figure 9: ShowBackgroundFrame as False(Transparency)*

#### Code Example in C#

```csharp
this.radialGauge1.ShowBackgroundFrame = false;
```

#### Code Example in VB

```vb
Me.radialGauge1.ShowBackgroundFrame = false;
```

### Scales

**3.2.2.2 Scales**

Scales are used to control element placement and value ranges.

#### Customizing Scales

You can customize scales added to the Radial Gauge using the properties listed in the following table:

## API Reference

This section will list the specific APIs related to configuring the Radial Gauge, such as properties for `FrameType` and `ShowBackgroundFrame`.

### Code Examples

These examples demonstrate configuring a Radial Gauge in both C# and VB, focusing on frame type and background frame settings.

## Cross References

- Refer to the documentation on different scale configuration options for more details.

### More Information

- For detailed information on scales and their configuration, see the documentation on customizing Radial Gauge properties.

<!-- tags: [radial gauge, frames, scales, transparency, configuration, syncfusion winforms version 11.4.0.26] keywords: [frame type, background frame, showbackgroundframe, customizing scales, label interval, half circle, speedometer, c#, vb, winforms] -->
```

---

<!-- 페이지 6 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: Gauge
page_number: 021
page_id: Gauge#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:29Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- Demonstrates how to configure tick marks and inner lines for a radial gauge in Windows Forms.
- Includes code examples in both C# and VB for setting properties such as tick placement, color, and height.

## Content

### Configuring Tick Marks and Inner Lines
To customize the appearance of tick marks and inner lines in a radial gauge, the following properties can be set:

#### C#
```csharp
this.radialGaugel.MinorTickMarkHeight = 6;
this.radialGaugel.MajorTickMarkHeight = 12;
this.radialGaugel.MinorInnerLinesHeight = 6;
```

#### VB
```vb
Me.radialGaugel.TickPlacement = Syncfusion.Windows.Forms.Gauge.TickPlacement.Outside
Me.radialGaugel.MajorTickMarkColor = System.Drawing.Color.White
Me.radialGaugel.MinorTickMarkColor = System.Drawing.Color.White
Me.radialGaugel.InterLinesColor = System.Drawing.Color.White
Me.radialGaugel.MinorTickMarkHeight = 6
Me.radialGaugel.MajorTickMarkHeight = 12
Me.radialGaugel.MinorInnerLinesHeight = 6
```

#### Explanation
- **TickPlacement**: Sets the placement of the tick marks relative to the gauge.
- **MajorTickMarkColor** and **MinorTickMarkColor**: Define the color of major and minor tick marks.
- **InterLinesColor**: Sets the color of the inner lines.
- **MinorTickMarkHeight** and **MajorTickMarkHeight**: Control the height of minor and major tick marks.
- **MinorInnerLinesHeight**: Controls the height of the minor inner lines.

### Visual Representation
The following image illustrates a radial gauge with customized tick marks and inner lines:

![Radial Gauge](image.png)

### Description of the Image
- The gauge shows a range from 0 to 120.
- Major tick marks are placed at intervals of 10 (e.g., 0, 10, 20, ...).
- Minor tick marks are placed at intervals of 2 between major ticks.
- The gauge features a needle pointing to the center, indicating no specific value.
- The color scheme includes white for tick marks and inner lines.

## API Reference

### Properties
- **TickPlacement**
  - **Type**: `Syncfusion.Windows.Forms.Gauge.TickPlacement`
  - **Default**: `Inside`
  - **Description**: Determines the placement of tick marks (Inside or Outside the gauge).
  
- **MajorTickMarkColor**
  - **Type**: `System.Drawing.Color`
  - **Default**: `Black`
  - **Description**: Sets the color of major tick marks.
  
- **MinorTickMarkColor**
  - **Type**: `System.Drawing.Color`
  - **Default**: `Black`
  - **Description**: Sets the color of minor tick marks.
  
- **InterLinesColor**
  - **Type**: `System.Drawing.Color`
  - **Default**: `Black`
  - **Description**: Sets the color of the inner lines.
  
- **MinorTickMarkHeight**
  - **Type**: `int`
  - **Default**: `4`
  - **Description**: Sets the height of minor tick marks.
  
- **MajorTickMarkHeight**
  - **Type**: `int`
  - **Default**: `8`
  - **Description**: Sets the height of major tick marks.
  
- **MinorInnerLinesHeight**
  - **Type**: `int`
  - **Default**: `4`
  - **Description**: Sets the height of minor inner lines.

## Code Examples

### Full Example in C#

```csharp
using System;
using System.Drawing;
using Syncfusion.Windows.Forms.Gauge;

public class RadialGaugeExample
{
    public void ConfigureGauge()
    {
        RadialGauge radialGaugel = new RadialGauge();

        // Configure tick marks and inner lines
        radialGaugel.TickPlacement = TickPlacement.Outside;
        radialGaugel.MajorTickMarkColor = Color.White;
        radialGaugel.MinorTickMarkColor = Color.White;
        radialGaugel.InterLinesColor = Color.White;
        radialGaugel.MinorTickMarkHeight = 6;
        radialGaugel.MajorTickMarkHeight = 12;
        radialGaugel.MinorInnerLinesHeight = 6;

        // Additional configurations...
    }
}
```

### Full Example in VB

```vb
Imports System
Imports System.Drawing
Imports Syncfusion.Windows.Forms.Gauge

Public Class RadialGaugeExample
    Public Sub ConfigureGauge()
        Dim radialGaugel As New RadialGauge()

        ' Configure tick marks and inner lines
        radialGaugel.TickPlacement = TickPlacement.Outside
        radialGaugel.MajorTickMarkColor = Color.White
        radialGaugel.MinorTickMarkColor = Color.White
        radialGaugel.InterLinesColor = Color.White
        radialGaugel.MinorTickMarkHeight = 6
        radialGaugel.MajorTickMarkHeight = 12
        radialGaugel.MinorInnerLinesHeight = 6

        ' Additional configurations...
    End Sub
End Class
```

## Cross References
- Refer to the [Gauge Overview](#gauge-overview) for an introduction to the Gauge control.
- Refer to the [Customizations](#customizations) section for more examples of configuring the Gauge control.

<!-- tags: [Gauge, Windows Forms, Tick Marks, Inner Lines, Radial Gauge, Syncfusion, Version 11.4.0.26] keywords: [RadialGauge, TickPlacement, MajorTickMarkColor, MinorTickMarkColor, InterLinesColor, MinorTickMarkHeight, MajorTickMarkHeight, MinorInnerLinesHeight] -->
```


---

<!-- 페이지 7 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_025.jpeg
document_name: Gauge
page_number: 025
page_id: Gauge#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:15:00Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- Demonstrates the usage of Rangplacement within a gauge control.
- Explains configurations for "RangePlacement Inside" and "RangePlacement Outside".
- Discusses scaling divisions in a gauge.

## Content

### 3.2.2.6 Scaling Divisions

#### Overview of RangePlacement Inside

![](Unclear: Figure 15: RangePlacement Inside)

#### Overview of RangePlacement Outside

![](Unclear: Figure 16: RangePlacement Outside)

---

## Page-level Navigation/TOC

- **3.2.2.6 Scaling Divisions**
  - RangePlacement Inside
  - RangePlacement Outside

---

## Cross References

- **See also:** Rangplacement options, gauge configurations.

---

<!-- tags: [Gauge, RangePlacement, ScalingDivisions, WindowsForms] keywords: [RangePlacementInside, RangePlacementOutside, ScalingDivisions, WindowsFormsGauge] -->
```

---

<!-- 페이지 8 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_029.jpeg
document_name: Gauge
page_number: 029
page_id: Gauge#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:15:09Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

![Metro](https://<image_url>/Metro)

## 3.4 Data Binding

You can bind any data source to the RadialGauge and map an index of a record to represent the actual value in RadialGauge. The DisplayMember and DisplayRecordIndex properties will map the DataColumn and DataRow of the binding source respectively to the Gauge control, which will then support high frequency data updates.

### Example

```csharp
this.radialGauge1.DataSource = dataTable;
this.radialGauge1.DisplayRecordIndex = [Row Index];
this.radialGauge1.DisplayMember = [column name];
```

### [ASPx]

```html
<input type="text" value="" id="SetDropDownText" />
<input type="button" value="Set Text" id="setText" />

<script type="text/javascript">
    $("#setText").bind('click', function () {
        var multiDD = $find("MultiColumnDropdown");
        multiDD.setText($('#SetDropDownText').val());
    });
</script>
```

## Page-level Navigation/TOC (if applicable)
- 3.4 Data Binding

## Cross References
See also: [Additional References]

## RAG Annotations
<!-- tags: [Metro, Windows Forms, RadialGauge, Data Binding, DisplayMember, DisplayRecordIndex, DataColumn, DataRow, Gauge control] keywords: [Metro, RadialGauge, Data Binding, DisplayMember, DisplayRecordIndex, DataColumn, DataRow, Gauge control] -->
```

---

<!-- 페이지 9 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_002.jpeg
document_name: Gauge
page_number: 002
page_id: Gauge#page_002
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:22Z
fidelity: lossless
-->

# Contents

## Overview

- **1.1 Introduction to Gauge for Windows Forms** ..... 3
- **1.2 Prerequisites and Compatibility**
  - **1.2.1 Prerequisites** ..... 3
  - **1.2.2 Compatibility** ..... 3

## Installation and Deployment

- **2.1 Installation** ..... 5
- **2.2 Samples and Location**
  - **2.2.1 Samples Installation Location** ..... 5
  - **2.2.2 Viewing Samples** ..... 5
  - **2.2.3 Source Code Location** ..... 8
- **2.3 Deployment Requirements** ..... 9
  - **2.3.1 DLL List** ..... 9

## Radial Gauge

- **3.1 Real World Scenarios** ..... 11
- **3.2 Getting Started**
  - **3.2.1.1 Creating a Radial Gauge** ..... 12
  - **3.2.1.2 Elaborate Structure of the Control** ..... 14
  - **3.2.2 Concepts and Features** ..... 14
    - **3.2.2.1 Radial Gauge Frame** ..... 14
    - **3.2.2.2 Scales** ..... 17
    - **3.2.2.3 Ticks** ..... 19
    - **3.2.2.4 Needles** ..... 22
    - **3.2.2.5 Ranges** ..... 23
    - **3.2.2.6 Scaling Divisions** ..... 25
- **3.3 Visual Styles for all the Gauges** ..... 26
- **3.4 Data Binding** ..... 29

## Notes and Cross References

- **Note:** This page provides an overview of the contents of the document, covering key sections like Overview, Installation and Deployment, and Radial Gauge. Each section discusses the essential features and requirements for using Gauge in Windows Forms.

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [Gauge, Windows Forms, Installation, Deployment, Radial Gauge, Data Binding, Compatibility, Samples] -->
```

---

<!-- 페이지 10 -->

```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_006.jpeg
document_name: Gauge
page_number: 006
page_id: Gauge#page_006
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:37Z
fidelity: lossless
-->

## Essential Gauge for Windows Forms

### Overview
- Provides a suite of UI, Reporting, and BI controls for professional desktop applications in Windows Forms.
- Supports Visual Studio 2012, Windows 8, and .NET 4.5, ensuring compatibility and advanced functionality.

## Content

### Figure 1: Syncfusion Essential Studio Dashboard
![Syncfusion Essential Studio Dashboard](https://<image_url>)

**Description of Figure 1:**
- The Essential Studio window, providing various UI controls for Windows Forms development.
- Features include 100+ UI controls for creating professional desktop applications.
- Navigation options for Windows Forms, WPF, ASP.NET MVC, ASP.NET, Silverlight, Windows Phone, Mobile MVC, and WinRT.

### Steps to Access Samples
1. In the Dashboard window, click **Run Samples for Windows Forms** under **UI Edition**.
   - The **UI Windows Forms Sample Browser** window will be displayed.

### Note: Viewing Samples
You can view the samples in any of the following three ways:
- **Run Samples**: Click to view the locally installed samples.
- **Online Samples**: Click to view online samples.
- **Explore Samples**: Explore the UI for Windows Forms on disk.

### User Interface Edition Panel
- The **User Interface Edition panel** is displayed by default.

## API Reference

Not directly provided in this image. For detailed API information, please refer to the full documentation or online resources.

## Code Examples

### C#
No code examples are provided in this image. For implementation details, refer to the complete user guide or documentation.

### VB.NET
No specific VB.NET code examples are provided in this image. Additional coding examples can be found in the full user guide.

## Page-level Navigation/TOC

Not specifically listed in this image. For a comprehensive table of contents, refer to the user guide or documentation.

## Cross References

### Additional Resources
- **Sales**: Contact support for inquiries.
- **Recheck**: Administrator Level Access Required for certain functionalities.
- **Documentation**: Access online documentation for detailed guidance.
- **Release Notes**: Check release notes for the latest updates.
- **Read Me**: Access the Read Me file for additional information.

## RAG Annotations

<!-- tags: Essential Studio, Windows Forms, UI controls, .NET 4.5, Syncfusion Winforms, version: 11.4.0.26 keywords: UI, Reporting, BI, desktop applications, Visual Studio 2012, Windows 8, .NET 4.5, local samples, online samples, disk exploration -->
```

---

<!-- 페이지 11 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_010.jpeg
document_name: Gauge
page_number: 010
page_id: Gauge#page_010
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:52Z
fidelity: lossless
-->

## Overview
- Focus on configuring and customizing the appearance of the CircularGauge control.
- Detailed instructions on setting up major and minor ticks, labels, and annotations.
- Highlighting the usage of GaugeStyle to enhance aesthetic visualization.

## Content

### Customizing Tick Appearance
The CircularGauge control provides numerous options to customize the appearance of ticks, including major ticks and minor ticks. These ticks can be used to divide the range and enhance the readability of the gauge.

#### Major Ticks
Major ticks are used to mark specific intervals on the gauge scale and are a prominent visual element. You can customize the appearance of major ticks using the following properties:

- **Width**: Specifies the width of the tick.
- **Height**: Specifies the length of the tick.
- **Color**: Specifies the color of the tick.
- **LineStyle**: Changes the line style of the tick (Solid, Dash, Dotted, etc.).
- **Offset**: Controls the distance from the center where the tick is drawn.

**Example:**
```csharp
circularGauge1.MajorTicks.Width = 2;
circularGauge1.MajorTicks.Height = 10;
circularGauge1.MajorTicks.Color = Color.Black;
circularGauge1.MajorTicks.LineStyle = DashStyle.Dash;
circularGauge1.MajorTicks.Offset = 0.8;
```

#### Minor Ticks
Minor ticks provide additional divisions between major ticks and enhance the granularity of the gauge scale. You can customize minor ticks using the following properties:

- **Width**: Specifies the width of the minor tick.
- **Height**: Specifies the length of the minor tick.
- **Color**: Specifies the color of the minor tick.
- **LineStyle**: Changes the line style of the minor tick.
- **Offset**: Controls the distance from the center where the minor tick is drawn.
- **Steps**: Specifies the number of intervals between each major tick.

**Example:**
```csharp
circularGauge1.MinorTicks.Width = 1;
circularGauge1.MinorTicks.Height = 5;
circularGauge1.MinorTicks.Color = Color.Gray;
circularGauge1.MinorTicks.LineStyle = DashStyle.Solid;
circularGauge1.MinorTicks.Offset = 0.85;
circularGauge1.MinorTicks.Steps = 5;
```

### Configuring Labels
Labels are used to assign numerical or textual values to the ticks on the gauge. You can customize labels using the following properties:

- **Font**: Specifies the font style, size, and weight of the label text.
- **Text**: Specifies the content of the label.
- **Color**: Specifies the color of the label text.
- **Format**: Specifies how the value should be formatted (e.g., "##.##" for decimal points).
- **Offset**: Controls the distance from the center where the label is positioned.
- **Position**: Determines whether the label should be placed inside or outside the gauge.

**Example:**
```csharp
circularGauge1.Labels.Font = new Font("Arial", 10, FontStyle.Bold);
circularGauge1.Labels.Color = Color.Black;
circularGauge1.Labels.Format = "##.##";
circularGauge1.Labels.Offset = 1.2;
circularGauge1.Labels.Position = GaugeTextPosition.Outside;
```

### Adding Annotations
Annotations allow you to include additional visual elements, such as text or images, on the gauge to convey important information to the user. These annotations can be positioned at specific coordinates on the gauge.

**Example:**
```csharp
circularGauge1.Annotations.Add(new CircularGaugeAnnotation
{
    RoundShape = true,
    Size = new SizeF(15, 15),
    Offset = new PointF(0, 0),
    FillStyle = new FillStyle
    {
        Color = Color.DarkRed
    },
    Text = "Error!"
});
```

### Setting the Gauge Style
The GaugeStyle property is used to set a pre-defined aesthetic theme for the gauge. Syncfusion provides several predefined styles such as "None", "Classic", "Modern", etc. You can also create a custom style and apply it to your gauge.

**Example:**
```csharp
circularGauge1.Style = CircularGaugeGaugeStyle.Classic;
```

If you need a more customized look, you can create a custom style and override the properties:

**Example:**
```csharp
circularGauge1.Style = new CircularGaugeCustomStyle();
circularGauge1.Style.Background = new FillStyle
{
    GradientStyle = GradientStyle.Linear,
    StartColor = Color.LightBlue,
    EndColor = Color.White,
};
```

By combining these customization options, you can create a visually appealing and functional CircularGauge control tailored to your specific application needs.

## Code Examples

### Major Ticks
```csharp
using Syncfusion.Windows.Forms.CircularGauge;

circularGauge1.MajorTicks.Width = 2;
circularGauge1.MajorTicks.Height = 10;
circularGauge1.MajorTicks.Color = Color.Black;
circularGauge1.MajorTicks.LineStyle = DashStyle.Dash;
circularGauge1.MajorTicks.Offset = 0.8;
```

### Minor Ticks
```csharp
using Syncfusion.Windows.Forms.CircularGauge;

circularGauge1.MinorTicks.Width = 1;
circularGauge1.MinorTicks.Height = 5;
circularGauge1.MinorTicks.Color = Color.Gray;
circularGauge1.MinorTicks.LineStyle = DashStyle.Solid;
circularGauge1.MinorTicks.Offset = 0.85;
circularGauge1.MinorTicks.Steps = 5;
```

### Labels
```csharp
using Syncfusion.Windows.Forms.CircularGauge;

circularGauge1.Labels.Font = new Font("Arial", 10, FontStyle.Bold);
circularGauge1.Labels.Color = Color.Black;
circularGauge1.Labels.Format = "##.##";
circularGauge1.Labels.Offset = 1.2;
circularGauge1.Labels.Position = GaugeTextPosition.Outside;
```

## Cross References
- **Related Documentation:** 
    - [Syncfusion CircularGauge Overview](#overview)
    - [Gauge Customization Techniques](#customization)
    - [Styling and Themes in CircularGauge](#styling)

## RAG Annotations
<!-- tags: circulargauge, winforms, customization, ticks, labels, annotations, style, gauge, syncfusion-sdk keywords: major ticks, minor ticks, labels, annotations, gauge style, customization, winforms controls -->
```

---

<!-- 페이지 12 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_014.jpeg
document_name: Gauge
page_number: 014
page_id: Gauge#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:29Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## 3.2.1.2 Elaborate Structure of the Control

The RadialGauge control includes the following elements: Scale Label, Needle, Gauge Value, and Background Frame. All the elements are optional for displaying the Gauge control.

### Feature Summary:

Here is a brief overview of various features of the RadialGauge control.

- **Scales**—The scale value can be customized to be displayed within defined limits.
- **Frame types**—Allows you to specify the radial built-in frame style, such as full circle or half circle.
- **Pointers**—Provide complete support for pointers to point the value.
- **Range**—Full-fledged range support.
- **Image and Labels**—Used to customize the appearance of gauge pointer values with user-specified colors and alignment.

## 3.2.2 Concepts and Features

This section illustrates the features of Radial Gauge with images and sample code. It contains the following topics:

- **Radial Gauge Frames**
- **Scales**
- **Ticks**
- **Needles**
- **Ranges**
- **Scaling Divisions**

### 3.2.2.1 Radial Gauge Frame

The frame defines the frame types of radial gauges. Frames can be applied using the FrameType property. The RadialGauge control contains two frame types:

- **Full Circle**
- **Half Circle**

#### Property Table

| Property                    | Type    | Description                                                        |
|-----------------------------|---------|--------------------------------------------------------------------|
| **FrameType**               | Enum    | Gets or sets the frame type.                                      |
| **ShowBackgroundFrame**     | Boolean | Gets or sets the visibility of the background frame.           |

## Code Examples (multi-language supported)

- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

## Page-level Navigation/TOC (if applicable)

- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References

- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations

<!-- tags: [radialgauge, Syncfusion, Winforms, Gauge, control, api, version] keywords: [RadialGauge, Scale, Frame, Pointer, Range, Customization, Full Circle, Half Circle, Property, Enum, Boolean, Visibility, Developers, Design, Implementation] -->
```

---

<!-- 페이지 13 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_018.jpeg
document_name: Gauge
page_number: 018
page_id: Gauge#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:45Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- This page provides an overview of the Essential Gauge control for Windows Forms.
- It includes detailed property descriptions and a visual example of the gauge layout.
- The properties listed help in customizing the appearance and behavior of the gauge.

## Content

### Table 3: Property Table

| Property            | Type     | Description                                                                 |
|---------------------|----------|-----------------------------------------------------------------------------|
| ShowScaleLabel      | Boolean  | Gets or sets the scale label visibility.                                |
| ScaleLabelColor     | Color    | Gets or sets the scale label color of the gauge.                        |
| LabelPlacement      | Enum     | Gets or sets whether to place the ticks inside or outside the arc.     |
| TextOrientation     | Enum     | Gets or sets the text orientation layout.                                |

### Figure 10: Scale outside the arc

![Scale outside the arc](https://example.com/image.png)
*Figure 10: Scale outside the arc*

## API Reference

### Properties
- **ShowScaleLabel**: Boolean
  - Description: Gets or sets the visibility of the scale label.
- **ScaleLabelColor**: Color
  - Description: Gets or sets the color of the scale label.
- **LabelPlacement**: Enum
  - Description: Gets or sets the placement of ticks relative to the arc.
- **TextOrientation**: Enum
  - Description: Gets or sets the orientation layout of the text.

## Code Examples

### Example: Configuring Gauge Properties

```csharp
// Example of configuring gauge properties
Syncfusion.Windows.Forms.GaugeControl gauge = new Syncfusion.Windows.Forms.GaugeControl();
gauge.ShowScaleLabel = true;
gauge.ScaleLabelColor = Color.Red;
gauge.LabelPlacement = Syncfusion.Windows.Forms.Gauge.LabelPlacementType.Outside;
gauge.TextOrientation = Syncfusion.Windows.Forms.Gauge.TextOrientationType.Vertical;
```

## RAG Annotations
<!-- tags: [Gauge, Windows Forms, properties, customization, ScaleLabel, LabelPlacement, TextOrientation] keywords: [Essential Gauge, Windows Forms, control, properties, visibility, placement, orientation, color, scale label, text] -->
```

---

<!-- 페이지 14 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_022.jpeg
document_name: Gauge
page_number: 022
page_id: Gauge#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:59Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Content

### TickPlacement

#### Figure 12: TickPlacement Inside

![](image1.png)

#### Figure 13: TickPlacement Outside

![](image2.png)

### 3.2.2.4 Needles

You can easily customize the style of the needle and the positions of the sub elements within the RadialGauge through the following enumerations.

#### Figure 14: Default and Advanced pointer styles

![](image3.png)

### Properties

| Property      | Type   | Description                     |
|---------------|--------|-----------------------------------|
| NeedleColor   | Color  | Gets or sets the gauge needle color. |

## Page-level Navigation/TOC (if applicable)

- **TickPlacement**
  - TickPlacement Inside (Figure 12)
  - TickPlacement Outside (Figure 13)
- **Needles**
  - Customizing Needle Styles (Figure 14)
  - Properties

## Cross References

See also:
- [RadialGauge](#)
- [Customizing the Style of the Needle](#)

<!-- tags: [RadialGauge, CustomizingNeedles, NeedleColor] keywords: [tickplacement, inside, outside, needlestyles, properties] -->
```

---

<!-- 페이지 15 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_026.jpeg
document_name: Gauge
page_number: 026
page_id: Gauge#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:15:09Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

The Gauge control for Windows Forms includes support for customizing the number of major tick lines and number of minor tick lines using the **Major Difference** and **Minor Difference**. It also provides support to customize the number of tick lines using **MaximumValue** and **MinimumValue**.

## Properties

| Property          | Type       | Description                                                                 |
|-------------------|------------|-----------------------------------------------------------------------------|
| Minimum           | Float      | Gets or sets the minimum value for the radial scale. Default value is set to 0. |
| Maximum           | Float      | Gets or sets the maximum value for the radial scale. Default value is set to 120. |
| MajorDifference   | Float      | Gets or sets the major difference value. |
| MinorDifference   | Integer    | Gets or sets the minor difference value. |

### Example Code

- **C#**

    ```csharp
    this.radialGauge1.MajorDifference = 20F;
    this.radialGauge1.MaximumValue = 120F;
    this.radialGauge1.MinimumValue = 0F;
    this.radialGauge1.MinorDifference = 1;
    ```

- **VB**

    ```vb
    Me.radialGauge1.MajorDifference = 20F
    Me.radialGauge1.MaximumValue = 120F
    Me.radialGauge1.MinimumValue = 0F
    Me.radialGauge1.MinorDifference = 1
    ```

## 3.3 Visual Styles for all the Gauges

The Gauge control for Windows Forms includes four stunning skins for professional representation of gauges. You can easily modify the look and feel of the gauge component using the built-in visual styles and color schemes.

<!-- tags: [gauge, windows forms, visual styles, major difference, minor difference, maximum value, minimum value] keywords: [gauge control, windows forms, visual styles, customization, major ticks, minor ticks] -->
``` 


---

<!-- 페이지 16 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_030.jpeg
document_name: Gauge
page_number: 030
page_id: Gauge#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:15:22Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- This section provides insights into using the <script> tag to integrate JavaScript functionalities with a Windows Forms application that includes synchronization with Gauge controls.
- Demonstrate the usage of script files or embed-inline scripts as shown in the example snippet.

## Content

### Using the <script> Tag in Windows Forms

The `<script>` tag is typically associated with web development, embedding or importing JavaScript files or code directly into an HTML document. However, within the context of Windows Forms using Syncfusion's Essential Gauge, its use here may not be directly applicable.

#### Example Code
```xml
<script>
    <!-- Content or reference to scripts goes here -->
</script>
```

This inclusion indicates the intention to enhance the Gauge control behavior via JavaScript, suggesting a hybrid approach where dynamic functionalities are integrated with the native Windows Forms environment. This is a common scenario in modern development, particularly when leveraging JavaScript libraries alongside traditional desktop applications.

### Technical Considerations
- Ensure that the JavaScript references or inline scripts specified in the <script> tag are compatible with the JavaScript engine being utilized in the Windows Forms application.
- The embedded or external scripts should align with the functionality and features provided by Syncfusion's Essential Gauge control, ensuring that any additional logic complements rather than conflicts with the control’s native capabilities.

### Best Practices
- Always validate any external script references to ensure that they come from a secure and reliable source to prevent security vulnerabilities.
- Maintain clear documentation and comments within your scripts to facilitate maintenance and future updates.

## Code Examples

### Example 1: Embedding Custom JavaScript Functionality
```csharp
// This example assumes that the JavaScript functionality is embedded directly in your Windows Forms application.
public void LoadCustomScripts()
{
    // Invoke JavaScript functions or script logic here
    // Example: Integrating external scripts or inline JavaScript logic for enhanced functionality.
    // This is typically done via the WebBrowser control or similar mechanisms that can evaluate JavaScript.
    // Ensure the appropriate namespaces and references are included within your application.
}
```

## Page-level Navigation/TOC (if applicable)
- [Top]
- [Introduction to Using Scripts with Windows Forms]
- [Technical Considerations]
- [Example Code & Best Practices]

<!-- tags: Glyph, Essential Gauge, Windows Forms, JavaScript, Syncfusion, Compatibility, Script Integration, Hybrid Application Development keywords: Gauge, Windows Forms, Script, JavaScript, Syncfusion, Code Examples, Reference -->
```

---

<!-- 페이지 17 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_003.jpeg
document_name: Gauge
page_number: 003
page_id: Gauge#page_003
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:22Z
fidelity: lossless
-->

## Overview

This section covers information on the Gauge control for Windows Forms, its key features, prerequisites to use the control, compatibility with various operating systems, and other documentation details for the product. It comprises the following topics:
- Introduction
- Installation and Deployment
- Getting Started
- Gauge for Windows Forms controls

### 1.1 Introduction to Gauge for Windows Forms

The Gauge control for Windows Forms is a data visualization tool that can be used to display several data points or data ranges in a precise and compact area. The data displayed in the control can be quickly understood by the user. Syncfusion's Windows Forms library enables users to configure the Gauge control through C# codes. The Gauge control comes with sophisticated customization support.

The Gauge control is intended for developers who want to use gauges in their Windows Forms applications. It is a very useful control to indicate the current value in a range of values.

### 1.2 Prerequisites and Compatibility

This section covers the requirements for using Gauge control. It also lists operating systems and browsers compatible with the product.

#### 1.2.1 Prerequisites

The prerequisites details are listed below:

| **Development Environments** |                                                                                                    |
|------------------------------|----------------------------------------------------------------------------------------------------|
| Visual Studio 2012 (Ultimate, Premium, Professional and Express) |                                                                 |
| Visual Studio 2010 (Ultimate, Premium, Professional and Express) |                                                                 |
| Visual Studio 2008 with SP1 (Team, Professional, Standard and Express) |                                                             |

The .NET Framework versions required are:

- .NET 4.5
- .NET 4.0
- .NET 3.5 SP1

### 1.2.2 Compatibility

The compatibility details are as follows:

---

<!-- tags: [gauge, windows forms, user guide, prerequisites, compatibility] keywords: [gauge control, data visualization, windows forms, visual studio, .NET framework, development environments] -->
```

---

<!-- 페이지 18 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_007.jpeg
document_name: Gauge
page_number: 007
page_id: Gauge#page_007
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:36Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- A catalog of essential features for working with Syncfusion Gauge controls in Windows Forms.
- Showcase, Grids, Data Visualization, Layout, and Editing capabilities are highlighted.
- Guide to navigating the UI Windows Forms Sample Browser to access the Gauge samples.

## Content

### Navigation Instructions

#### Figure 2: UI Windows Forms Sample Browser
This figure displays the Windows Forms Sample Browser interface, categorized as follows:

- **Showcase**: Includes various demo applications like Invoice, Outlook Demo, Succinity Series, VS2012 Demo, and Trader Grid Test Demo.
- **Grids**: Represents different grid types such as Cell Grid, Date Grid, and Pivot Grid.
- **Data Visualization**: Includes Diagram, Barcode, Schedule, Gauge, and Chart.
- **Layout**: Features Ribbon, Docking Manager, Tile Layout, Carousel, Metro Form, and Container Controls.

#### Steps to Access Gauge Samples
1. **Locate the Data Visualization Category**: Navigate to the "Data Visualization" section in the browser.
2. **Click the Gauge Tile**: Select the Gauge tile under the Data Visualization category.
3. **View the Gauge Samples**: After clicking the Gauge tile, the Gauge samples will be displayed.

## API Reference

This section would detail the APIs related to the Gauge control, including methods, properties, and events. However, the current content does not include specific API information, so this section remains placeholder text.

## Code Examples

### Example: Displaying the UI Windows Forms Sample Browser
This section would include example code snippets demonstrating how to set up and use the Gauge control within a Windows Forms application. Below is a placeholder example:

```csharp
// Example code will be inserted here to demonstrate usage of the Gauge control.
```

## Related Sections

- Refer to the next section or documentation for detailed usage examples and customization options for the Gauge control.

<!-- tags: [syncfusion, windows forms, gauge, data visualization, UI, UI sample browser, version 11.4.0.26] keywords: [gauge samples, showcase, grids, layout, editing, data visualization, UI sample browser] -->
```

---

<!-- 페이지 19 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_011.jpeg
document_name: Gauge
page_number: 011
page_id: Gauge#page_011
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:49Z
fidelity: lossless
-->

# 3 Radial Gauge

The RadialGauge control can be used for representing a range of values in circular form. It can be used to create sophisticated dashboards, clocks, industrial equipment, medical equipment, more.

## 3.1 Real World Scenarios

A radial gauge evaluates the values of scales and presents them in a radial manner. Radial Gauge enables you to quickly build high quality dashboard, process control, gadget and clocks. Radial gauges consist of important internal domains to present data in a more sophisticated way.

The best example of a radial gauge is a speedometer. The speedometer can be designed to be placed in a racing game application, denoting the speed of a vehicle.

![Speedometer](image.png "Figure 4: Speedometer")

## 3.2 Getting Started

This section provides information about radial gauges for developers who are new to the Gauge control.
```

---

<!-- 페이지 20 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: Gauge
page_number: 015
page_id: Gauge#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:58Z
fidelity: lossless
-->

## Overview
- Discusses the properties related to setting colors and visibility for different parts of the gauge control in Windows Forms.
- Focuses on gradient colors for the background, inner frame, and outer frame.
- Includes properties for setting the color of the gauge arc, label, and value.
- Contains a boolean property for controlling the visibility of the gauge value.

## Content

The following table summarizes the properties related to configuring the visual appearance of the gauge control:

### Gauge Properties
| Property Name                | Type      | Description                                                                 |
|------------------------------|-----------|-----------------------------------------------------------------------------|
| BackgroundGradientStartColor | Color     | Gets or sets the gradient start color for the gauge background.           |
| BackgroundGradientEndColor   | Color     | Gets or sets the gradient end color for the gauge background.              |
| InnerFrameGradientStartColor | Color     | Gets or sets the gradient start color for the inner frame.                |
| InnerFrameGradientEndColor   | Color     | Gets or sets the gradient end color for the inner frame.                  |
| OuterFrameGradientStartColor | Color     | Gets or sets the gradient start color for the outer frame.                |
| OuterFrameGradientEndColor   | Color     | Gets or sets the gradient end color for the outer frame.                  |
| GaugeArcColor                | Color     | Gets or sets the arc color of the gauge.                                |
| GaugeLableColor              | Color     | Gets or sets the gauge label color.                                     |
| GaugeValueColor              | Color     | Gets or sets the gauge value color.                                     |
| ShowGaugeValue               | Boolean   | Gets or sets the gauge value visibility.                                |

## API Reference

### Properties
The following table lists the properties and their descriptions:

| Property Name                | Type      | Description                                                                 |
|------------------------------|-----------|-----------------------------------------------------------------------------|
| BackgroundGradientStartColor | Color     | Gets or sets the gradient start color for the gauge background.           |
| BackgroundGradientEndColor   | Color     | Gets or sets the gradient end color for the gauge background.              |
| InnerFrameGradientStartColor | Color     | Gets or sets the gradient start color for the inner frame.                |
| InnerFrameGradientEndColor   | Color     | Gets or sets the gradient end color for the inner frame.                  |
| OuterFrameGradientStartColor | Color     | Gets or sets the gradient start color for the outer frame.                |
| OuterFrameGradientEndColor   | Color     | Gets or sets the gradient end color for the outer frame.                  |
| GaugeArcColor                | Color     | Gets or sets the arc color of the gauge.                                |
| GaugeLableColor              | Color     | Gets or sets the gauge label color.                                     |
| GaugeValueColor              | Color     | Gets or sets the gauge value color.                                     |
| ShowGaugeValue               | Boolean   | Gets or sets the gauge value visibility.                                |

## Code Examples

### Setting Colors and Visibility
```csharp
// Example: Setting background gradient colors
gauge1.BackgroundGradientStartColor = Color.Red;
gauge1.BackgroundGradientEndColor = Color.Blue;

// Example: Setting frame gradient colors
gauge1.InnerFrameGradientStartColor = Color.Green;
gauge1.InnerFrameGradientEndColor = Color.Yellow;
gauge1.OuterFrameGradientStartColor = Color.Orange;
gauge1.OuterFrameGradientEndColor = Color.Purple;

// Example: Setting gauge arc, label, and value colors
gauge1.GaugeArcColor = Color.Black;
gauge1.GaugeLableColor = Color.White;
gauge1.GaugeValueColor = Color.Gray;

// Example: Showing or hiding the gauge value
gauge1.ShowGaugeValue = true;
```

## Cross References
- For more information on configuring other aspects of the gauge control, see the [Gauge Control Documentation](#gauge-control-documentation).
- Additional details on color management and gradients can be found in the [Color and Gradient Properties](#color-and-gradient-properties) section.

<!-- tags: [gauge, windows forms, color, gradient, visibility] keywords: [color, gradient, background, frame, arc, label, value, visibility] -->
```

---

<!-- 페이지 21 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_019.jpeg
document_name: Gauge
page_number: 019
page_id: Gauge#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:22Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Content

### Scale inside the arc

- **Figure 11:** Scale inside the arc

This image illustrates the placement of labels inside the arc of a RadialGauge.

### Placing Labels in the RadialGauge Control

The following code sample demonstrates how to place labels in the RadialGauge control:

#### C# Code Sample

```csharp
this.radialGauge1.LabelPlacement = 
    Syncfusion.Windows.Forms.Gauge.LabelPlacement.Outside;

this.radialGauge1.TextOrientation = 
    Syncfusion.Windows.Forms.Gauge.TextOrientation.SlideOver;
```

#### VB Code Sample

```vb
Me.radialGauge1.LabelPlacement = 
    Syncfusion.Windows.Forms.Gauge.LabelPlacement.Outside

Me.radialGauge1.TextOrientation = 
    Syncfusion.Windows.Forms.Gauge.TextOrientation.SlideOver
```

### 3.2.2.3 Ticks

This section discusses the configuration and properties of ticks in a gauge control.

## Code Examples

Example code snippets are provided in both C# and VB to demonstrate the configuration of ticks and labels within a RadialGauge.

## API Reference

This section covers the various properties, methods, and events associated with the RadialGauge control, focusing on label placement and tick configurations.

#### Properties

- **LabelPlacement**: Determines the placement of labels in the RadialGauge (inside or outside the arc).
- **TextOrientation**: Defines how the text orientation is applied to labels; options include `SlideOver`.

### Cross References

For more information on configuring other aspects of the RadialGauge, refer to the [Syncfusion WinForms documentation](https://www.syncfusion.com/documentation/windowsforms).

<!-- tags: [Syncfusion Windows Forms, RadialGauge, LabelPlacement, TextOrientation, Ticks, C#, VB, Windows Forms User Guide] 
keywords: [Syncfusion, Windows Forms, RadialGauge, Label Placement, Text Orientation, Ticks, CSharp, VB.NET, User Guide, SDK, Documentation, Gauge Control, Configuration, Placement, Orientation, Examples] -->
``` 


---

<!-- 페이지 22 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_023.jpeg
document_name: Gauge
page_number: 023
page_id: Gauge#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:36Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- Explains how to customize needle styles and visibility in a radial gauge.
- Demonstrates setting needle properties such as color and style in C# and VB.
- Introduces the concept of ranges in a gauge to highlight value ranges.
- Lists attributes for customizing ranges including start/end values and placement.

## Content

### Customizing Needle Styles and Visibility

The following properties can be used to set the needle style and visibility in a radial gauge:

| Property      | Type   | Description                |
|---------------|--------|-----------------------------|
| NeedleStyle  | Enum   | Gets or sets the needle style. |
| ShowNeedle   | Boolean| Gets or sets the needle visibility. |

#### Code Examples

##### C#
```csharp
this.radialGauge1.ShowNeedle = true;
this.radialGauge1.NeedleColor = System.Drawing.Color.Black;
this.radialGauge1.NeedleStyle = Syncfusion.Windows.Forms.Gauge.NeedleStyle.Advanced;
```

##### VB
```vb
Me.radialGauge1.ShowNeedle = True
Me.radialGauge1.NeedleColor = System.Drawing.Color.Black
Me.radialGauge1.NeedleStyle = Syncfusion.Windows.Forms.Gauge.NeedleStyle.Advanced
```

### 3.2.2.5 Ranges

Ranges are objects that highlight a range of values and can display different ranges in different colors. Ranges can be customized using various attributes such as range placement, height, color of the range, and so on. All the available attributes are listed in the following table:

| Property         | Type   | Description                                                                                       |
|------------------|--------|---------------------------------------------------------------------------------------------------|
| Startvalue      | Integer| Specify the start value of the range. Default value is set to 0.                               |
| Endvalue        | Integer| Specify the end value of the range. Default value is set to 0.                                 |
| RangePlacement  | Enum   | Using this attribute, the range can be positioned in two areas along the radial scale. It includes the following options: |
|                  |        |- Inside<br>- Outside<br>The default value is Inside.                                           |

## API Reference (if applicable)

- **Namespace**: `Syncfusion.Windows.Forms.Gauge`
- **Types**:
  - `NeedleStyle`: Enum for setting the needle style.
  - `RangePlacement`: Enum for setting the placement of ranges.

## Code Examples (multi-language supported)

The above examples demonstrate how to customize both the needle properties and the range attributes in a radial gauge using both C# and VB.

## Page-level Navigation/TOC (if applicable)
- 3.2.2.5 Ranges

<!-- tags: [Syncfusion, Winforms, Gauge, NeedleStyle, RangePlacement, RadialGauge] keywords: [Customizing, Needle, Visibility, Ranges, Startvalue, Endvalue, Placement] -->
```

---

<!-- 페이지 23 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: Gauge
page_number: 027
page_id: Gauge#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:52Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

The styles are built in for all of the gauges. Using SkinManager, these four styles can be assigned to the gauge. The following skins are available:

- Blue
- Black
- Silver
- Metro

## Code sample

### C#

```csharp
this.radialGauge1VisualStyle = Syncfusion.Windows.Forms.Gauge.ThemeStyle.Black;
```

### VB

```vb
Me.radialGauge1VisualStyle = Syncfusion.Windows.Forms.Gauge.ThemeStyle.Black
```

## Figure 17: Blue

![](image.png)

<!-- tags: [syncfusion, winforms, gauge, skins, styles, c#, vb] keywords: [blue, black, silver, metro, radialgauge, themestyle, skinmanager, windows forms] -->
```

---

<!-- 페이지 24 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_031.jpeg
document_name: Gauge
page_number: 031
page_id: Gauge#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:15:01Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- Concepts and key features of the Gauge control.
- Installation and deployment instructions.
- Compatibility and prerequisites.

## Content

### Index

#### C
- **Compatibility** 3
- **Concepts and Features** 14
- **Creating a Radial Gauge** 12

#### D
- **Data Binding** 29
- **Deployment Requirements** 9
- **DLL List** 9

#### E
- **Elaborate Structure of the Control** 14

#### G
- **Getting Started** 11

#### I
- **Installation** 5
- **Installation and Deployment** 5
- **Introduction to Gauge for Windows Forms** 3

#### N
- **Needles** 22

#### O
- **Overview** 3

#### P
- **Prerequisites** 3
- **Prerequisites and Compatibility** 3

#### R
- **Radial Gauge** 11
- **Radial Gauge Frame** 14
- **Ranges** 23
- **Real World Scenarios** 11

#### S
- **Samples and Location** 5
- **Samples Installation Location** 5

#### T
- **Ticks** 19

#### V
- **Viewing Samples** 5
- **Visual Styles for all the Gauges** 26

#### Scaling
- **Scales** 17
- **Scaling Divisions** 25

#### Source Code
- **Source Code Location** 8

### Appendix
- **Page-Level Navigation/TOC**: All entries in the index section serve as a localized table of contents for quick navigation.

#### Cross References:
- Refer to specific sections as directed by the index.

#### Code Examples:
- Ensure all code examples (C#) are referenced as shown in the documentation.

### API Reference
- Details are available in the specific pages listed under the index for each feature or component极致实际情况的权利.

```markdown
<!-- tags: [gauge, winforms, control, sdk, documentation] keywords: [syncfusion, radial gauge, data binding, visual styles] -->
```

---

<!-- 페이지 25 -->

```md
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_004.jpeg
document_name: Gauge
page_number: 004
page_id: Gauge#page_004
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:22Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Content

### Compatibility

The following table lists the compatible operating systems for the software:

| Operating Systems | Compatibility |
| --- | --- |
|  | • Windows Server 2008 (32 bit and 64 bit) |
|  | • Windows 7 (32 bit and 64 bit) |
|  | • Windows Vista (32 bit and 64 bit) |
|  | • Windows XP |
|  | • Windows 2003 |

## API Reference (if applicable)

This section would include namespace, class, members (Methods/Properties/Events/Enums), parameters table, returns, and exceptions if relevant.

## Code Examples (multi-language supported)

This section would include examples in C#, VB, XML, XAML, JS, CSS, TS, Python if relevant.

## Page-level Navigation/TOC (if applicable)

This section would include any local Table of Contents for this page.

## Cross References

This section would include notable reference points to other sections or external resources if applicable.

## RAG Annotations

<!-- tags: [gauge, windows-forms, operating-systems, compatibility] keywords: [windows server 2008, windows 7, windows vista, windows xp, windows 2003, 32 bit, 64 bit, essential gauge] -->
```

---

<!-- 페이지 26 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_008.jpeg
document_name: Gauge
page_number: 008
page_id: Gauge#page_008
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:33Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview

- This page introduces the concepts of using the Essential Gauge control in Windows Forms applications.
- Demonstrates the RadialGauge Demo and DataBinding Demo.
- Explains the Source Code Location for the Windows Forms Gauge control.

## Content

### Figure 3: Essential Gauge WF Samples

![Essential Gauge WF Samples](https://example.com/essential-gauge-wf-samples)  

Figure 3 illustrates the Essential Gauge WF Samples, showcasing a RadialGauge Demo and a DataBinding Demo.  

4. Select any sample and browse through the features.

### 2.2.3 Source Code Location

#### Overview
- Provides the default location of the Windows Forms Gauge control source code.

The default location of the Windows Forms Gauge control source code is:

```
C:\Program Files\Syncfusion\Essential Studio\[VersionNumber]\Windows\Gauge.Windows\Src
```

## API Reference

This section provides details on the API related to the Gauge control in Windows Forms.

### WinForms-specific conventions:
- Control names, namespaces, and types are mentioned exactly as shown in the image.

## Code Examples

No specific code examples are provided in this section.

## Page-level Navigation/TOC

None provided in this section.

## Cross References

- See also: [RadialGauge Demo], [DataBinding Demo]

## RAG Annotations
<!-- tags: [Essential Gauge, Windows Forms, RadialGauge Demo, DataBinding Demo, Source Code Location, control, version: 11.4.0.26] keywords: [Gauge, Windows Forms, RadialGauge, DataBinding, Source Code Location, features, version] -->
```

---

<!-- 페이지 27 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_012.jpeg
document_name: Gauge
page_number: 012
page_id: Gauge#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:45Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- The Gauge control is an extension of Windows Forms programming.
- Supports a broad range of dashboard development features.
- Includes resources, controls, graphics, layout, and data binding.

## Content

### 3.2.1.1 Creating a Radial Gauge

Radial gauges can be enhanced with a circle frame or semi-circle frame. This section covers how to include a radial gauge in an application.

#### Through Designer:

1. Drag the RadialGauge control from the toolbox onto the form.

![Figure: RadialGauge control selection](image.png)

#### Steps to Create a Radial Gauge:

- **Step 1:** Open the Windows Forms application in Visual Studio.
- **Step 2:** Navigate to the **Toolbox** panel.
- **Step 3:** Locate and drag the **RadialGauge** control to the form.
- **Step 4:** Customize the properties of the RadialGauge as needed.

## API Reference

### RadialGauge

#### Properties
- **Position:** The position of the gauge on the form.
- **Size:** The dimensions of the gauge.
- **Value:** The current value displayed on the gauge.
- **Range:** The minimum and maximum values the gauge can display.

### Example Usage

```csharp
using Syncfusion.Windows.Forms.Gauge;

// Create a RadialGauge instance
RadialGauge radialGauge = new RadialGauge();

// Set the position and size
radialGauge.Location = new System.Drawing.Point(50, 50);
radialGauge.Size = new System.Drawing.Size(200, 200);

// Set the value
radialGauge.Value = 75;

// Add the gauge to the form
this.Controls.Add(radialGauge);
```

## Code Examples

### Adding a RadialGauge to a Form

```csharp
private void InitializeRadialGauge()
{
    RadialGauge radialGauge = new RadialGauge();
    radialGauge.Location = new System.Drawing.Point(50, 50);
    radialGauge.Size = new System.Drawing.Size(200, 200);
    radialGauge.Value = 75;
    this.Controls.Add(radialGauge);
}
```

## References
- [Syncfusion WinForms Documentation](https://help.syncfusion.com/windowsforms/gauge)
- Additional resources and examples available from the Syncfusion website.

<!-- tags: [radial gauge, windows forms, dashboard development, radial frame, semi-circle frame, designer, control, windows forms programming] keywords: [RadialGauge, Visual Studio, toolbox, position, size, value, range, customization, windows forms, controls, graphics, layout, data binding, example, usage] -->
```

---

<!-- 페이지 28 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_016.jpeg
document_name: Gauge
page_number: 016
page_id: Gauge#page_016
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:03Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Content

### Full Circle Gauge

![Figure 7: Full Circle Gauge](image_link_here)

### Half Circle Gauge

![Figure 8: Half circle gauge](image_link_here)

## Code Sample:

```csharp
this.radialGaugel.FrameType = Syncfusion.Windows.Forms.Gauge.FrameType.HalfCircle;
```

```vb
' [VB]
```

## Footer
© 2013 Syncfusion. All rights reserved.

Page 16
```

<!-- tags: [Gauge, syncfusion-sdk, Windows Forms, full circle gauge, half circle gauge] keywords: [Syncfusion.Windows.Forms.Gauge, FrameType.HalfCircle, C#, VB] -->
```

---

<!-- 페이지 29 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_020.jpeg
document_name: Gauge
page_number: 020
page_id: Gauge#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:12Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

Two types of ticks can be added to the RadialGauge control scale. Major tick marks are the primary scale indicators. Minor tick marks and Inter tick marks are the secondary scale indicators that fall between the major ticks. The ticks can be placed by setting the TickPlacement property. Ticks can be placed inside or outside the arc.

The following table lists the important properties that can be used to customize the radial tick marks. This is done to represent the scale with meaningful markers and labels.

## Property Table

| Property                    | Type         | Description                                                                 |
|-----------------------------|--------------|-----------------------------------------------------------------------------|
| TickPlacement               | Enum         | Gets or sets whether to place the tickmarks inside or outside the arc. |
| MajorTickMarkColor         | Color        | Gets or sets the color of the major tickmarks.                        |
| MajorTickMarkHeight        | Integer      | Gets or sets the height of the major tickmarks.                        |
| MinorTickMarkColor         | Color        | Gets or sets the color of the minor tickmarks.                        |
| MinorTickMarkHeight        | Integer      | Gets or sets the height of the minor tickmarks.                        |
| InterLinesColor            | Color        | Gets or sets the color of the InterLines of the gauge.               |
| MinorInnerLinesHeight      | Integer      | Gets or sets the line height of the minor inner lines.               |

The following code example illustrates how to add major and minor ticks to the radial scale.

```csharp
this.radialGauge1.TickPlacement = Synctfusion.Windows.Forms.Gauge.TickPlacement.Outside;
this.radialGauge1.MajorTickMarkColor = System.Drawing.Color.White;
this.radialGauge1.MinorTickMarkColor = System.Drawing.Color.White;
this.radialGauge1.InterLinesColor = System.Drawing.Color.White;
```

<!-- tags: [product, RadialGauge, TickMark, TickPlacement, MajorTickMark, MinorTickMark, InterLines] keywords: [RadialGauge, tick marks, customizing, scale indicators, placement, tick color, line height] -->
```

---

<!-- 페이지 30 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: Gauge
page_number: 024
page_id: Gauge#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:25Z
fidelity: lossless
-->

## Overview

This page explains the configuration of ranges for a radial gauge using the `Syncfusion.Windows.Forms.Gauge.Range` class. It covers essential properties such as `Height` and `Color` and provides code samples in both C# and VB to demonstrate adding ranges to a radial gauge.

### Key Points

- **Height**: Specifies the height of the range. Default is set to 5.
- **Color**: Gets or sets the color of the range.

## Content

### Properties of Range

| Property   | Type     | Description                                                                                     |
|------------|----------|-------------------------------------------------------------------------------------------------|
| Height     | Integer  | Specify the height of the range. Default value is set to 5.                                  |
| Color      | Color    | Gets or sets the color of the range.                                                             |

### Adding Ranges to a Radial Gauge

The following code sample illustrates how to add ranges to the radial gauge:

#### C#

```csharp
Syncfusion.Windows.Forms.Gauge.Range range1 = new Syncfusion.Windows.Forms.Gauge.Range();

range1.Color = System.Drawing.Color.FromArgb(((int)((byte)(225))),
                                           ((int)((byte)(128))),
                                           ((int)((byte)(128))));
range1.EndValue = 0F;
range1.Height = 5;
range1.InRange = false;
range1.Name = "GaugeRange1";
range1.RangePlacement = Syncfusion.Windows.Forms.Gauge.TickPlacement.Inside;
range1.StartValue = 0F;
this.radialGauge1.Ranges.Add(range1);
```

#### VB

```vb
Dim range1 As New Syncfusion.Windows.Forms.Gauge.Range()
range1.Color = System.Drawing.Color.FromArgb(CInt(CByte(225)),
                                           CInt(CByte(128)),
                                           CInt(CByte(128)))
range1.EndValue = 0F
range1.Height = 5
range1.InRange = False
range1.Name = "GaugeRange1"
range1.RangePlacement = Syncfusion.Windows.Forms.Gauge.TickPlacement.Inside
range1.StartValue = 0F
Me.radialGauge1.Ranges.Add(range1)
```

## Page-level Navigation/TOC (if applicable)

- Overview
  - Key Points
- Content
  - Properties of Range
  - Adding Ranges to a Radial Gauge
  - Code Examples

## Cross References

See also:

- `Syncfusion.Windows.Forms.Gauge.Range`
- `Syncfusion.Windows.Forms.Gauge.TickPlacement`
- `System.Drawing.Color`

<!-- tags: [Syncfusion, Windows Forms, Gauge, Range, TickPlacement, color, height] keywords: [radial gauge, range configuration, C#, VB, Syncfusion.Windows.Forms.Gauge.Range, Syncfusion.Windows.Forms.Gauge.TickPlacement] -->
```

---

<!-- 페이지 31 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: Gauge
page_number: 028
page_id: Gauge#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:41Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Overview
- This page showcases two examples of gauges: one in black and one in silver.
- The gauges display a range of values from 0 to 120, with distinct colored sections indicating different ranges.

## Content

### Black Gauge
**Figure 18: Black**

This figure presents a black-colored gauge with the following features:
- **Range**: The gauge measures values between 0 and 120.
- **Color Coding**:
  - **Green**: The lowest section (approximately 0 to 40).
  - **Yellow**: The middle section (approximately 40 to 90).
  - **Red**: The highest section (approximately 90 to 120).
- **Pointer**: The gauge pointer is white and points to the 40 mark in the green section.

### Silver Gauge
**Figure 19: Silver**

This figure shows a silver-colored gauge with the following characteristics:
- **Range**: The gauge measures values between 0 and 120.
- **Color Coding**:
  - **Green**: The lowest section (approximately 0 to 40).
  - **Yellow**: The middle section (approximately 40 to 90).
  - **Red**: The highest section (approximately 90 to 120).
- **Pointer**: The gauge pointer is white and points to the 0 mark, indicating the baseline value.

## Cross References
- See also:
  - Gauge design principles in "Gauge Concepts."

<!-- tags: [Syncfusion, Winforms, Gauge, Design, Black, Silver] keywords: [Essential Gauge, Windows Forms, Black, Silver, Range, Color Coding, Pointer, Design] -->
```