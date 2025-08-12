```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_398.jpeg
document_name: XlsIO
page_number: 398
page_id: XlsIO#page_398
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:13:15Z
fidelity: lossless
-->

# Essential XlsIO

## Content

### UnProtecting the Workbook

You can unprotect or remove protection for a document by entering the password in the Unprotect Workbook dialog box in MS Excel, as shown in the following screen shot.

### Figure 146: Protected Workbook

![Figure 146: Protected Workbook](https://example.com/figure146.png)

#### UnProtecting the Workbook

You can unprotect or remove protection for a document by entering the password in the Unprotect Workbook dialog box in MS Excel, as shown in the following screen shot.

### Figure 147: Unprotecting Workbook by entering Correct Password

![Figure 147: Unprotecting Workbook by entering Correct Password](https://example.com/figure147.png)

XlsIO also provides support to unprotect a workbook with password by using the `UnProtect` method.

---

## API Reference

### Methods

#### UnProtect

- **Description**: Unprotect a workbook with a password.
- **Parameters**:
  - `password`: The password used to unprotect the workbook.
- **Returns**: `bool`
  - `true` if the protection is successfully removed, otherwise `false`.
- **Exceptions**:
  - `InvalidPasswordException`: Thrown if the provided password is incorrect.

---

## Code Examples

### C#

```csharp
using Syncfusion.XlsIO;

public void UnprotectWorkbook()
{
    // Open the workbook
    using (ExcelEngine excelEngine = new ExcelEngine())
    {
        IApplication application = excelEngine.Excel;
        application.DefaultVersion = ExcelVersion.XLSX;

        // Open the protected workbook
        IWorkbook workbook = application.Workbooks.Open("ProtectedWorkbook.xlsx");

        // Unprotect the workbook
        workbook.UnProtect("syncfusion");

        // Save the unprotected workbook
        workbook.SaveAs("UnprotectedWorkbook.xlsx");

        // Close the workbook
        workbook.Close();
    }
}
```

---

## Cross References

- See also: [Protecting a Workbook](#protecting-a-workbook)

---

<!-- tags: XlsIO, workbook, password, UnProtect, Excel, MS Excel, unprotect, protect, API, version 11.4.0.26 -->
```