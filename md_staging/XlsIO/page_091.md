```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_091.jpeg
document_name: XlsIO
page_number: 091
page_id: XlsIO#page_091
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:54:06Z
fidelity: lossless
-->

# XlsIO

## Overview
- Demonstrates how to create and format a professional resume using Excel.
- Highlights the use of fonts, styles, images, and custom formatting.
- Illustrates the integration of personal details, employment history, and educational credentials.

## Content

### Employee Information Form

The following section presents a structured format for creating an employee resume using Excel. This example showcases Antony Jose's profile, including personal information, employment history, and educational background.

#### Employee Details

| **Field**        | **Value**               |
|------------------|-------------------------|
| **Name**         | Antony Jose             |
| **Title**        | Sales Manager           |
| **Birth Date**   | 01/04/92                |
| **Hire Date**    | 08/30/1963             |
| **Home Phone**   | (206) 555-3412          |
| **Extension**    | 3355                    |
| **Home Address** | 722 Moss Bay Blvd       |
| **Salary**       | $50,000.00              |

#### Professional Biography

Antony Jose graduated from St. Andrews University, Scotland, with a BSC degree in 1976. Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London. He was promoted to sales manager in March 1993.

---

## API Reference

### Excel Formatting Features

- **Font Styling**: Fonts like Tahoma are used to enhance readability.
- **Alignment**: Proper alignment ensures a polished appearance.
- **Number Formatting**: Custom formats are applied to handle monetary values and dates.
- **Image Integration**: Profile photos can be inserted to personalize the resume.

---

## Code Examples

### Excel Document Setup Example

```csharp
// Example: Setting up the Excel document for employee profile
using (ExcelEngine excelEngine = new ExcelEngine())
{
    IApplication application = excelEngine.Excel;
    application.DefaultVersion = ExcelVersion.Xlsx;

    // Create a new workbook
    IWorkbook workbook = application.Workbooks.Create(1);
    IWorksheet worksheet = workbook.Worksheets[0];

    // Insert employee photo
    var photo = worksheet.Pictures.Add(900, 500, "profile_photo.jpg");
    photo.left = 950;

    // Add employee details
    worksheet.Range["B9"].Text = "Name";
    worksheet.Range["F9"].Text = "Antony Jose";
    worksheet.Range["B11"].Text = "Title";
    worksheet.Range["F11"].Text = "Sales Manager";
    worksheet.Range["B13"].Text = "Birth Date";
    worksheet.Range["F13"].Text = "01/04//92";
    worksheet.Range["B15"].Text = "Hire date";
    worksheet.Range["F15"].Text = "08/30//1963";
    worksheet.Range["B17"].Text = "Home phone";
    worksheet.Range["F17"].Text = "(206) 555-3412";
    worksheet.Range["B19"].Text = "Extension";
    worksheet.Range["F19"].Text = "3355";
    worksheet.Range["B21"].Text = "Home address";
    worksheet.Range["F21"].Text = "722 Moss Bay Blvd";
    worksheet.Range["B24"].Text = "Salary";
    worksheet.Range["F24"].Text = "$50,000.00";

    // Add professional biography
    worksheet.Range["B27"].Text = "Antony Jose graduated from St. Andrews University, Scotland, with a BSC degree in 1976. Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London. He was promoted to sales manager in March 1993.";

    // Save the workbook
    workbook.SaveAs("employee_profile.xlsx");
}
```

---

## Page-level Navigation/TOC

- **Overview**
- **Content**
  - Employee Information Form
  - Professional Biography
- **API Reference**
  - Excel Formatting Features
- **Code Examples**
  - Excel Document Setup Example

---

## Cross References

- **See also**: [Essential XlsIO](#) for more advanced Excel features and formatting examples.

---

<!-- tags: [XlsIO, Excel, Resume, Formatting] keywords: [Essential XlsIO, Antony Jose, Sales Manager, Resume, Excel formatting, Custom styles] -->
```