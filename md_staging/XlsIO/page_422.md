```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_422.jpeg
document_name: XlsIO
page_number: 422
page_id: XlsIO#page_422
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:14:51Z
fidelity: lossless
-->

### Using Add-In Functions in XlsIO

```vb
[VB.NET]

Dim unknownFunctions As IAddInFunctions = workbook.AddInFunctions
unknownFunctions.Add("c:\blp\api\dde\blp.xla", "blp")

' Use the Function.
sheet.Range("A3").Formula = "blp(A1+"" CORP"",""PX_LAST"")"
```

**Note:** If you move the file to another computer, or distribute it, the workbook will expect to find the same Add-In, in the same place, on their computers. But, if the Add-In is moved or deleted from the computer, the workbook won't be able to find it, and your code won't work. Make sure that the Add-In is accessed by locating the .xla file through the Tools menu (Tools -> Addins -> Browse).

## API Reference

- **Namespace:** Microsoft.Office.Interop.Excel
- **Class:** IAddInFunctions
- **Method:** Add()
  - **Parameters:**
    - **Path (String):** The file path of the Add-In.
    - **FunctionName (String):** The name of the function to be added.
  - **Returns:** None.
  - **Description:** Adds a custom function from the specified Add-In to the workbook.

## Code Examples

### Example: Adding and Using a Custom Function

This example demonstrates how to add a custom function from a .xla file and use it in your workbook.

```vb
' Adding the Add-In function
Dim unknownFunctions As IAddInFunctions = workbook.AddInFunctions
unknownFunctions.Add("c:\blp\api\dde\blp.xla", "blp")

' Using the custom function in a cell
sheet.Range("A3").Formula = "blp(A1+"" CORP"",""PX_LAST"")"
```

### Example: Dynamic Function Addition

You can add multiple functions from the same or different Add-Ins dynamically based on requirements.

```vb
Dim unknownFunctions As IAddInFunctions = workbook.AddInFunctions
unknownFunctions.Add("c:\path\to\add-in.xla", "functionName1")
unknownFunctions.Add("c:\another\path\xla", "functionName2")

' Use the functions in different cells
sheet.Range("B3").Formula = "functionName1(A1)"
sheet.Range("C3").Formula = "functionName2(B1)"
```

## Cross References

- For more information on managing Add-Ins in Excel, see [Manage Excel Add-Ins](#).
- For detailed documentation on the `IAddInFunctions` API, refer to the [Microsoft Office Interop API documentation](#).

<!-- tags: [xlsio, add-ins, custom-functions, vba, vb.net, workbook] keywords: [add-in functions, excel, ms office, vba, formula, custom functions, xla] -->
```