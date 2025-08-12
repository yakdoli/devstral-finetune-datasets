```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_303.jpeg
document_name: DocIo
page_number: 303
page_id: DocIo#page_303
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:47:27Z
fidelity: lossless
-->

# Exporting Header and Footer

## Overview
- Header and Footer in a Word document are useful for placing specific information that is consistently displayed on every page.
- These headers and footers can be exported to an EPub document so that only the first section header appears at the top of the document and the first section footer appears at the end.
- The feature is controlled by turning on the `HtmlExportHeadersFooters` property, which is set to `true` by default.

## Content

### Exporting Header and Footer

**Description:**
Header and Footer in the Word document are helpful in placing specific information that has to be displayed on every page. These headers and footers can be exported to the EPub document in such a way that only the first section header would appear at the top of the document and the first section footer would appear at the end of the document. This can be done by turning on `HtmlExportHeadersFooters` property. By default, this property is set to true and hence it always exports header and footer.

#### Code Illustration

The following code illustrates how to export header and footer.

```csharp
[C#]

// Load any .doc or .docx file
WordDocument document = new WordDocument(filename);
```

## References

- Syncfusion Fax Order Form
- Product suites: Essential Studio, Essential Studio User Interface, Essential Studio Enterprise, Essential Studio Reporting, Essential Studio Business Intelligence, Individual products and Product subscriptions
- Platforms Supported: ASP.NET, Windows Forms, WPF, Silverlight, ASP.NET MVC

## Contact Information

If you have any questions, please contact `sales@syncfusion.com` or call at 1-888-9DOTNET (US only) or 1-919-481-1974.

## Acknowledgment

We appreciate your business and look forward to exceeding your expectations of service.

*Syncfusion, Inc.*

Page 303 | © 2013 Syncfusion. All rights reserved.
<!-- tags: [WinForms, EPub, HeaderFooterExport, WordDocument, SyncfusionWinforms, EssentialStudio, UserInterface, Enterprise, Reporting, BusinessIntelligence, IndividualProducts, EPubExport, HtmlExportHeadersFooters] keywords: [header, footer, word document, EPub, export, section header, section footer, default property, first section header, first section footer, contact, sales, Syncfusion, 2013, All rights reserved] -->
```