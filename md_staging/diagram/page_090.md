```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_090.jpeg
document_name: diagram
page_number: 090
page_id: diagram#page_090
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:07Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Describes the `ViewPortBoundsChanging Event` and its occurrence.
- Explains how properties can be set programmatically in a `Windows Forms` application.

## Content

### Event Explanation

| Event Name | Description |
|------------|-------------|
| ViewPortBoundsChanging Event | Occurs when the controls viewport bounds is changed. |

### Programmatic Property Settings

Properties can be set programmatically as follows:

#### C#

```csharp
overviewControl1.BackColor = System.Drawing.SystemColors.AppWorkspace;
overviewControl1.Diagram = diagram1;
overviewControl1.Dock = System.Windows.Forms.DockStyle.Bottom;
overviewControl1.ForeColor = System.Drawing.Color.Red;
overviewControl1.Location = new System.Drawing.Point(0, 377);
overviewControl1.Name = "overviewControl";
overviewControl1.Size = new System.Drawing.Size(200, 100);
overviewControl1.TabIndex = 1;
```

#### VB

```vb
overviewControl1.BackColor = System.Drawing.SystemColors.AppWorkspace
overviewControl1.Diagram = diagram1
overviewControl1.Dock = System.Windows.Forms.DockStyle.Bottom
overviewControl1.ForeColor = System.Drawing.Color.Red
overviewControl1.Location = New System.Drawing.Point(0, 377)
overviewControl1.Name = "overviewControl"
overviewControl1.Size = New System.Drawing.Size(200, 100)
overviewControl1.TabIndex = 1
```

## API Reference

- **Namespace**: `System.Windows.Forms`
- **Types**: `Control`, `Diagram` (for `Diagram1`), `DockStyle`, `Size`, `Point`

## Code Examples

The above sections provide examples in both C# and VB for setting properties programmatically.

<!-- tags: [syncfusion, winforms, diagram, event, property, tutorial] keywords: [ViewPortBoundsChanging, Diagram, DockStyle, System.Drawing, AppWorkspace, Red, Location, Size, TabIndex] -->
```