```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_615.jpeg
document_name: chart
page_number: 615
page_id: chart#page_615
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:27Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Demonstrates how to localize static elements of a chart using resource files.
- Explains the process of specifying equivalent terms for all static elements in the chart.
- Shows how to set the culture using the `Localize` property in both C# and VB.

## Content

The following table illustrates the default English resource file for chart localization, with key terminology such as "AllowAlignment," "EnableXZooming," and others listed.

### Resource Table

| Name                 | Value             | Comment    |
|----------------------|-------------------|------------|
| AllowAlignment       | Allow Alignment   |            |
| Area                 | Area              |            |
| AutoHighlight        | Auto Highlight    |            |
| ChartNullException   | Chart             |            |
| EditPalette          | Edit palette...   |            |
| EditStyle            | Edit style...     |            |
| EnableXZooming       | Enable X Zooming  |            |
| EnableYZooming       | Enable Y Zooming  |            |
| Mode                 | Modes             |            |
| Palettes             | Palettes          |            |
| Real3D               | Real 3D           |            |
| ResetZoom            | Reset Zoom        |            |
| Series               | Series            |            |
| ThreeD               | 3D                |            |
| TwoD                 | 2D                |            |
| Types                | Types             |            |

### Note

It is mandatory to specify equivalent terms for all static elements to localize the chart.

#### Setting the Culture

Specify the culture using the `Localize` property as given in the following code:

```csharp
this.chartControl1.Localize="de-DE";
```

```vb
Me.chartControl1.Localize="de-DE"
```

## API Reference

### Properties

- **Localize**
  - **Description**: Specifies the culture for localizing the chart.
  - **Type**: String
  - **Example Values**: `"de-DE"`, `"fr-FR"`

## Code Examples

The following examples demonstrate how to set the culture for the chart control in C# and VB.

### C# Example

```csharp
this.chartControl1.Localize = "de-DE";
```

### VB Example

```vb
Me.chartControl1.Localize = "de-DE"
```

## RAG Annotations

<!-- tags: [Syncfusion Windows Forms, Chart, Localization, Resource Files, Static Elements, Culture, Localize Property] keywords: [chart localization, resource file, static element, culture specification, localize, de-DE, fr-FR, C#, VB] -->
```