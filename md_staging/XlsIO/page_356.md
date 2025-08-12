```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_356.jpeg
document_name: XlsIO
page_number: 356
page_id: XlsIO#page_356
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:13:15Z
fidelity: lossless
-->

## Essential XlsIO

### Content

Set up data validation rules in Excel spreadsheets. The following examples demonstrate how to apply data validation for numbers and dates.

```csharp
validation1.AllowType = ExcelDataType.Integer
validation1.CompareOperator = ExcelDataValidationComparisonOperator.Between
validation1.FirstFormula = "0"
validation1.SecondFormula = "10"
validation1.ShowErrorBox = True
validation1.ErrorBoxText = "Enter Value between 0 to 10"
validation1.ErrorBoxTitle = "ERROR"
validation1.PromptBoxText = "Data Validation using Condition for Numbers"
validation1.ShowPromptBox = True
```

```csharp
' Data Validation for Date.
Dim validation2 As IDataValidation = sheet.Range("A5").DataValidation
sheet.Range("A5").Text = "Enter the Date"
validation2.AllowType = ExcelDataType.Date
validation2.CompareOperator = ExcelDataValidationComparisonOperator.Between
validation2.FirstDateTime = New DateTime(2003,5,10)
validation2.SecondDateTime = New DateTime(2004,5,10)
validation2.ShowErrorBox = True
validation2.ErrorBoxText = "Enter Value between 10/5/2003 to 10/5/2004"
validation2.ErrorBoxTitle = "ERROR"
validation2.PromptBoxText = "Data Validation using Condition for Date"
validation2.ShowPromptBox = True
```

#### Reading the Existing Data Validation Settings

You can also read the Data Validation settings in an existing workbook. The following code example illustrates this.

##### C#

```csharp
// Reading the Data Validation list.
this.comboBox1.Items.AddRange(sheet.Range["A1"].DataValidation.ListOfValues);
```

##### VB.NET

```vb
' Reading the Data Validation list.
Me.comboBox1.Items.AddRange(sheet.Range("A1").DataValidation.ListOfValues)
```

### See Also

- AutoFilters, Importing and Exporting, Template Markers, Grouping and Ungrouping

<!-- tags: [xlsio, data validation, essential xlsio, syncfusion winforms, v11.4.0.26] keywords: [data validation rules, numeric data validation, date validation, error messages, prompts, list of values, reading data validation settings] -->
```