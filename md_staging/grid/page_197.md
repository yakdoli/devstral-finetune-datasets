```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_197.jpeg
document_name: grid
page_number: 197
page_id: grid#page_197
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:55Z
fidelity: lossless
--> 

## Number Formats and Cell Tips

### Overview
- Demonstrates the use of custom number formats in a grid control.
- Illustrates how to set cell tips using the `CellTipText` object.

### Content

#### Number Formats

1. **Using C#**
   ```csharp
   [C#]
   
   this.gridControl1[2, 2].Format = "###0.##%";
   ```

2. **Using VB.NET**
   ```vbnet
   [VB.NET]
   
   Me.gridControl1(2, 2).Format = "###0.##%"
   ```

Below is a table showing different number formats:

|   | Number Formats           |
|---|---------------------------|
| 2 |                           |
| 3 | 0.00                    | C | 0.00; (0.00) | ###0.##% | #0.#E+00 |
| 4 | 3.14                    | $3.14       | 3.14        | 314.16%  | 31.4E-01 |

**Figure 104: Number Formats**

#### Cell Tips

##### 4.1.4.2.10.4 Cell Tips

The `CellTipText` object allows you to specify the tooltip text displayed when the mouse pointer moves over a cell. Cell tip text can be set for rows, columns, tables, and individual cells.

The following code examples illustrate how to set cell tips using the `CellTipText` object:

1. **Using C#**
   ```csharp
   [C#]
   
   // Tip Text for cell (2,3).
   this.gridControl1[2, 3].CellTipText = "TipText for cell 2,3";
   
   // Tip Text for row 3.
   this.gridControl1.RowStyle[3].CellTipText = "TipText for row 3";
   
   // Tip Text for column 4.
   this.gridControl1.ColStyle[4].CellTipText = "TipText for column 4";
   ```

## Page-level Navigation/TOC

- Number Formats
  - Using C#
  - Using VB.NET
- Cell Tips
  - Setting Cell Tips Using `CellTipText`

## RAG Annotations
<!-- tags: [syncfusion, winforms, grid, number formats, cell tips, cell tip text, cell styles] keywords: [grid, CellTipText, number formats, tooltip, cell tip, C#, VB.NET] -->
```