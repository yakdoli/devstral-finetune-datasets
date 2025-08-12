```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_295.jpeg
document_name: tools
page_number: 295
page_id: tools#page_295
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:04:23Z
fidelity: lossless
--> 

## Overview
- Detailed information on `AutoCompleteSource` enum values for WinForms AutoComplete features.
- Examples in both C# and VB.NET for configuring the AutoCompleteSource property.

## Content

### AutoCompleteSource Enum

The `AutoCompleteSource` enum defines the data source for autocomplete functionality in Windows Forms. Below are the various values this enum supports:

- **HistoryList**: Includes all the URLs in the history list.
- **RecentlyUsedList**: Includes the list of most recently used URLs.
- **AllUrl**: Equivalent source of `HistoryList` and `RecentlyUsedList` as the source.
- **AllSystemSources**: Equivalent source of `AllUrls` and `FileSystem` as the source (Default value of `AutoCompleteSource` when `AutoCompleteMode` is set to values other than default).
- **ListItems**: Specifies the items in the control.
- **FileSystemDirectories**: Specifies directory names alone without file names.
- **CustomSource**: Uses the string values entered in `AutoCompleteCustomSource` property.
- **None**: There will not be any source for the auto completion.

### Code Examples

#### C#
```csharp
this.textBox1.AutoCompleteSource = 
System.Windows.Forms.AutoCompleteSource.HistoryList;
```

#### VB.NET
```vb
Me.textBox1.AutoCompleteSource = 
System.Windows.Forms.AutoCompleteSource.HistoryList
```

## API Reference

- **Namespace**: `System.Windows.Forms`
- **Class**: `TextBox`
- **Property**: `AutoCompleteSource`
  - Type: `AutoCompleteSource`
  - Description: Specifies the data source for autocomplete.

### Parameters

| Name | Type | Description | Default | Required |
|------|------|-------------|---------|----------|
| `AutoCompleteSource` | `AutoCompleteSource` | The source from which autocomplete suggestions are provided. | `None` | Yes |

### Returns

- Type: None (Property setter)
- Description: Sets the data source for autocomplete suggestions in the TextBox control.

### Exceptions

- None explicitly mentioned in this context.

---

### Getting Started

To implement AutoComplete functionality in a Windows Forms application, you can configure the `AutoCompleteSource` property as shown in the examples above. This allows users to quickly input common or recently used values, improving usability and efficiency.

## Page-level Navigation/TOC (if applicable)

- Overview
- Content
  - AutoCompleteSource Enum
  - Code Examples
- API Reference
  - Parameters
  - Returns
  - Exceptions
- Getting Started

## Cross References

- [Link to AutoCompleteMode documentation](#) (for different modes of autocomplete)
- [Link to TextBox Control documentation](#) (for general control details)

## RAG Annotations
```html
<!-- tags: [AutoCompleteSource, Windows Forms, AutoComplete, TextBox, C#, VB.NET] keywords: [AutoCompleteSource, HistoryList, RecentlyUsedList, AllUrl, AllSystemSources, ListItems, FileSystemDirectories, CustomSource, None, AutoCompleteMode] -->
```
```