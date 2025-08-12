```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_873.jpeg
document_name: tools
page_number: 873
page_id: tools#page_873
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:14Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Instructions

1. **Run the application.** You will be able to see the `NumericUpDownExt` control in your form.

   ![NumericUpDownExt created Through Code](./image.png)
   *Figure 553: NumericUpDownExt created Through Code*

### Concepts and Features

#### Value Settings

The various values of the `NumericUpDownExt` control and their settings are given below.

| **NumericUpDownExt Properties** | **Description**                                                                                                                                                       |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Value                           | Gets / sets the value assigned to the spin box (also known as an up-down control).                                                                                  |
| Hexadecimal                     | Gets / sets the value indicating whether the spin box (also known as an up-down control) should display the value it contains in hexadecimal format.                |
| HexValue                        | Gets the value in hexadecimal numeration.                                                                                                                            |
| Minimum                          | Gets / sets the minimum allowed value for the spin box (also known as an up-down control).                                                                         |
| Increment                        | Gets / sets the value to increment or decrement the spin box (also known as an up-down control) when the up or down buttons are clicked. The default value is set to '1'. |

#### Code Example in C#

```csharp
this.numericUpDownExt1.Value = new decimal(new int[] { 25, 0, 0, 0 });
this.numericUpDownExt1.Hexadecimal = true;
this.numericUpDownExt1.Minimum = new decimal(new int[] { 50, 0, 0, 0 });
```

### Footer

© 2013 Syncfusion. All rights reserved. 873 |

<!-- tags: [product, windows forms, control, numericupdownext, version] keywords: [Syncfusion, numericupdownext, winforms, properties, value, minimum, increment, hexadecimal] -->
```