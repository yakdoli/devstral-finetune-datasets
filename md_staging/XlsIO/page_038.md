```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_038.jpeg
document_name: XlsIO
page_number: 038
page_id: XlsIO#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:50:23Z
fidelity: lossless
-->

## 3.3.2 ASP.NET

Now, you have created a ASP.NET application (refer to Creating a Platform Application). This section covers the following:

### Overview
- Deploying Essential XlsIO in an ASP.NET Application
- Creating and adding an Excel document (with worksheets) to the Application

### Content

#### Deploying Essential XlsIO in an ASP.NET Application

This section provides information and instructions for deploying ASP.NET applications that use Essential XlsIO for ASP.NET. This is in addition to the section on Deploying Essential Studio for ASP.NET (Common --> Deploying Essential Studio for ASP.NET) in the Getting Started guide. Essential XlsIO ships with .NET Framework 2.0 (Visual Studio 2005) version of the C# and VB.NET samples which are installed beneath 2.0 directories. During installation, application directories are created in IIS for each of the C# and VB.NET samples.

[![Computer Management](https://docs.syncfusion.com/products/images/essential_xlsio/asp-net-application.png)](https://docs.syncfusion.com/products/images/essential_xlsio/asp-net-application.png)

#### Figure: Computer Management

The image above shows the structure of the IIS application directories created for the C# and VB.NET samples, under the "Default Web Site" in the "Internet Information Services" section. The XlsIO.Web application is highlighted, indicating its location within the directory structure.

### API Reference

#### XlsIO.Web Directory

The XlsIO.Web directory contains the essential components for deploying an ASP.NET application using Essential XlsIO. It includes subdirectories and files relevant for creating and manipulating Excel documents within the application.

### Code Examples

#### Example: Creating an Excel Document Using XlsIO

```csharp
using Syncfusion.XlsIO;
using System;
using System.Web.UI;

public partial class Default : Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        // Initialize Excel engine
        ExcelEngine excelEngine = new ExcelEngine();
        IApplication application = excelEngine.Excel;

        // Add a new workbook
        IWorkbook workbook = application.Workbooks.Create(1);

        // Access the first worksheet
        IWorksheet worksheet = workbook.Worksheets[0];

        // Add data to the worksheet
        worksheet["A1"].Text = "Hello, World!";
        worksheet["A2"].Text = DateTime.Now.ToString();

        // Save the document
        string filePath = @"c:\temp\HelloWorld.xlsx";
        workbook.SaveAs(filePath);

        // Close the document
        workbook.Close();
        excelEngine.Dispose();
    }
}
```

### Cross References

See also:
- Creating a Platform Application
- Deploying Essential Studio for ASP.NET (Common --> Deploying Essential Studio for ASP.NET)
- XlsIO.Web Directory Structure

### RAG Annotations

<!-- tags: Essential XlsIO, ASP.NET, Deployment, Excel Document, C#, VB.NET, IIS, Computer Management, XlsIO.Web, Application Directories, Syncfusion Winforms keywords: deploying XlsIO, creating Excel document, worksheet, IIS, directory structure, application deployment -->

```