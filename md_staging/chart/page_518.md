```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_518.jpeg
document_name: chart
page_number: 518
page_id: chart#page_518
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:49:01Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the use of "Skins" in charts to customize the visual appearance.
- Illustrates the difference in chart styles when the "Skins" value is set to different themes: Office2007 Silver and Almond.
- Includes examples of series plots with skin customization options.

## Content

### Office2007 Silver Skin
The chart below utilizes the Office2007 Silver theme.

#### Figure 334: Office2007 Silver

- **Chart Title**: Chart with Skins
- **Series**: Displays data points along a linear scale.
- **Skins Value**: Set to Office2007 Silver.

### Almond Skin
The following output is displayed when the Skins value is set to Almond.

#### Figure 335: Almond

- **Chart Title**: Chart with Skins
- **Series**: Represents data points using purple-colored markers.
- **Skins Value**: Set to Almond.

## Code Examples

The examples showcase the interaction of skins with chart customization. Below is a sample code snippet for modifying the chart's skin.

```csharp
// Example of setting the Skin property to Almond
chart.Chart.Skins.ApplicationName = "Almond";
```

## API Reference

### Namespace: Syncfusion.Windows.Forms.Chart
#### Properties
- **Skins.ApplicationName**: Allows user to set the skin name for the chart.
  - **Type**: String
  - **Default**: Generic skin

### Methods
- **ApplySkin()**: Applies the selected skin to the chart.
  - **Parameters**: None
  - **Returns**: void
  - **Description**: Dynamically updates the chart's visual appearance based on the selected skin.

## Page-level Navigation/TOC (if applicable)

See also:
- Further details on chart customization options.
- Extensive examples of various skin themes.

<!-- tags: chart, skins, customization, windows forms, Syncfusion Winforms, Office2007 Silver, Almond keywords: skins, chart customization, visual themes, Windows Forms, Syncfusion -->
```