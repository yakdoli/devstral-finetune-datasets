```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_358.jpeg
document_name: grid
page_number: 358
page_id: grid#page_358
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:11:25Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Substitutes new_text for old_text in a text string. Use SUBSTITUTE when you want to replace specific text in a text string; use REPLACE when you want to replace any text that occurs in a specific location in a text string.

## Syntax

SUBSTITUTE(text, old_text, new_text, instance_num), where:

- Text is the text or the reference to a cell containing text for which you want to substitute characters.
- Old_text is the text you want to replace.
- New_text is the text you want to replace old_text with.
- Instance_num specifies which occurrence of old_text you want to replace with new_text. If you specify instance_num, only that instance of old_text is replaced. Otherwise, every occurrence of old_text in text is changed to new_text.

## Example

The example may be easier to understand if you copy it to a blank worksheet.

|   | A            |                 |           |
|---|--------------|-----------------|-----------|
| **1** | **Data**   |                 |           |
| **2** | **Sales Data** |                 |           |
| **3** | **Quarter 1, 2008** |                     |           |
| **4** | **Quarter 1, 2011** |                     |           |
|       | **Formula**       | **Description (Result)** |           |
|       | `=SUBSTITUTE(A2, "Sales", "Cost")` | Substitutes Cost for Sales (Cost Data).     |
|       | `=SUBSTITUTE(A3, "1", "2", 1)`     | Substitutes first instance of "1" with "2" (Quarter 2, 2008). |
|       | `=SUBSTITUTE(A4, "1", "2", 3)`     | Substitutes third instance of "1" with "2" (Quarter 1, 2012). |

## 4.1.4.6.6.230 SUBTOTAL

The SUBTOTAL function returns a subtotal in a list. Once the subtotal list is created, you can modify it by editing the SUBTOTAL function.

<!-- tags: [essential grid, windows forms, substitute function, replace function, subtotal function, text manipulation, cell reference] keywords: [substitute, replace, text string, old_text, new_text, instance_num, sales data, quarter, formula, result, subtotal] -->
```