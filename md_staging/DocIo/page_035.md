```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: DocIo
page_number: 035
page_id: DocIo#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:13Z
fidelity: lossless
-->

## Essential DocIO

### Overview
- This section discusses deploying Essential DocIO in an ASP.NET application and creating Word documents.

### Content

#### 3.3.2 ASP.NET

Now, you have created an ASP.NET application (refer to **Creating Platform Application**). This section covers the following:

- Deploying Essential DocIO in an ASP.NET Application
- Creating a Word Document

#### Deploying Essential DocIO in an ASP.NET Application

This section provides information and instructions for deploying ASP.NET applications that use Essential DocIO for ASP.NET. This is in addition to the section on Deploying Essential Studio for ASP.NET (**Common-->Deploying Essential Studio for ASP.NET**) in the Getting Started Guide.

Essential DocIO ships with .NET Framework 2.0 (Visual Studio 2005) version of the C# and VB.NET samples, which are installed beneath 2.0 directories. During installation, application directories are created in IIS for each of the C# and VB.NET samples.

Web application by default is deployed in full trust mode.

#### Deploying in Medium Trust or Partial Trust Scenarios

There are two such scenarios in which Syncfusion assemblies might be deployed.

##### Example 1

If the Syncfusion Assemblies are in GAC (Global Assembly Cache), and the Web Application is running in medium trust, then the Syncfusion assemblies actually runs in full trust. Hence this scenario is fully supported and there are no additional steps necessary for deployment.

##### Example 2

Say, the Syncfusion Assemblies are present in the application's bin folder and the Web Application is running in medium trust, then the Syncfusion assemblies will run in medium trust.

Essential DocIO allows to work in medium trust by using following assemblies:

- Syncfusion.Core.dll
- Syncfusion.Compression.Base.dll
- Syncfusion.DocIO.Web.dll

<!-- tags: [Syncfusion Winforms, Essential DocIO, ASP.NET, medium trust, deployment] keywords: [Essential DocIO, ASP.NET, Web application, full trust, medium trust, Syncfusion assemblies, .NET Framework 2.0, GAC, Global Assembly Cache, IIS, deployment scenarios, C#, VB.NET, application directories, getting started guide, DocumentIO, Word Document] -->
```