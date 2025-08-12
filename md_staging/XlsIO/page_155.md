```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_155.jpeg
document_name: XlsIO
page_number: 155
page_id: XlsIO#page_155
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:58:09Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Describes the Conditional Formatting feature in XlsIO.
- Explains the Icon Sets functionality for highlighting cells based on specific rules.
- Details how to apply icon sets and hide cell values.

## Content

### Icon Sets in XlsIO

#### Figure 54: Icon Sets

![Icon Sets](https://i.imgur.com/figure54.png)

- The image illustrates the conditional formatting options available in XlsIO, focusing on the use of icon sets for highlighting cells based on specific rules.
- Various icon sets, such as arrows, flags, checkmarks, and similar symbols, are displayed to show different conditional formatting options that can be applied.

#### Using Conditional Formatting with Icon Sets

It is possible to hide the value of the cell and just draw the icon, while applying a conditional formatting rule for icon sets, by using the New Formatting Rule dialog box.

## API Reference

### Conditional Formatting Methods

For applying icon sets in XlsIO, use the following:

```csharp
worksheet.ConditionalFormatting.FilePath = "YourFormattingRule.xlsx";
// Apply other properties and rules as necessary.
```

#### Examples

- **Example 1: Applying Icon Set to Cells**

```csharp
// Assume 'worksheet' is the worksheet range to apply formatting.
var conditionalFormat = worksheet.ConditionalFormatting.CreateIconSetCondition();
conditionalFormat.ConditionValue = ConditionValue.IconSet;
conditionalFormat.IconType = IconType.Arrows4;
```

### Further Reading

For more detailed information on conditional formatting and icon sets, refer to the following resources:

- [XlsIO Documentation on Conditional Formatting](https://docs.syncfusion.com/windowsforms/xlsio/conditionalformatting/)
- [Syncfusion Support for XlsIO Features](https://www.syncfusion.com/support/windowsforms/xlsio)

---

<!-- tags: xlsio, conditional formatting, icon sets, winforms, 11.4.0.26 keywords: essential xlsio, icon sets, conditional formatting, winforms, xlsx, document processing -->
```