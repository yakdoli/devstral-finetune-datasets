```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_213.jpeg
document_name: grid
page_number: 213
page_id: grid#page_213
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:03:13Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### 4.1.4.4.6 Enhanced Numeric Up Down

The Numeric Up Down cell type has been enhanced to provide more styles and properties that can be added to the numeric up down control by using the `FloatNumericUpDownStyleProperties` class. It enables you to set the limitations of the numeric values and several other properties.

| **Float Numeric Up Down Style Property** | **Description**                                                                 |
|------------------------------------------|---------------------------------------------------------------------------------|
| BackColor                                | Specifies the back color of the container.                                     |
| Maximum                                  | Indicates the maximum value that the cell can have.                            |
| StartValue                              | The starting value of the embedded cell.                                       |
| Step                                    | The value that has to be incremented for each click of the button.              |
| WrapValue                               | The bool value that will allow to wrap the text.                               |
| DecimalPlaces                           | The decimal values after the decimal point.                                    |
| Orientation                             | Orientation of the cell container on NumericUpDown.                             |
| InterceptArrowkeys                      | Allows to change the value by using ARROW keys from keyboard.                   |
| ThousandsSeparator                      | The bool value which allows to separate the thousand basis.                     |

The following code examples illustrate how to set the cell type to `FNumericUpDown`.

#### 1. Using C#

```csharp
RegisterCellModel.GridCellType(this.gridControl1, CustomCellTypes.FNumericUpDown);
GridStyleInfo style = this.gridControl1[1, 1];
```

<!-- tags: [Syncfusion, Winforms, Numeric Up Down, FloatNumericUpDownStyleProperties, Grid] keywords: [numeric up down, styles, properties, maximum value, start value, step, wrap value, decimal places, orientation, intercept arrow keys, thousands separator] -->
```