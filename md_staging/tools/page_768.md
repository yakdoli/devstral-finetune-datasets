```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_768.jpeg
document_name: tools
page_number: 768
page_id: tools#page_768
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:33:24Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## ![PercentTextBox created Through Code](https://i.imgur.com/B08jz.png)

**Figure 484:** PercentTextBox created Through Code

### 3.5.8.5.3 Concepts and Features

The following Editors controls (DoubleTextBox, IntegerTextBox, PercentTextBox, and CurrencyTextBox) have been revamped. Click [here] to see the details of revamping.

#### 3.5.8.5.3.1 Display Settings

This section discusses the display settings of the PercentTextBox control.

The PercentTextBox provides a list of properties to set the display characteristics of the percentage.

| PercentTextBox Properties           | Description                                                                                      |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| PercentDecimalDigits                | Gets / sets the maximum number of digits for the decimal portion of the percentage.            |
| PercentDecimalSeparator             | Gets / sets the decimal separator character that will be used for the display.                 |
| PercentGroupSeparator               | Gets / sets the separator to be used for grouping digits.                                        |
| PercentGroupSizes                   | Gets / sets the grouping of percent digits in the PercentTextBox.                              |
| PercentNegativePattern              | Gets / sets the pattern to use when the value is negative.                                      |
| NegativeSign                         | Gets / sets the sign that is to be used to indicate a negative value.                          |
| PercentPositivePattern              | Gets / sets the pattern to use when the value is positive.                                       |

## API Reference

### DiagramAPI

- **DiagramAPI** (Namespace): The namespace containing the API related to diagram controls.
- **DiagramProperties**:
  - **Property**: Type
    - **Description**: Short description of the property.

## Code Examples

The following is an example of using PercentTextBox in a Windows Forms application:

```csharp
PercentTextBox percentTextBox = new PercentTextBox();
percentTextBox.PercentDecimalDigits = 2;
percentTextBox.PercentDecimalSeparator = '.';
percentTextBox.PercentGroupSeparator = ',';
percentTextBox.PercentNegativePattern = "-n%";
percentTextBox.NegativeSign = '-';
percentTextBox.PercentPositivePattern = "n%";
```

### Notes

- The properties listed above can be used to customize the display format of the percentage value in the PercentTextBox control.
- Ensure that any custom separators or patterns adhere to the formatting rules to avoid runtime errors.

## Related Topics

- [Working with PercentTextBox Control](https://docs.syncfusion.com/winforms/percenttextbox-control)
- [Formatting Options in Windows Forms Controls](https://docs.syncfusion.com/winforms/formatting-options-in-winforms)

<!-- tags: Windows Forms, Windows Forms Controls, PercentTextBox, PercentDecimalDigits, PercentGroupSeparator, PercentNegativePattern, PercentPositivePattern, version: 11.4.0.26 -->
```
``` 
