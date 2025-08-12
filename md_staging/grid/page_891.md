```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_891.jpeg
document_name: grid
page_number: 891
page_id: grid#page_891
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:47:53Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of customized groups and child groups in the Grid Grouping Control.
- Focuses on configuring the `TableOptions` settings to customize the appearance and behavior of the grid.
- Highlights how different selection modes and grid appearance properties can be set for enhanced usability.

## Content

### Customized Groups and Child Groups in Grid Grouping Control

#### Main Grid Control

The image shows a `GridGroupingControl` where the data is organized into groups based on wins in football matches. The grid has the following columns: ID, losses, School, Sport, ties, wins, and year.

##### Hierarchical Data Grouping
- The grid is grouped into different categories based on the number of wins:
  - `wins: 0 - 3 Items`
  - `wins: 1 - 2 Items`
  - `wins: 2 - 8 Items`
  - `wins: 3 - 14 Items`
- Each group contains entries with specific details about each football match outcome.

##### Table Options Configuration
The `TableOptions` panel on the right side of the image lists various properties that control the grid's behavior and appearance. Some notable settings include:
- **Selection Modes**: 
  - `ListBoxSelectionMode`: MultiExtended
  - `ListBoxSelectionCurr`: HideCurrentCell
- **Appearance Settings**:
  - `SelectionBackColor`: 255, 128, 128
  - `SelectionTextColor`: Maroon
  - `GridHeaderBorder`: Solid; 208, 215, 229
  - `ShowTableIndent`: True
- **Behavioral Properties**:
  - `AllowDragColumns`: True
  - `AllowDropDownCell`: True
  - `AllowMultiColumnSort`: True
  - `AllowSortColumns`: True
  - `ShowRecordHeader`: False
  - `ShowTableRowHeader`: False

##### Example Entries
Here are some example entries from the grid:
- **School: Duke**
  - ID: 139, losses: 11, wins: 0, year: 2001
  - ID: 140, losses: 11, wins: 0, year: 2000
  - ID: 144, losses: 11, wins: 0, year: 1996
- **School: Georgia Tech**
  - ID: 168, losses: 10, wins: 1, year: 1994
- **School: North Carolina**
  - ID: 16, losses: 8, wins: 2, year: 2003
- **School: Wake Forest**
  - ID: 222, losses: 10, wins: 1, year: 1995
  - ID: 217, losses: 9, wins: 2, year: 2000
  - ID: 224, losses: 9, wins: 2, year: 1993

##### Notes on the Grid Design
- The grid is designed to handle hierarchical data effectively, allowing users to expand and collapse groups for better navigation.
- Different selection modes and appearance settings ensure a customized user experience for sorting, filtering, and interacting with the data.

#### Figure: Customized Groups and Child Groups of Grid Grouping Control
![Figure 352: Customized Groups and Child Groups of Grid Grouping Control](#)
The figure shows the extended functionality of grouping and collapsing data in a structured manner using `GridGroupingControl`.

### Additional Resources
**Note:** For more details, refer to the following browser sample:
```plaintext
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Grouping Grid Options\Table Options Demo
```

## API Reference
- **Class:** `Syncfusion.Windows.Forms.Grid.Grouping.GridTableOptions`
- **Properties:**
  - `AllowDragColumns`: Boolean
  - `AllowSortColumns`: Boolean
  - `CaptionRowHeight`: Integer
  - `ColumnHeaderRowHeight`: Integer
  - `GridHeaderBorder`: GridBorder
  - `SelectionBackColor`: Color
  - `SelectionTextColor`: Color
  - `ShowTableIndent`: Boolean

## Code Examples

### C#
```csharp
using Syncfusion.Windows.Forms.Grid.Grouping;

// Example of configuring TableOptions
GridTableOptions tableOptions = gridGroupingControl1.TableModel.Options;
tableOptions.AllowDragColumns = true;
tableOptions.AllowSortColumns = true;
tableOptions.CaptionRowHeight = 20;
tableOptions.ColumnHeaderRowHeight = 22;
tableOptions.SelectionBackColor = Color.FromArgb(255, 128, 128);
tableOptions.SelectionTextColor = Color.Maroon;
tableOptions.ListBoxSelectionMode = SelectionMode.MultiExtended;
tableOptions.ListBoxSelectionCurrent = HideCurrentCell.HideCurrentCell;
tableOptions.ShowTableIndent = true;
```

## Page-level Navigation/TOC
- Figure 352: Customized Groups and Child Groups of Grid Grouping Control
- Table Options Configuration
- Example Grid Entries

## Cross References
- **See also:** Grid.Grouping.Windows Samples for additional demonstrations and usage scenarios.

<!-- tags: grid, gridgroupingcontrol, tableoptions, grouping, selectionmode, userinterface, syncfusion, winforms keywords: gridgroupingcontrol, tableoptions, groupinggrid, customgroups, selectionmodes, hierarchicaldata, griddesign -->
```
