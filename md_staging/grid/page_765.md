```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_765.jpeg
document_name: grid
page_number: 765
page_id: grid#page_765
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:22Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Setting Expression Fields Through Code

#### Figure 307: Setting Expression Fields Through Code

| ID   | losses | School         | Sport    | ties | wins | year | Winning % | Losing % |
|------|--------|----------------|----------|------|------|------|-----------|----------|
| 1    | 7      | Duke           | Basketball | 0   | 26   | 2003 | 78.79      | 21.21     |
| 2    | 10     | Maryland       | Basketball | 0   | 21   | 2003 | 67.74      | 32.26     |
| 3    | 6      | Wake Forest    | Basketball | 0   | 25   | 2003 | 80.65      | 19.35     |
| 4    | 15     | Georgia Tech    | Basketball | 0   | 16   | 2003 | 51.61      | 48.39     |
| 5    | 16     | Virginia       | Basketball | 0   | 16   | 2003 | 50.00      | 50.00     |
| 6    | 13     | NC State       | Basketball | 0   | 18   | 2003 | 58.06      | 41.94     |
| 7    | 16     | North Carolina | Basketball | 0   | 19   | 2003 | 54.29      | 45.71     |
| 8    | 13     | Clemson        | Basketball | 0   | 15   | 2003 | 53.57      | 46.43     |
| 9    | 15     | Florida State  | Basketball | 0   | 14   | 2003 | 48.28      | 51.72     |
| 10   | 7      | Duke           | Football   | 0   | 3    | 2003 | 30.00      | 70.00     |
| 11   | 3      | Maryland       | Football   | 0   | 6    | 2003 | 66.67      | 33.33     |
| 12   | 5      | Wake Forest    | Football   | 0   | 5    | 2003 | 50.00      | 50.00     |
| 13   | 4      | Georgia Tech    | Football   | 0   | 5    | 2003 | 55.56      | 44.44     |

#### Note: For more details, refer the following browser sample:

<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Filters and Expressions\Expression Field Demo

### See Also

#### 4.3.4.3.4.1.1 Nested Expression Fields

Expression fields can be **nested**, meaning that the formula expression of an expression field can have reference to other fields. Given below are examples for nested expression fields.

- `ExpressionField1.Expression = "[Col1] * 100"`
- `ExpressionField2.Expression = "[ExpressionField1] + 0.5"`
- `ExpressionField3.Expression = "[ExpressionField1] + [ExpressionField2]"`

### Sample Code

## API Reference

Not applicable.

## Code Examples

Not applicable.

## Page-level Navigation/TOC

Not applicable.

## Cross References

- 4.3.4.3.4.1.1 Nested Expression Fields

<!-- tags: [WinForms, EssentialGrid, ExpressionFields, NestedExpressionFields, Version11.4.0.26] keywords: [expression fields, nested expression fields, essential grid, windows forms, duke, basketball] -->
```