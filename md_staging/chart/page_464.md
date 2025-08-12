```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_464.jpeg
document_name: chart
page_number: 464
page_id: chart#page_464
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:43:33Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## 4.9.2 Toolbars

### Overview

- Built-in Toolbar included with Essential Charts for Windows Forms
- Enabled during runtime using the ChartControl's ShowToolbar property
- Provides multiple commands for managing charts visually and programmatically

## Content

### Essential Chart Toolbar

Essential Charts comes with a built-in Toolbar that can be made visible to enable the user to do the following during runtime:

- Save the chart as an image.
- Copy the image to clipboard.
- Print the chart.
- Print Preview of the Chart.
- Change the color palette of the chart.
- Affects the style of the chart.
- Change the Chart Type.
- Toggle 3D style of the Chart.
- Toggle Legend Appearance.

The toolbar can be made visible through the ChartControl's **ShowToolbar** property.

#### Toolbar Appearance

The toolbar looks like the below image.

![Built-In Chart Toolbar](https://i.imgur.com/image.png)

**Figure 296: Built-In Chart Toolbar**

#### Toolbar Commands and Functionalities

The toolbar commands and their functionalities are described below.

| Chart toolbar Commands                          | Chart toolbar Items name        | Description                                                                 |
|-------------------------------------------------|----------------------------------|-----------------------------------------------------------------------------|
| Save                                            | Save                             | Saves the chart as an image file.                                          |
| Copy                                            | Copy                             | Copies the image of the chart to the clipboard.                            |
| Print                                           | Print                            | Prints the chart using the selected printer.                                |
| Print Preview                                   | Print Preview                   | Displays a preview of the chart before printing.                           |
| Palette                                         | Palette                          | Allows changing the color palette of the chart.                           |
| Styles                                          | Styles                           | Affects the visual style of the chart.                                    |
| Chart Types                                     | Chart Types                      | Changes the type of the chart (e.g., bar, line, pie).                     |
| 3D Style                                        | 3D Style                         | Toggles the 3D perspective of the chart.                                   |
| Legend Appearance                               | Legend Appearance                | Controls the visibility and appearance of the chart's legend.            |

## API Reference

### ChartControl Properties

- **ShowToolbar**  
  **Type:** Boolean  
  Specifies whether the built-in toolbar is visible for the chart.  
  **Default:** `false`

---

### Code Example

```csharp
// Enable the toolbar for the ChartControl
chartControl1.ShowToolbar = true;
```

## Page-level Navigation/TOC (if applicable)
- 4.9.2 Toolbars
  - Overview
  - Content
    - Essential Chart Toolbar
    - Toolbar Appearance
    - Toolbar Commands and Functionalities

## Cross References
See also:
- Chapter 4: Customizing Chart Appearance
- Section 4.9: Interactivity

<!-- tags: [essentialchart, windowsforms, toolbar, builtintoolbar, chartcontrol, syncingfusion, 11.4.0.26] keywords: [toolbar, chart, windows forms, essential charts, interactivity, print, style] -->
```