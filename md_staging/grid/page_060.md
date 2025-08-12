```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_060.jpeg
document_name: grid
page_number: 060
page_id: grid#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:19:50Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates setting the Anchor Property for the Grid Grouping Control.
- Explains how to enable runtime grouping by configuring the ShowGroupDropArea property.

## Content

### Setting the Anchor Property
The following image illustrates setting the Anchor Property for the Grid Grouping Control.

![Figure 23: Setting the Anchor Property](#)

### Enabling Runtime Grouping
18. To allow grouping at run time, the Grid Grouping control displays a drop panel onto which the user can drag columns to be grouped. To display this drop panel, you need to set the `ShowGroupDropArea` property to `true` as shown in the following screenshot.

### Configuration Details
The screenshot shows the following:
- **Grid Grouping Control**: Displays a grid with columns such as Address, City, CompanyName, ContactName, and ContactTitle.
- **Properties Panel**: The Properties panel on the right side of the screenshot displays settings for the Grid Grouping Control, including various Layout and Look and Feel options.
- **Anchoring**: The Anchor property is set to `Top, Left`, ensuring the Grid Grouping Control maintains its position relative to these edges.
- **Runtime Grouping Setup**: The `ShowGroupDropArea` property is mentioned but not directly visible in the screenshot details. This property needs to be set to `true` to enable the drop panel.

## API Reference
### GridGroupingControl
- **Properties**:
  - `ShowGroupDropArea`: Boolean property to enable or disable the group drop area at runtime.
  - `Anchor`: Specifies the edges of the container that the control is anchored to.

## Code Examples
```csharp
// C# Example
using Syncfusion.Windows.Forms.Grid;

gridGroupingControl1.ShowGroupDropArea = true;
gridGroupingControl1.Anchor = AnchorStyles.Top | AnchorStyles.Left;
```

## Page-level Navigation/TOC
- **Setting the Anchor Property**
- **Enabling Runtime Grouping**

## Cross References
See also:
- Other configuration options for Grid Grouping Control.
- Complete API reference for GridGroupingControl properties.

<!-- tags: [Grid Grouping Control, Anchor Property, ShowGroupDropArea, Windows Forms] keywords: [grid, anchor, grouping, runtime, drop panel, Syncfusion Winforms] -->
```