```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_148.jpeg
document_name: XlsIO
page_number: 148
page_id: XlsIO#page_148
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:02Z
fidelity: lossless
-->

# Essential XlsIO

![](image.png)

*Figure 49: Removing Conditional Format by using Excel*

## Removing Conditional Formats in XlsIO

XlsIO also provides support for removing the conditional formats. Following are the methods for removing the conditional formats associated with the IConditionalFormat interface.

- Remove
- RemoveAt

### Removing Conditional Formats at specified range

XlsIO removes the conditional formats at specified range by using Remove Method.

The following code example illustrates this.

```csharp
// Removing conditional format at the specified range.
sheet.Range["E5"].ConditionalFormats.Remove();
```

## 6.5 Creating a Custom Conditional Format

(C) 2013 Syncfusion. All rights reserved. | 148 | Page
```

<!-- tags: [xlsio, conditional format, removing conditional formats, xssf, syncfusion winforms, syncfusion, iconditionalformat] keywords: [conditional format, xssf, remove, removeat, clear rules, custom conditional format] -->
