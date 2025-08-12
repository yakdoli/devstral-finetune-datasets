```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_294.jpeg
document_name: tools
page_number: 294
page_id: tools#page_294
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:12Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Focuses on configuring the AutoComplete control for History Data List mode.
- Describes the properties and settings required for proper functionality.

## Content

### Setting Up History Data List Mode

- **Properties to Configure:**
  - `CategoryName`
  - `AutoAddItem`
  - `AutoSerialize`

The `CategoryName`, `AutoAddItem`, and `AutoSerialize` properties must be set appropriately for the History Data List mode to work properly.

#### Code Examples

**C#**
```csharp
this.autoCompletel.CategoryName = "FTP";
this.autoCompletel.DataSource = DataTable1;
```

**VB.NET**
```vb
Me.autoCompletel.CategoryName = "FTP"
Me.autoCompletel.DataSource = DataTable1
```

**Note:** We can set External datasource for the autocompletion. See **External DataSource** topic.

### Dynamic Source at RunTime

Enabling the `AutoComplete.AutoAddItem` property will allow the end users to save their entries at run time. Pressing Enter key will save the user entry. See **Through Designer** topic for details.

### Setting AutoCompletion Source Through Designer

The different sources available for auto completion are specified using the `Control.AutoCompleteSource` property. When the end user enters a letter in the TextBox for example, the letter will be matched with the source available and displays the dropdown item accordingly.

#### Property Description

| Property           | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| AutoCompleteSource | Auto completion source for the control. The different sources are,         |
|                    | File System - Files system as source,                                      |

### More Information

- **See Also**
  - **How to delete the items in the list at run time?**
  - **3.5.1.1.3.2.2 Source for AutoComplete Control**

### Summary

- The AutoComplete control's functionality is enhanced by configuring the appropriate properties, such as `CategoryName`, `AutoAddItem`, and `AutoSerialize`.
- Code examples in C# and VB.NET are provided to demonstrate setting the `CategoryName` and `DataSource`.
- The ability to add new entries dynamically is facilitated through the `AutoAddItem` property.

## API Reference

- **Properties**
  - `AutoCompleteSource`: Specifies the source of auto-completion data.

## Code Examples

Refer to the examples provided in the **C#** and **VB.NET** sections for configuring the AutoComplete control.

## Page-level Navigation/TOC

- **Setting Up History Data List Mode**
- **Dynamic Source at RunTime**
- **Setting AutoCompletion Source Through Designer**
- **Summary**

<!-- tags: [AutoComplete control, CategoryName, AutoAddItem, AutoSerialize, History Data List, External DataSource, AutoCompleteSource, VB.NET, C#] -->
```