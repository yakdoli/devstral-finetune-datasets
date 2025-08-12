```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_147.jpeg
document_name: XlsIO
page_number: 147
page_id: XlsIO#page_147
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:57:45Z
fidelity: lossless
-->

### Essential XlsIO

#### Figure 48: XlsIO with Conditional Formatting

## Reading Conditional Formats in XlsIO

XlsIO also provides support for reading conditional formats. Following code example illustrates this.

```csharp
// Read conditional formatting settings.
this.textBox1.Text = 
    sheet.Range["A1"].ConditionalFormats[0].FormatType.ToString();
this.textBox2.Text = 
    sheet.Range["A1"].ConditionalFormats[0].Operator.ToString();
this.textBox3.Text = 
    sheet.Range["A1"].ConditionalFormats[0].BackColor.ToString();
```

```vb
' Read conditional formatting settings.
Me.textBox1.Text = 
    sheet.Range("A1").ConditionalFormats(0).FormatType.ToString()
Me.textBox2.Text = 
    sheet.Range("A1").ConditionalFormats(0).Operator.ToString()
Me.textBox3.Text = 
    sheet.Range("A1").ConditionalFormats(0).BackColor.ToString()
```

## Removing Conditional Formats in MS-Excel

With Microsoft Excel, you can delete conditional formats from the selected cells or from the entire sheet.

To remove the conditional formats in MS-Excel:

1. Select the cell that has the conditional format that you want to delete.
2. Click **Conditional Formatting** on the **Home** tab, and then select **Clear Rules**. The **Clear Rules** property can be applied to the selected cells or to the entire sheet.

```


<!-- tags: [xlsio, conditional formatting, reading, removing, winforms, ms-excel] keywords: [xlsio, conditional formats, reading, removing, clear rules, selected cells, home tab] -->
```