```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_239.jpeg
document_name: grid
page_number: 239
page_id: grid#page_239
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:04:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains the search and replace actions in the Essential Grid control.
- Describes how to perform independent or simultaneous search and replace operations.
- Details the use of the Find Next/Replace buttons for individual or whole worksheet searches.
- Highlights the ability to perform all search results through Find All/Replace All buttons.
- Outlines various search options like case matching, whole cell matching, and search direction.
- Demonstrates enabling the Find and Replace feature in Essential Grid using code examples in C# and VB.NET.

## Content

### The search and replace actions:
- Can be performed independently or simultaneously.
- Can be done for individual search or for the entire worksheet by using the Find Next/Replace buttons.
- Can be done for all the search results by clicking Find All/Replace All buttons.

### Search Options
The search options are as follows:

- Match Case - Matches case while performing search.
- Match Whole Cell - Matches the search text with the entire text in a grid cell.
- Search Up - Specifies if the search can be performed bottom-up.
  - Column Only - Searches only the current column.
  - Selection Only - Searches only the current selection.
  - Whole Table - Searches the whole table.

The Find and Replace feature can be enabled for Essential Grid by using the following code:

#### Using C#

```csharp
GridFindTextOptions options = GridFindTextOptions.WholeTable | GridFindTextOptions.SearchUp;
object locInfo = GridRangeInfo.Table();
GridFindReplaceEventArgs frEvents = new GridFindReplaceEventArgs(cmbSearch.Text, "", options, locInfo);
GridFindReplaceDialogSink frDialog.Find(frEvents);
```

#### Using VB.NET

```vb
Private options As GridFindTextOptions = GridFindTextOptions.WholeTable Or GridFindTextOptions.SearchUp

Private locInfo As Object = GridRangeInfo.Table()
Private frEvents As New GridFindReplaceEventArgs(cmbSearch.Text, "", options, locInfo)
GridFindReplaceDialogSink(frDialog.Find(frEvents))
```

## API Reference

### Methods

- `GridFindTextOptions`: A member used to specify the search options.
- `GridRangeInfo`: Specifies the range of cells to search within.
- `GridFindReplaceEventArgs`: Represents the arguments passed for find and replace operations.
- `GridFindReplaceDialogSink`: A member used to perform the find operation.

### Parameters

- `cmbSearch.Text`: The text to search for.
- `options`: The search options to use.
- `locInfo`: Information indicating where to search.

### Returns

- None. This method performs the search and replace action itself.

## Code Examples

### C# Example
The example demonstrates enabling the Find and Replace feature in an Essential Grid control, specifying search options and performing the operation.

### VB.NET Example
The VB.NET example shows how to enable the Find and Replace feature in an Essential Grid control, specifying the same options as in the C# example.

### Common Queries

- **How do I perform a case-sensitive search in an Essential Grid?**
  Use the `Match Case` option within the code to enable a case-sensitive search.

- **Can I replace text in only a specific column of the grid?**
  Yes, use the `Column Only` option in the search locInfo to restrict the search to a specific column.

<!-- tags: Essential Grid, Windows Forms, Search, Replace, GridFindTextOptions, GridRangeInfo, GridFindReplaceEventArgs, GridFindReplaceDialogSink, C#, VB.NET keywords: search and replace, Essential Grid, Windows Forms, case-sensitive search, column-specific search, whole table search -->
```