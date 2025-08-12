```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_843.jpeg
document_name: tools
page_number: 843
page_id: tools#page_843
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:15Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to use separators in date, time, and numeric formats.
- Demonstrates changing default separators for date, time, and numeric values.

## Content

### Separator Properties

| Property            | Description                                                                                           |
|---------------------|-------------------------------------------------------------------------------------------------------|
| DateSeparator       | Specifies the character to use when a date separator position is specified. The default separator is `'.'`. |
| ThousandSeparator   | Specifies the character to use when a thousands separator position is specified. The default separator is `','`. |
| TimeSeparator       | Specifies the character to use when a time separator position is specified. The default separator is `':'`. |

For example, if you want to display the user data in date time format as `mm/dd/yy`, the mask character should be `####/####`.

We can change the default separators used. If you want to display the date time as `'mm-dd-yy'`, change the `DateSeparatorProperty` from `'/'` to `'-'`.

Similarly, other separators can be used.

#### C#

```csharp
this.maskedEditBox1.DateSeparator = '-';
this.maskedEditBox1.DecimalSeparator = '.';
this.maskedEditBox1.ThousandSeparator = ',';
this.maskedEditBox1.TimeSeparator = ':';
```

#### VB.NET

```vb
Me.maskedEditBox1.DateSeparator = "-"C
Me.maskedEditBox1.DecimalSeparator = "."C
Me.maskedEditBox1.ThousandSeparator = ","C
Me.maskedEditBox1.TimeSeparator = ":"C
```

![Date Separator Set](image.png)

### Figure 536: Date Separator Set

## Conclusion
- This document provides guidance on customizing separators in Windows Forms to better suit specific formatting needs.

## Code Examples

#### C#

```csharp
this.maskedEditBox1.DateSeparator = '-';
this.maskedEditBox1.DecimalSeparator = '.';
this.maskedEditBox1.ThousandSeparator = ',';
this.maskedEditBox1.TimeSeparator = ':';
```

#### VB.NET

```vb
Me.maskedEditBox1.DateSeparator = "-"C
Me.maskedEditBox1.DecimalSeparator = "."C
Me.maskedEditBox1.ThousandSeparator = ","C
Me.maskedEditBox1.TimeSeparator = ":"C
```

## RAG Annotations
<!-- tags: [WinForms, mask, separator, date, time, numeric] keywords: [DateSeparator, TimeSeparator, ThousandSeparator, DecimalSeparator, format, mask character, WinForms, Syncfusion, separators] -->
```