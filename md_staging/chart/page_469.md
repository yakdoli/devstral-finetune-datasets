```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_469.jpeg
document_name: chart
page_number: 469
page_id: chart#page_469
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:43:42Z
fidelity: lossless
-->

## Overview

1. Describes the various properties related to the toolbar for Windows Forms Chart.
2. Explains how to set styles for the chart using the toolbar.
3. Details the appearance settings accessible through the Chart Series Style dialog box.

## Content

### Properties of the Toolbar

| Property      | Description                                                                                                                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DockingFree   | Indicates if the toolbar is to be held docked. Default value is `false`.                                                                                                                                                  |
| Header       | Gets / sets the height of the header. Default value is `0`.                                                                                                                                                               |
| Location     | Gets / sets the location of the toolbar.                                                                                                                                                                                  |
| Orientation   | Gets / sets the orientation of the toolbar. Default value is **Horizontal**.                                                                                                                                           |
| Position     | Gets / sets the docking position of the toolbar. Default value is `ChartDock.Top`.                                                                                                                                      |
| ShowBorder   | Indicates if the border of the toolbar should be shown. Default value is `true`.                                                                                                                                        |
| Size         | Gets / sets the size of the toolbar button. Will be used only when the `Autosize` property is set to `false`.                                                                                                           |
| Spacing      | Gets or sets the spacing. Default value is `4`.                                                                                                                                                                         |

### Appearance

#### Setting Styles for the Chart through the Toolbar

**Subheading:** Setting Styles for the Chart through the Toolbar

To set styles for the chart using the toolbar, follow these steps:

1. Click the **Styles** icon in the toolbar to open the **Chart Series Style** dialog box.
2. The following settings are available in this dialog box:

   - **Interior color**: The interior color for the series can be set using the options available in the **Interior** tab.
   - **Border properties**: Border properties can be customized using the **Border** tab.
   - **Text for the series**: Text for the series can be enabled and customized using the **Text** tab.
   - **Shadow for the series**: Shadow for the series can be enabled and customized using the **Shadow** tab.
   - **Series symbols**: Series can hold customized symbols using the **Symbol** tab.
   - **FancyToolTip**: FancyToolTip can be enabled using the options available in the **Fancy ToolTip** tab.

An example image demonstrates how to set the interior properties through the "Interior" tab in the Chart Series Style Window. This can be invoked by clicking the "Styles" command.

---

### API Reference (if applicable)

No specific API reference is provided for the toolbar properties on this page.

### Code Examples (if any)

No code examples are provided on this page.

## Page-level Navigation/TOC (if applicable)

- DockingFree Property
- Header Property
- Location Property
- Orientation Property
- Position Property
- ShowBorder Property
- Size Property
- Spacing Property
- Appearance
  - Setting Styles for the Chart through the Toolbar

## Cross References

See also:
- Chart Series Style dialog box
- Toolbar in Windows Forms Chart

---

### End Page Content

<!-- tags: [chart, toolbar, winforms, appearance] keywords: [DockingFree, Header, Orientation, Position] -->
```