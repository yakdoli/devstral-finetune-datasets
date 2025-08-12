```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: pdf
page_number: 032
page_id: pdf#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:25:16Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Creating and configuring WPF and Silverlight applications with Syncfusion components.
- Deploying Essential PDF into WPF applications.
- Steps to create a Silverlight Application in Microsoft Visual Studio.

## Content

### Creating a WPF Application

The following screenshot shows the dialog for creating a new WPF application in Visual Studio.

<figure>
![New Project dialog-WPF Application](image.png)
<figcaption>Figure 17: New Project dialog-WPF Application</figcaption>
</figure>

**Steps:**

1. A WPF application is created.  
   - Once the application is created, you will see the interface for configuring and building the application.

2. Now you need to deploy Essential PDF into this WPF application. Refer **WPF** topic for detailed info.

### Creating a Silverlight Application

**Steps:**

1. Open Microsoft Visual Studio. Go to **File** menu and click **New Project**. In the *New Project* dialog, select **Silverlight Application** template, name the project and click **OK**.

## Page-level Navigation/TOC (if applicable)
- [Getting Started](#getting-started): Overview of WPF and Silverlight applications.
- [WPF Deployment](#wpf-deployment): Detailed steps to deploy Essential PDF into a WPF application.
- [Silverlight Application Creation](#silverlight-application-creation): Steps to create a Silverlight application.

## API Reference (if applicable)
- Namespace: `Syncfusion.Windows.Forms`
- Class: `EssentialPdf`
- Methods/Properties:
  - `AddPdfViewer()`
  - `SetPdfDocument()`
  - `ExportToPdf()`

## Code Examples (multi-language supported)
```csharp
// Sample code for deploying Essential PDF in a Silverlight application
public void SetupSilverlightApplication()
{
    // Initialize the Essential PDF component
    var pdfViewer = new PdfViewer();
    pdfViewer.LoadDocument("path_to_your_pdf_file.pdf");

    // Add the viewer to the Silverlight application UI
    this.RootGrid.Children.Add(pdfViewer);
}

```

## Cross References
See also:
- WPF integration: [link to WPF topic]
- Silverlight development: [link to Silverlight reference]

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```