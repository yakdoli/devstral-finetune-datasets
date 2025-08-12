```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_104.jpeg
document_name: edit
page_number: 104
page_id: edit#page_104
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:03Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Describes how to enable Automatic Outlining by setting the `ShowOutliningCollapsers` property to `True`.
- Lists the Edit APIs provided to support Outlining functionality.

## Content

### Outlining APIs

The following table describes the Edit Control methods that support Outlining:

| Edit Control Method         | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| Collapse                    | Collapses all regions in the currently selected area or in the current line. |
| Expand                      | Expands all collapsed regions in the currently selected area or in the current line. |
| SwitchCollapsingOn          | Turns on the collapse and collapse all option.                                |
| SwitchCollapsingOff         | Turns off the collapse option.                                              |
| CollapseAll                 | Collapses all regions.                                                      |
| ExpandAll                   | Expands all collapsed regions.                                              |
| ToggleLineCollapsing       | Toggles the collapse option for the current line.                          |

### Example Code: Enabling Automatic Outlining

The following C# code snippet demonstrates how to use the mentioned APIs to manage outliners:

```csharp
// Enabling Automatic Outlining.
this.editControl.ShowOutliningCollapsers = true;

// Collapses all regions in the currently selected area or in the current line.
this.editControl.Collapse();

// Expands all collapsed regions in the currently selected area or in the current line.
this.editControl.Expand();

// Turns on the collapse and collapse all option.
this.editControl.SwitchCollapsingOff();

// Turns off the collapse option.
this.editControl.SwitchCollapsingOn();

// Collapses all regions.
this.editControl.CollapseAll();

// Expands all collapsed regions.
this.editControl.ExpandAll();

// Toggles the collapse option for the current line.
this.editControl.ToggleLineCollapsing();
```

<!-- tags: [product, module, control, api, version] keywords: [WinForms, Edit, Outlining, ShowOutliningCollapsers, Collapse, Expand, SwitchCollapsingOn, SwitchCollapsingOff, CollapseAll, ExpandAll, ToggleLineCollapsing] -->
```