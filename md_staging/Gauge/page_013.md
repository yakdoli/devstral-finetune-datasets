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
