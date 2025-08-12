```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_391.jpeg
document_name: XlsIO
page_number: 391
page_id: XlsIO#page_391
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:14:19Z
fidelity: lossless
-->

## Essential XlsIO

### Code Example

```vb
' Expand group with flag set to expand parent.
worksheet.Range("A11:A19").ExpandGroup(ExcelGroupBy.ByRows, ExpandCollapseFlags.ExpandParent)

' Collapse group.
worksheet.Range("A61:A114").CollapseGroup(ExcelGroupBy.ByRows)
```

### For More Information Refer:
- [AutoFilters](AutoFilters)
- [Validating Data](Validating Data)
- [Template Markers](Template Markers)
- [Grouping and Ungrouping](Grouping and Ungrouping)

## 4.6 Review

This section explains how the following features can be implemented by using XlsIO.

- **Comments** - This topic explains how comments can be inserted and formatted using the XlsIO's APIs.
- **Changes** - This topic explains various protection levels of Excel supported by XlsIO.

## 4.6.1 Comments

Microsoft Excel has the ability to insert Comments in cells. Comments enable a user to get additional information about a cell, such as, what the value represents. You can insert and format comments through the Insert menu in Excel. You can also format the comments inserted through the Format Comment dialog box.

<!-- tags: [xlsio, winforms, comments, group, collapse, expand, template markers, auto filters, validating, template markers, grouping, ungrouping] keywords: [comments, excel, protect, unprotect, group, expand parent, expandcollapseflags,ranges] -->
``` 
