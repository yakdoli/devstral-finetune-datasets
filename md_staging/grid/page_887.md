```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_887.jpeg
document_name: grid
page_number: 887
page_id: grid#page_887
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:47:19Z
fidelity: lossless
-->

## Overview
- Explores the configuration of the `gridGroupingControl1` control using various properties.
- Focuses on customizing the `TableOptions` settings for enhanced grid functionality.
- Includes control over drag-and-drop, sorting, and visual elements like grid lines and selection colors.

## Content

### Control Configuration in TableOptions

The following section lists the properties and their values set in the `TableOptions` for the `gridGroupingControl1` control:

```plaintext
| Property                  | Value                                    |
|---------------------------|------------------------------------------|
| AllowDragColumns          | True                                     |
| AllowDropDownCell         | True                                     |
| AllowMultiColumnSort       | True                                     |
| AllowSelection            | None                                     |
| AllowSortColumns          | True                                     |
| CaptionRowHeight          | 22                                      |
| ColumnHeaderRowHeight     | 22                                      |
| ColumnsMaxlengthFirstNRecord| 100                                     |
| ColumnsMaxlengthStrategy   | MaxLengthSummary                         |
| DefaultColumnWidth         | 60                                      |
| DrawTextWithGdiInterop    | False                                    |
| GridLineBorder            | Standard                                 |
| GroupFooterSectionHeight   | 10                                      |
| GroupHeaderSectionHeight   | 10                                      |
| GroupPreviewSectionHeight  | 36                                      |
| IndentWidth               | 18                                      |
| ListBoxSelectionColorOptions| ApplySelectionColor                      |
| ListBoxSelectionCurrentCellOpt| WhiteCurrentCell                       |
| ListBoxSelectionMode       | None                                     |
| ListBoxSelectionOutlineBorder| NotSet                                 |
| ListBoxSelectionRecursive  | False                                    |
| MaxDropDownTableSize      | 640, 280                                |
| MaxFilterBarChoiceListSize| 640, 160                                |
| RecordPreviewRowHeight     | 36                                      |
| RecordRowHeight           | 18                                      |
| RowHeaderWidth            | 18                                      |
| SelectionBackColor         | Highlight                                |
| SelectionTextColor         | HighlightText                            |
| ShowRecordPlusMinus       | True                                     |
| ShowRecordPreviewRow      | False                                    |
| ShowRowHeader             | True                                     |
| ShowTableIndent           | True                                     |
| ShowTableIndentAsCoveredRow| False                                   |
| ShowTableRowHeaderAsCovere| False                                   |
| ShowTreeLines             | False                                    |
| SummaryRowHeight          | -1                                      |
| TreeLineBorder            | Solid; ControlDarkDark; Thin             |
| VerticalPixelScroll       | True                                     |
| WeakReferenceChangedListene| (Collection)                            |
```

### Detailed Explanation of Key Properties

- **AllowDragColumns**: Enables dragging and rearranging of grid columns.
- **AllowDropDownCell**: Permits dropdown functionality within grid cells.
- **AllowSelection**: Configures selection behavior, currently disabled.
- **DefaultColumnWidth**: Sets the initial width of all grid columns.
- **GridLineBorder**: Defines the border style for grid lines, currently set to `Standard`.
- **SelectionBackColor** and **SelectionTextColor**: Define the color of the selected rows, highlighting text for better visibility.
- **TreeLineBorder**: Specifies the appearance of hierarchical tree lines when expanded.

### Visual Customization

- The `TableOptions` allows fine-tuning of the grid’s appearance and behavior, such as row and column heights, grid lines, and selection colors.
- Dropdown sizes and filter settings can be customized to fit the specific needs of the application.

## API Reference

### Members Configured

#### Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl

- **Properties:**
  - `AllowDragColumns`
  - `AllowDropDownCell`
  - `AllowMultiColumnSort`
  - `AllowSelection`
  - `AllowSortColumns`
  - `CaptionRowHeight`
  - `ColumnHeaderRowHeight`
  - `ColumnsMaxlengthFirstNRecord`
  - `ColumnsMaxlengthStrategy`
  - `DefaultColumnWidth`
  - `DrawTextWithGdiInterop`
  - `GridLineBorder`
  - `GroupFooterSectionHeight`
  - `GroupHeaderSectionHeight`
  - `GroupPreviewSectionHeight`
  - `IndentWidth`
  - `ListBoxSelectionColorOptions`
  - `ListBoxSelectionCurrentCellOpt`
  - `ListBoxSelectionMode`
  - `ListBoxSelectionOutlineBorder`
  - `ListBoxSelectionRecursive`
  - `MaxDropDownTableSize`
  - `MaxFilterBarChoiceListSize`
  - `RecordPreviewRowHeight`
  - `RecordRowHeight`
  - `RowHeaderWidth`
  - `SelectionBackColor`
  - `SelectionTextColor`
  - `ShowRecordPlusMinus`
  - `ShowRecordPreviewRow`
  - `ShowRowHeader`
  - `ShowTableIndent`
  - `ShowTableIndentAsCoveredRow`
  - `ShowTableRowHeaderAsCovere`
  - `ShowTreeLines`
  - `SummaryRowHeight`
  - `TreeLineBorder`
  - `VerticalPixelScroll`
  - `WeakReferenceChangedListene`

## Code Examples

### Example: Initializing TableOptions

Here’s how to configure the `TableOptions` programmatically in C#:

```csharp
gridGroupingControl1.TableOptions.AllowDragColumns = true;
gridGroupingControl1.TableOptions.AllowDropDownCell = true;
gridGroupingControl1.TableOptions.AllowSelection = GridDataControlSelectionFlags.None;
gridGroupingControl1.TableOptions.DefaultColumnWidth = 60;
gridGroupingControl1.TableOptions.IndentWidth = 18;
gridGroupingControl1.TableOptions.SelectionBackColor = Color.LightBlue;
gridGroupingControl1.TableOptions.SelectionTextColor = Color.Black;
gridGroupingControl1.TableOptions.ShowRecordPreviewRow = false;
```

### Example: Customizing GridLineBorder

This snippet modifies the grid line border for a more visible appearance:

```csharp
gridGroupingControl1.TableOptions.GridLineBorder = BorderStyle.Solid;
gridGroupingControl1.TableOptions.TreeLineBorder = BorderStyle.Solid;
```

## Page-level Navigation/TOC
- **Overview**: Summarizes the purpose and scope of the page.
- **Content**: Lists and explains the properties configured in `TableOptions`.
- **API Reference**: Details the properties and their configurable values.
- **Code Examples**: Provides sample code for programmatically configuring the `gridGroupingControl1`.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, gridGroupingControl1, TableOptions, customization, properties] keywords: [AllowDragColumns, AllowDropDownCell, AllowSelection, DefaultColumnWidth, GridLineBorder, SelectionBackColor, SelectionTextColor, ShowTreeLines] -->
```