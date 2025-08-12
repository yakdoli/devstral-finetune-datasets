```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_305.jpeg
document_name: tools
page_number: 305
page_id: tools#page_305
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:04:17Z
fidelity: lossless
-->

## Overview
- Demonstrates how to configure `AutoCompleteComboBox` columns and add history items using the `AddHistoryItem` method.
- Explains how to use external data sources to populate `AutoCompletePopup` with items that include images.
- Provides a sample location for implementing `AutoCompleteDemo` with external data sources.
- Describes the process for refreshing columns when using an external data source.

## Content

### AutoCompleteComboBox Configuration

The following VB.NET code snippet demonstrates configuring the `AutoCompleteComboBox` columns and adding history items:

```vb
[VB.NET]

Me.autoCompleteDataColumnInfo1.ColumnHeaderText = "Title"
Me.autoCompleteDataColumnInfo1.ImageColumn = False
Me.autoCompleteDataColumnInfo1.MatchingColumn = True
Me.autoCompleteDataColumnInfo1.Visible = True

Me.autoCompleteDataColumnInfo2.ColumnHeaderText = "Size"
Me.autoCompleteDataColumnInfo2.ImageColumn = True
Me.autoCompleteDataColumnInfo2.MatchingColumn = False
Me.autoCompleteDataColumnInfo2.Visible = True

Me.autoComplete1.AddHistoryItem("User Guide", 3)
Me.autoComplete1.AddHistoryItem("User Item", 2)
```

#### Figure 132: DropDownItem added to AutoComplete Popup using AddHistoryItem Method

![Figure 132: DropDownItem added to AutoComplete Popup using AddHistoryItem Method](https://i.imgur.com/8ZmKu.jpeg)

### Items with Images Through External DataSource

**Content**

Items with images can be added to the `AutoCompletePopup`, also using external data sources like XML files. A sample demonstrating the implementation of external data sources is available in the below location:

#### Sample Location

```text
..\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0\Editors Package\AutoCompleteDemo
```

**Refreshing Columns**

While using an external data source, the `Columns` property can be initially refreshed by clicking the **Refresh Columns** verb, visible in the designer.

## See Also

- [Multiple Columns](Multiple Columns)
- [3.5.1.1.3.5 Persistence](3.5.1.1.3.5 Persistence)

## API Reference

### Properties

- **autoCompleteDataColumnInfo**: Configures the columns for `AutoCompleteComboBox`.
  - **ColumnHeaderText**: Sets the text displayed in the column header.
  - **ImageColumn**: Specifies whether the column should display images.
  - **MatchingColumn**: Indicates whether the column should be used for matching.
  - **Visible**: Controls the visibility of the column.

### Methods

- **AddHistoryItem**: Adds an item to the history list of the `AutoCompleteComboBox`.
  - **Parameters**:
    - **ItemName**: The string representing the item to add.
    - **Weight**: An integer value indicating the weight of the item.

## Code Examples

### Adding History Items

```vb
Me.autoComplete1.AddHistoryItem("User Guide", 3)
Me.autoComplete1.AddHistoryItem("User Item", 2)
```

### Configuring Column Information

```vb
Me.autoCompleteDataColumnInfo1.ColumnHeaderText = "Title"
Me.autoCompleteDataColumnInfo1.ImageColumn = False
Me.autoCompleteDataColumnInfo1.MatchingColumn = True
Me.autoCompleteDataColumnInfo1.Visible = True
```

## RAG Annotations

<!-- tags: [Syncfusion Winforms, AutoCompleteComboBox, AutoCompletePopup, External DataSource, AddHistoryItem, Multiple Columns, Persistence] keywords: [AutoCompleteComboBox, AutoCompletePopup, History Items, External Data Source, Image Columns, MatchingColumn, Visible, Refresh Columns, AutoCompleteDemo, User Guide, User Item] -->
```