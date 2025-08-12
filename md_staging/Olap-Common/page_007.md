```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_007.jpeg
document_name: Olap Common
page_number: 007
page_id: Olap Common#page_007
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:14:51Z
fidelity: lossless
-->

# Online Analytical Processing (OLAP)

Online Analytical Processing (OLAP) is a service that performs a real-time, multi-dimensional analysis of complex data stored in a database. The OLAP typically consists of a server component that uses specialized algorithms, indexing tools to efficiently process data mining tasks, and an OLAP client that efficiently lets you visualize the OLAP data pertaining to your business needs.

Here is how Wikipedia defines OLAP.

## ADOMD.NET

The Syncfusion OLAP controls use the **ADOMD.NET**, which is a Microsoft .NET framework provider for retrieving data from OLAP servers in the .NET platform. While ADOMD.NET primarily retrieves OLAP data from SQL Server Analysis Services (Microsoft's OLAP Server), its adherence to industry standards like XML/A allows you to access any OLAP server (SAP, SAS, Hyperion, etc.) through it and hence provides you the ability to visualize using Syncfusion OLAP control, OLAP data from myriads of data sources including Microsoft's SSAS.

## ADOMD.NET assembly and setup files information

The following assembly is required to run Syncfusion's OLAP samples:

- Microsoft.AnalysisServices.AdomdClient.dll

Install the following setup files for the above assembly:

- SQLServer2005_ADOMD.msi and SQLServer2005_ASOLEDB9.msi
- Or
- SQLSERVER2008_ASADOMD10.msi and SQLSERVER2008_ASOLEDB10.msi

These setup files can be downloaded at [Microsoft download center](https://www.microsoft.com/download-center/).

**Note:** By default, the following setup files will be installed while installing Syncfusion's Essential Studio setup for BI edition:

- SQLSERVER2008_ASADOMD10.msi
- SQLSERVER2008_ASOLEDB10.msi

## API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums), Parameters table, Returns, Exceptions.

## Code Examples (multi-language supported)
Extract ALL code exactly using fenced blocks: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python, etc.

### WinForms-specific conventions
- Distinguish between control names, namespaces, and types; prefer C# samples; treat property grids, designer steps, and menu paths as regular text.

<!-- tags: [OLAP, ADOMD.NET, Syncfusion Winforms, Multi-dimensional data analysis] keywords: [OLAP, ADOMD.NET, OLAP server, data visualization, Syncfusion controls, SQL Server Analysis Services, BI tools] -->
```