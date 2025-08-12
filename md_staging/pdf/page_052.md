```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_052.jpeg
document_name: pdf
page_number: 052
page_id: pdf#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:24Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Add a Button to the aspx page in View.
- Create a custom ActionResult to handle PDF generation.
- Implement the logic to generate and serve the PDF file.

## Content

### Step 1: Add a Button to the aspx Page

To create a button on the aspx page, use the following code:

```aspx
[ASPX]
<% Html.BeginForm("HelloWorld", "GettingStarted", FormMethod.Post); 
{
  <input type="submit" value="Create PDF" />
<% Html.EndForm(); 
}
```

### Step 2: Create Custom ActionResult

In an MVC application, a controller action returns an action result. In particular, it returns an action that derives from the base `ActionResult` class.

However, if you want to return some other type of content to a browser, such as an image, a PDF file, or a Microsoft Excel document, you need to create your own action result. The following code example illustrates how to create a custom action result.

#### C# Code Example

```csharp
[C#]
public class PdfResult : ActionResult
{
    private string m_filename;
    private PdfDocument m_pdfDocument;
    private PdfLoadedDocument m_pdfLoadedDocument;
    private HttpResponse m_response;
    private HttpReadType m_readType;

    public string FileName
    {
        get
        {
            return m_filename;
        }
        set
        {
            m_filename = value;
        }
    }

    public PdfDocument PdfDoc
    {
```

## API Reference (if applicable)
- **Class**: `PdfResult`
  - **Properties**:
    - `FileName`: Gets or sets the name of the PDF file.
    - `PdfDoc`: Represents the PDF document.

## Code Examples (multi-language supported)
- The above C# code demonstrates how to create a custom `PdfResult` class that inherits from `ActionResult`, enabling the generation and return of PDF content.

<!-- tags: [syncfusion, mvc, pdf, actionresult, custom actionresult, pdf generation] keywords: [actionresult, pdf, custom actionresult, pdf generation, mvc, aspx, button] -->
```