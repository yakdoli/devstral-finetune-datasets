```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_353.jpeg
document_name: XlsIO
page_number: 353
page_id: XlsIO#page_353
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:12:48Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Explains the **Data Validation Settings** in **Essential XlsIO** for configuring validation rules in Excel worksheets.
- Describes the use of the **IDataValidation class** for implementing different types of validation in Excel.

## Content

### Data Validation in Essential XlsIO

Essential XlsIO, equivalent to the MS Excel, is built with APIs to read and write data validation in a worksheet by using the **IDataValidation** class. Following are some validation types that XlsIO supports:

#### Supported Validation Types
- Text Length Validation
- Time Validation
- List Validation
- Number Validation
- Date Validation
- Custom Validation

#### Example: Validation Settings GUI

**Figure 130: Data Validation Settings**

![Data Validation Settings](attachment:Figure_130.png)

#### Example Code: List Validation

```csharp
// Data validation to list the values in the first cell.
IDataValidation validation = sheet.Range["A1"].DataValidation;
sheet.Range["A1"].Text = "Data validation list";
validation.ListOfValues = new string[] { "ListItem1", "ListItem2", "ListItem3" };
```

#### Additional Resource
An article which describes data validation is available in the following path:  
[http://www.syncfusion.com:91/products/xlsio/backoffice/Articles/data_validation.aspx](http://www.syncfusion.com:91/products/xlsio/backoffice/Articles/data_validation.aspx).

---

## API Reference
- **Namespace**: Syncfusion.XlsIO
- **Class**: IDataValidation
- **Members**:
  - **TextLengthValidation**: Validates the length of text entries.
  - **TimeValidation**: Ensures entries fit within specified time constraints.
  - **ListValidation**: Restricts entries to specific predefined values.
  - **NumberValidation**: Validates numerical inputs against certain criteria.
  - **DateValidation**: Ensures dates fall within specified ranges.
  - **CustomValidation**: Allows user-defined validation rules.

---

## Code Examples

- **Example 1: Date Validation**
  ```csharp
  IDataValidation validation = sheet.Range["A1"].DataValidation;
  validation.DataType = ExcelDataValidationDataType.Date;
  validation.BeginValue = DateTime.Parse("1/2/1900");
  validation.EndValue = DateTime.Parse("1/1/1984");
  sheet.Range["A1"].Text = "Date validation example";
  ```

- **Example 2: List Validation**
  ```csharp
  IDataValidation validation = sheet.Range["A1"].DataValidation;
  validation.ListOfValues = new string[] { "ListItem1", "ListItem2", "ListItem3" };
  sheet.Range["A1"].Text = "Data validation list";
  ```

---

## Cross References
- Refer to the official **Syncfusion Documentation**:  
[http://www.syncfusion.com/products/xlsio](http://www.syncfusion.com/products/xlsio)

<!-- tags: [Essential XlsIO, data validation, Syncfusion Winforms, API, version 11.4.0.26] keywords: [data validation, IDataValidation, Excel, validation types, C#, code examples, documentation, date validation, list validation, number validation, custom validation] -->
```