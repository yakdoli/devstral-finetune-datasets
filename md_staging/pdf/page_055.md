```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_055.jpeg
document_name: pdf
page_number: 055
page_id: pdf#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:27:25Z
fidelity: lossless
-->

# Essential PDF

```html
</td>
</tr>
</table>
<%
Html.EndForm();
%>
```

### Step 3: Controller

Add the following code in the Controller's action result.

```csharp
[C#]
public static PdfResult ExportAsActionResult(this PdfDocument PdfDoc, string filename, HttpResponse response, HttpReadType type)
{
    return new PdfResult(PdfDoc, filename, response, type);
}
```

### Step 4: Run the Application

Now try running the project by selecting **Start Debugging** option from the **Debug** menu. The following dialog box appears. It provides options to download and launch the generated file.

![Figure 24: opening Sample.pdf](https://i.imgur.com/iL28Qf7.png)

**Figure 24: opening Sample.pdf**

A PDF document is created in the ASP.NET MVC application.

### API Reference

- **Namespace**: Sync Fusion
- **Class**: PdfDocument
- **Methods**:
  - **ExportAsActionResult**
    - **Parameters**:
      - `this PdfDocument PdfDoc`: The PDF document to be exported.
      - `string filename`: The name of the PDF file.
      - `HttpResponse response`: The HTTP response object.
      - `HttpReadType type`: The type of HTTP read.
    - **Returns**: `PdfResult` - A specialized result that will process the PDF.

### Code Examples

```csharp
public static PdfResult ExportAsActionResult(this PdfDocument PdfDoc, string filename, HttpResponse response, HttpReadType type)
{
    return new PdfResult(PdfDoc, filename, response, type);
}
```

<!-- tags: [pdf, export, actionresult, asp.net mvc, winforms] keywords: [pdfdocument, pdfresult, export, controller, actionresult, syncfusion] -->
```