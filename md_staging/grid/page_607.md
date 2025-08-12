```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_607.jpeg
document_name: grid
page_number: 607
page_id: grid#page_607
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:27:42Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section focuses on the design-time support provided by the Grid Grouping Control in Syncfusion WinForms.

## Content

### Grid Grouping Control Design Time Support

#### Figure 256: Design Time Support in the Grid Grouping Control
- **Appearance**: The grid provides design time and run time options to customize the appearance of its elements. The appearance settings include various options such as background color, font, text color, alignment, and so on.

#### Grid Grouping Control Example

**Grid Design Overview:**
The Grid Grouping Control allows for hierarchical data representation and provides the ability to group data by specific fields. The following grid shows a sample dataset grouped by "Sport" and "wins," with nested groups representing various conditions.

**Grid Control Settings:**
- **VerticalScrollTips**: False
- **VerticalThumbTrack**: True
- **WantTabKey**: True
- **Look and Feel**: Appearance
  - **Appearance**: Appearance
  - **BaseStyles**
  - **ChildGroupOptions**: ShowAddNewRecord
  - **NestedTableOptions**: ShowTreeLines = True
  - **TopLevelGroupOptions**: ShowAddNewRecord
- **Optimization**: 
  - **AllowedOptimizeLoad**: None
  - **AllowOptimizeLoad**: True
  - **BindToCurrencyManager**: True
  - **CacheRecordValues**: False
  - **CounterLogic**: All
  - **InsertRemoveRefreshDirty**: InvalidateVisible

**Sample Data:**
The grid displays a dataset with 225 items, grouped by "Sport." For Football, there are 108 items, and the data is further categorized into groups based on the number of wins (e.g., wins: 0, wins: 1, wins: 2, etc.).

**Details:**
- **Football Teams Data:**
  - **Wins: 0 - 3 Items**
    - Duke (0 wins, 11 losses, 0 ties)
    - Duke (0 wins, 11 losses, 0 ties)
    - Duke (0 wins, 11 losses, 0 ties)
  - **Wins: 1 - 2 Items**
    - Georgia Tech (1 win, 10 losses, 0 ties)
    - Wake Forest (1 win, 10 losses, 0 ties)
  - **Wins: 2 - 8 Items**
    - (Items not expanded)
  - **Wins: 3 - 14 Items**
    - (Items not expanded)

**Category Grid Example:**
The second grid displays a dataset grouped by "CategoryName," showing hierarchical details. The categories include:
- Beverages
- Condiments
- Confections
- Dairy Products

**Category Grid Data:**
- **CategoryName: Beverages**
  - **CategoryID**: 1
  - **Description**: Soft drinks, coffees, teas, beers, and

**Explanation:**
- The UI provides design-time support for customizing the appearance and structure of the Grid Grouping Control. Features such as grouping, sorting, and collapsing/expanding of groups are clearly demonstrated. Customization options like appearance, base styles, and optimization settings can be adjusted to enhance the user experience and performance.

## API Reference
- **Namespace**: `Syncfusion.Windows.Forms.Grid`
  - **Class**: `GridTableCellStyleInfo`
    - **Properties**: Appearance-related settings including background color, font, text color, etc.
    - **Methods**: 
      - `SetAppearance`: Adjusts the appearance of grid cells.
      - `GetAppearance`: Retrieves the current appearance settings.
    - **Events**: OnAppearanceChanged

## Code Examples
```csharp
// Example: Customizing Grid Appearance
grid.TableModel.SetStyle(GridRangeStyle.RowColumn(1, 1), new GridTableCellStyleInfo
{
    BackColor = Color.LightGray,
    Font = new Font("Arial", 10, FontStyle.Bold),
    TextForeColor = Color.Black
});
```

## Tags and Keywords
<!-- tags: [gridgroupingcontrol, designtime, appearance, windowsforms, syncfusion, optimization] keywords: [customization, hierarchicaldata, grouping, runtimeoptions] -->
```