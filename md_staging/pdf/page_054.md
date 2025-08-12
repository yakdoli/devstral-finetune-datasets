```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_054.jpeg
document_name: pdf
page_number: 054
page_id: pdf#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:50Z
fidelity: lossless
 -->

## Overview

- A concise guide on implementing custom ActionResult classes for handling PDF export actions
- Focus on creating custom action result classes that inherit from ActionResult to stream PDF documents to the browser
- Explanation of creating an extension method to export PDF documents from controllers

## Content

### Creating a Custom ActionResult for PDF Export

Every action result must inherit from the base **`ActionResult`** class. The base **`ActionResult`** class has one method that you must implement: the **`ExecuteResult`** method. The **`ExecuteResult`** method is called to generate the content created by the action result. This method streams the output Word document file to the browser.

Here is a sample implementation of a custom ActionResult class for PDF export:

```csharp
public class PdfResult : ActionResult
{
    private IPdfDocument m_pdfDocument;
    private IPdfLoadedDocument m_pdfLoadedDocument;
    private string FileName;
    private HttpResponse m_response;
    private HttpReadType ReadType;

    public PdfResult(IPdfLoadedDocument pdfLoadedDocument, HttpResponse response, HttpReadType type)
    {
        this.m_pdfDocument = null;
        this.m_pdfLoadedDocument = pdfLoadedDocument;
        this.FileName = filename;
        this.m_response = response;
        this.ReadType = type;
    }

    public override void ExecuteResult(ControllerContext context)
    {
        if (context == null)
            return;
        if (pdfLoadedDoc != null)
            this.pdfLoadedDoc.Save(FileName, Response, ReadType);
        if (PdfDoc != null)
            this.PdfDoc.Save(FileName, Response, ReadType);
    }
}
```

#### Explanation of the Code

- **`PdfResult`**: A custom ActionResult class for handling PDF export.
- **Fields**:
  - `m_pdfDocument`: Represents the PDF document to be saved.
  - `m_pdfLoadedDocument`: Represents the loaded PDF document.
  - `FileName`: The name of the file to be saved.
  - `m_response`: The HttpResponse object to write the PDF content to.
  - `ReadType`: The type of reading operation for the PDF document.
  
- **Constructor**: Initializes the fields with the provided parameters.
- **`ExecuteResult` Method**: Implements the logic to save the PDF document to the response stream.

### Returning Action Results from Controllers

A controller action cannot return an action result directly. For example, if you want to return a view from a controller action, you don't return a **`ViewResult`**. Instead, you call the **`View`** method. The **`View`** method instantiates a new **`ViewResult`** and returns the new **`ViewResult`** to the browser.

### Creating an Extension Method for Export

An extension method named **`ExportAsActionResult`** has to be created to add the **`Controller`** class. The **`ExportAsActionResult`** method returns a **`PdfResult`**.

#### Example of Using the Extension Method

Here is an example of adding an extension method to the **`Controller`** class:

```csharp
public static class ControllerExtensions
{
    public static PdfResult ExportAsActionResult(this Controller controller, string fileName, HttpReadType readType)
    {
        var pdfLoadedDoc = controller.pdfDocument.Load(); // Replace with actual loading logic
        return new PdfResult(pdfLoadedDoc, controller.HttpContext.Response, readType);
    }
}
```

### ASPX Example of PDF Export Form

Below is an example of an HTML form in ASPX for creating and submitting a PDF creation form:

```aspx
[ASPX]
<%
    Html.BeginForm("HelloWorld", "GettingStarted", FormMethod.Post);
    {
        %> 
        <table width="400px">
            <tr>
                <td align="left" width="100%" cellpadding="0" cellspacing="0" border="0">
                    <input type="checkbox" name="Browser" style="font-size:12px; font:Trebuchet MS" value="Browser" /> Open Document inside Browser
                </td>
                <td align="right">
                    <input type="submit" style="margin-right: 3px; height:27px; font-size:12px; font:Trebuchet MS" value="Create PDF" />
                </td>
            </tr>
        </table>
    %}
%>
```

### Conclusion

This guide showcases how to create custom **`ActionResult`** classes to handle PDF export functionality in a web application. It includes the creation of a custom **`PdfResult`** class, the implementation of the **`ExecuteResult`** method, and the addition of an extension method to the **`Controller`** class for exporting PDFs.

## API Reference

### Classes

- **`PdfResult`**: Inherits from **`ActionResult`** and implements the **`ExecuteResult`** method to handle PDF document streaming.
  
### Methods

- **`ExportAsActionResult`**: An extension method added to the **`Controller`** class to return a **`PdfResult`**.

## Code Examples

- **C# Example of Custom ActionResult**: The implementation of the **`PdfResult`** class, including the constructor and **`ExecuteResult`** method.
- **ASPX Example**: The HTML form for creating and submitting a request to generate a PDF document.

## Page-level Navigation/TOC

- **Overview**: Provides a brief summary of the page scope.
- **Creating a Custom ActionResult for PDF Export**: Explains the basics and code implementation of custom ActionResult classes.
- **Returning Action Results from Controllers**: Discusses how action results are returned from controllers.
- **Creating an Extension Method for Export**: Explains the process of adding extension methods to controllers.

## Cross References

- **See also**: Related topics and references within the documentation, such as further information on **`ActionResult`** classes and **`Controller`** extensions.

<!-- tags: [Syncfusion, WinForms, PDF export, ActionResult, custom action results, extension methods] keywords: [PdfResult, ExecuteResult, ExportAsActionResult, ControllerExtensions, ASPX] -->
```
