```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_105.jpeg
document_name: edit
page_number: 105
page_id: edit#page_105
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:40Z
fidelity: lossless
-->

## Overview
- Describes how to enable and manage automatic outlining in a VB.NET environment.
- Lists VB.NET code snippets to collapse, expand, and toggle outlining functionality.

## Content

### Essential Edit for Windows Forms

```vb.net
' Enabling Automatic Outlining.
Me.editControl1.ShowOutliningCollapsers = True

' Collapses all regions in currently selected area or in the current line.
Me.editControl1.Collapse()

' Expands all collapsed regions in currently selected area or in the current line.
Me.editControl1.Expand()

' Turns on collapse and collapse all option.
Me.editControl1.SwitchCollapsingOff()

' Turns off collapse option.
Me.editControl1.SwitchCollapsingOn()

' Collapses all regions.
Me.editControl1.CollapseAll()

' Expands all collapsed regions.
Me.editControl1.ExpandAll()

' Toggles collapse option for current line.
Me.editControl1.ToggleLineCollapsing()
```

### Outlining Operations

The `Edit Control` supports the following events to handle the various Outlining operations.

| Edit Control Event         | Description                                          |
|---------------------------|------------------------------------------------------|
| OutliningBeforeCollapse   | Occurs before the region is about to collapse.       |
| OutliningBeforeExpand     | Occurs before the region is about to expand.         |
| OutliningCollapse         | Occurs when the region collapses.                    |
| OutliningExpand           | Occurs when the region expands.                      |
| CollapsedAll             | Occurs when `CollapseAll` method was called.         |
| ExpandedAll              | Occurs when `ExpandedAll` method was called.         |

## Page-level Navigation/TOC (if applicable)
- **[No visible TOC or navigation in the captured image.]**

## Cross References
- **[No visible cross-references in the current context.]**

## RAG Annotations
<!-- tags: [windows-forms, edit-control, outlining] keywords: [automatic outlining, collapse, expand, collapseall, expandall, outlining events, syncfusion winforms, version 11.4.0.26] -->
```