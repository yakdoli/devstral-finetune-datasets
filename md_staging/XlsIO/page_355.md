```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_355.jpeg
document_name: XlsIO
page_number: 355
page_id: XlsIO#page_355
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:12:04Z
fidelity: lossless
-->

## XlsIO

![Error box](attachment://Error_box.png)

**Figure 132: Error box**

XlsIO has numerous validation rules and features which are demonstrated in the following code example. The `AllowType` property sets the type of validation, `CompareOperator` sets the validation criteria, and `ShowErrorBox` shows the error box with an error message.

### [C#]

```csharp
// Data Validation for Numbers.
IDataValidation validation1 = sheet.Range["A3"].DataValidation;
sheet.Range["A3"].Text = "Enter a Number";
validation1.AllowType = ExcelDataType.Integer;
validation1.CompareOperator = ExcelDataValidationComparisonOperator.Between;
validation1.FirstFormula = "0";
validation1.SecondFormula = "10";
validation1.ShowErrorBox = true;
validation1.ErrorBoxText = "Enter Value between 0 to 10";
validation1.ErrorBoxTitle = "ERROR";
validation1.PromptBoxText = "Data Validation using Condition for Numbers";
validation1.ShowPromptBox = true;

// Data Validation for Date.
IDataValidation validation2 = sheet.Range["A5"].DataValidation;
sheet.Range["A5"].Text = "Enter the Date";
validation2.AllowType = ExcelDataType.Date;
validation2.CompareOperator = ExcelDataValidationComparisonOperator.Between;
validation2.FirstDateTime = new DateTime(2003, 5, 10);
validation2.SecondDateTime = new DateTime(2004, 5, 10);
validation2.ShowErrorBox = true;
validation2.ErrorBoxText = "Enter Value between 10/5/2003 to 10/5/2004";
validation2.ErrorBoxTitle = "ERROR";
validation2.PromptBoxText = "Data Validation using Condition for Date";
validation2.ShowPromptBox = true;
```

### [VB.NET]

```vb
' Data Validation for Numbers.
Dim validation1 As IDataValidation = sheet.Range("A3").DataValidation
sheet.Range("A3").Text = "Enter a Number"
```

```html
<!-- tags: [XlsIO, Data Validation, Error box, validation rules, validation features, ExcelDataValidationComparisonOperator, showerrorbox, errorboxtext, datatype validation] keywords: [Data Validation, AllowType, CompareOperator, validation1, validation2, sheet.Range, validation criteria, error box with messageistinguished] -->
```