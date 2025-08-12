```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_721.jpeg
document_name: grid
page_number: 721
page_id: grid#page_721
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:58Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Discusses the key properties and functionalities associated with the Essential Grid for Windows Forms.
- Focuses on group elements, detailing properties for managing headers, footers, and summaries.
- Explores the manipulation of group elements using various properties.

## Content

### Section: Properties and Their Functionality

| Property Name                    | Description                                                                                                                                                          |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ShowGroupPreview                 | Indicates whether a preview is visible when the group is collapsed.                                                                                                   |
| ShowSummaries                    | Indicates whether summaries are visible.                                                                                                                             |
| ShowGroupSummaryWhenCollapsed    | Indicates whether summary items are visible when the group is collapsed.                                                                                            |
| ShowFilterBar                    | Indicates whether a filter bar is visible.                                                                                                                           |
| ShowStackedHeaders               | Indicates whether the stacked headers are visible.                                                                                                                  |
| ShowGroupIndentAsCoveredRange    | Indicates whether to treat all the indent cells for a group as a single covered cell.                                                                                |
| ShowCaptionSummaryCells          | Indicates whether a group caption should display summaries in columns instead of only one large caption bar.                                                        |

#### Next Chapter
> Discusses these properties in detail with a suitable example.

#### 4.3.4.3.1.2.1 Working with Group Elements

This section explores the various properties that can be used to manipulate the different group elements.

### Group Headers and Footers

The headers and footers of a group can be used to display any information that is common to all the elements of that group. You can toggle the display of these headers and footers by using the below given boolean properties.

- ```csharp
<GroupOptions>.ShowGroupHeader
```

- ```csharp
<GroupOptions>.ShowGroupFooter
```

Where the `<GroupOptions>` can be any one of the following:
- `TopLevelGroupOptions` to affect only the top most group.
- `ChildGroupOptions` to affect the child groups.
- `NestedTableGroupOptions` to affect the groups in nested tables.

You can also set the header / footer attributes such as `HeaderSectionHeight` and `FooterSectionHeight` by using the below given properties.

## API Reference

### Properties

- **ShowGroupPreview**
  - Type: Boolean
  - Description: Indicates whether a preview is visible when the group is collapsed.

- **ShowSummaries**
  - Type: Boolean
  - Description: Indicates whether summaries are visible.

- **ShowGroupSummaryWhenCollapsed**
  - Type: Boolean
  - Description: Indicates whether summary items are visible when the group is collapsed.

- **ShowFilterBar**
  - Type: Boolean
  - Description: Indicates whether a filter bar is visible.

- **ShowStackedHeaders**
  - Type: Boolean
  - Description: Indicates whether the stacked headers are visible.

- **ShowGroupIndentAsCoveredRange**
  - Type: Boolean
  - Description: Indicates whether to treat all the indent cells for a group as a single covered cell.

- **ShowCaptionSummaryCells**
  - Type: Boolean
  - Description: Indicates whether a group caption should display summaries in columns instead of only one large caption bar.

## Code Example

This section illustrates the usage of some of these properties in a C# code snippet:

```csharp
var grid = new GridControl();
var groupOptions = grid.GroupOptions;

// Example: Showing group header
groupOptions.ShowGroupHeader = true;

// Example: Displaying group summaries when collapsed
groupOptions.ShowGroupSummaryWhenCollapsed = true;

// Example: Toggling stacked headers visibility
groupOptions.ShowStackedHeaders = false;

// Example: Adjusting header size
groupOptions.HeaderSectionHeight = 50;

// Example: Adjusting footer size
groupOptions.FooterSectionHeight = 30;
```

## Conclusion

This section provides a detailed explanation of the properties related to group elements in the Essential Grid for Windows Forms. It covers how to toggle the visibility of various components such as headers, footers, previews, summaries, and summaries when the group is collapsed, providing flexibility in customizing the user interface.

## Cross References
- Refer to the next chapter for detailed examples.

<!-- tags: [windows forms, grid control, properties, group elements, summaries, headers, footers, nested tables ] keywords: [ShowGroupPreview, ShowSummaries, ShowGroupSummaryWhenCollapsed, ShowFilterBar, ShowStackedHeaders, ShowGroupIndentAsCoveredRange, ShowCaptionSummaryCells, ToggleHeadersFooters, HeaderSectionHeight, FooterSectionHeight] -->
```