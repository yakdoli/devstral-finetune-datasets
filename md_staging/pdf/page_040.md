```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: pdf
page_number: 040
page_id: pdf#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:25:42Z
fidelity: lossless
-->

# Essential PDF

## Overview

- Describes steps to deploy and use Essentia PDF components in an ASP.NET application.
- Lists required dependent assemblies for deployment.
- Provides code snippet for creating and adding pages to a PDF document.

## Content

### Deployment Configuration

```xml
<configuration>
  <system.web>
    <compilation>
      <assemblies>
        <add assembly="Syncfusion.Pdf.Base, Version=x.x.x, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89"/>
      </assemblies>
    </compilation>
  </system.web>
</configuration>
```

> Note: The version number represented by x.x.x in the above code will vary depending on the version you are linking to.

### Data File Permissions

1. **Data Files:** If you have .xml, .mdb, or other data files, ensure that they have sufficient security permission.
   - Authenticated users should have full control over the files and the directories in order to give ASP.NET code, enough permissions to open the file during runtime.

Refer to the document in the following path, for step by step process of Syncfusion assemblies deployment in ASP.NET.

```plaintext
http://www.syncfusion.com/support/user/uploads/webdeployment_c883f681.pdf
```

### Dependent Assemblies

> Note: Application with Essential PDF needs following dependent assemblies for deployment.

- **Syncfusion.Core.dll**
- **Syncfusion.Compression.Base.dll**
- **Syncfusion.Pdf.Base.dll**

### Result of Deployment

Essential PDF is now deployed in your ASP.NET application.

### Creating and Adding PDF Pages

#### Create and add a PDF document with pages to the application

The following code snippet will guide you to create and add PDF document to this application:

```csharp
[Publish]

// Create a new document.
PdfDocument doc = new PdfDocument();

// Add a page
PdfPage page = doc.Pages.Add();
```

## API Reference

### Code Examples

Example of creating a new PDF document and adding a page.

```csharp
[Publish]

// Create a new document.
PdfDocument doc = new PdfDocument();

// Add a page
PdfPage page = doc.Pages.Add();
```

## Cross References

See also: [Deployment of Syncfusion ASP.NET Assemblies](http://www.syncfusion.com/support/user/uploads/webdeployment_c883f681.pdf)

## Additional Notes

Ensure that all required permissions and configurations are set correctly to successfully integrate and deploy Syncfusion Essential PDF components in your application.

<!-- tags: [syncfusion-essentialpdf, asp.net-deployment, pdf-generation, winforms, version 11.4.0.26] keywords: [Essential PDF, Syncfusion, ASP.NET, deployment, data files, permission, code snippet, PDF document, pages, assemblies] -->
```