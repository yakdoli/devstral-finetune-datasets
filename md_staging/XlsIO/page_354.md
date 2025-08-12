```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_354.jpeg
document_name: XlsIO
page_number: 354
page_id: XlsIO#page_354
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:10:20Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates how to configure data validation in Excel using XlsIO.
- Explains the use of the `DataValidation` class to validate specific cell values.
- Illustrates setting up error alert options in the Data Validation dialog.

## Content

### Configuring Data Validation

Below are examples of configuring data validation in Excel using C# and VB.NET.

#### C#

```csharp
validation.PromptBoxText = "Data Validation list";
validation.IsPromptBoxVisible = true;
validation.ShowPromptBox = true;
```

#### VB.NET

```vb
' Data validation to list the values in the first cell.
Dim validation As IDataValidation = sheet.Range("A1").DataValidation
sheet.Range("A1").Text = "Data validation list"
validation.ListOfValues = New String() {"ListItem1", "ListItem2", "ListItem3"}
validation.PromptBoxText = "Data Validation list"
validation.IsPromptBoxVisible = True
validation.ShowPromptBox = True
```

### Error Alert Settings

The following screenshots illustrate the error alert settings through the **Data Validation** dialog box in MS Excel.

**Figure 131: Error Alert Options in MS Excel**

![Error Alert Options in MS Excel](https://i.imgur.com/Fig131.png)

The settings shown include:
- **Show error alert after invalid data is entered**
- **Style**: Warning
- **Title**: ERROR
- **Error message**: RetySe text length to 25 character

### Example of Error Alert Settings

The screenshot depicts:
- A checkbox indicating to show an error alert after invalid data is entered.
- Options to customize the alert style (Warning in this case).
- The title of the error alert and the error message that will be displayed.

## Code Examples

Here are the complete code snippets for setting up data validation with error alerts:

### C#

```csharp
// Configuring Data Validation
IWorkbook workbook = new Workbook();
IWorksheet sheet = workbook.Worksheets[0];

IDataValidation validation = sheet.Range["A1"].DataValidation;
validation.ListOfValues = new string[] { "ListItem1", "ListItem2", "ListItem3" };
validation.PromptBoxText = "Data Validation list";
validation.IsPromptBoxVisible = true;
validation.ShowPromptBox = true;

// Configuring Error Alert
validation.ShowErrorAlert = true;
validation.ErrorStyle = ErrorStyle.Warning;
validation.ErrorTitle = "ERROR";
validation.ErrorMessage = "Retry text length to 25 character";

workbook.Save("Output.xlsx");
```

### VB.NET

```vb
' Configuring Data Validation
Dim workbook As IWorkbook = New Workbook()
Dim sheet As IWorksheet = workbook.Worksheets(0)

Dim validation As IDataValidation = sheet.Range("A1").DataValidation
validation.ListOfValues = New String() {"ListItem1", "ListItem2", "ListItem3"}
validation.PromptBoxText = "Data Validation list"
validation.IsPromptBoxVisible = True
validation.ShowPromptBox = True

' Configuring Error Alert
validation.ShowErrorAlert = True
validation.ErrorStyle = ErrorStyle.Warning
validation.ErrorTitle = "ERROR"
validation.ErrorMessage = "Retry text length to 25 character"

workbook.Save("Output.xlsx")
```

## API Reference

### DataValidation Properties
- `PromptBoxText`: Displays the text in the prompt box.
- `IsPromptBoxVisible`: Indicates if the prompt box is visible.
- `ShowPromptBox`: Enables or disables the prompt box.
- `ShowErrorAlert`: Enables or disables the error alert.
- `ErrorStyle`: Sets the style of the error alert (e.g., Warning, Information, Stop).
- `ErrorTitle`: Sets the title of the error message.
- `ErrorMessage`: Sets the content of the error message.

## Cross References
- **See also:** 
  - "Data Validation in MS Excel" for more examples and usage scenarios.

<!-- tags: [xlsio, datavalidation, erroralert, syncfusionwinforms] keywords: [data validation, error alert, prompt box, validation list, ms excel, workbooks, worksheets, ranges] -->
```