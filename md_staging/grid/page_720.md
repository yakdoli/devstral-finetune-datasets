```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_720.jpeg
document_name: grid
page_number: 720
page_id: grid#page_720
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:36:08Z
fidelity: lossless
-->

## Overview
- The `GridGroupOptionsStyleInfo` class defines properties to control the look and feel of groups in a grouping grid.
- It distinguishes between three types of group options: TopLevelGroupOptions, ChildGroupOptions, and NestedTableGroupOptions.
- The document lists properties available for all kinds of Group Options to configure the group behavior.

## Content

### Group Options in GridGroupOptionsStyleInfo

The `GridGroupOptionsStyleInfo` class, which derives from `StyleInfoBase`, defines the properties to control the look and feel of the groups. A grouping grid distinguishes between three different kinds of group options, which are listed below.

| Group Option              | Description                                                                                   |
|---------------------------|-----------------------------------------------------------------------------------------------|
| TopLevelGroupOptions      | Lets you control the look & behavior of top-level group.                                    |
| ChildGroupOptions         | Lets you control the look & behavior of child groups.                                       |
| NestedTableGroupOptions   | Lets you control the look & behavior of groups in nested child relations.                    |

### Properties for the Group Options

The table below describes the properties defined in the `GridGroupOptionsStyleInfo` class. These properties are available for all kinds of Group Options.

| Group Option               | Description                                                                                           |
|----------------------------|-------------------------------------------------------------------------------------------------------|
| CaptionText                | Lets you control the caption text that is displayed.                                                |
| ShowCaption                | Indicates whether a caption row is visible.                                                          |
| ShowCaptionPlusMinus       | Indicates whether a plus/minus cell is to be displayed next to the caption.                       |
| ShowAddNewBeforeDetails    | When true, AddNew record is shown at the top of a group.                                           |
| ShowAddNewAfterDetails     | When true, AddNew record is shown at the bottom of a group.                                        |
| ShowColumnHeaders          | Indicates whether the column headers are visible.                                                   |
| ShowEmptyGroups            | Indicates whether a preview is visible when the group is collapsed.                               |
| ShowGroupHeader            | Indicates whether a header is visible.                                                              |
| ShowGroupFooter            | Indicates whether a footer is visible.                                                              |

---

### RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [GridGroupOptionsStyleInfo, StyleInfoBase, TopLevelGroupOptions, ChildGroupOptions, NestedTableGroupOptions, CaptionText, ShowCaption, ShowCaptionPlusMinus, ShowAddNewBeforeDetails, ShowAddNewAfterDetails, ShowColumnHeaders, ShowEmptyGroups, ShowGroupHeader, ShowGroupFooter, Winforms, Syncfusion, Grid] -->
```