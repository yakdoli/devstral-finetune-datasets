```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_110.jpeg
document_name: Olap Common
page_number: 110
page_id: Olap Common#page_110
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:26Z
fidelity: lossless
-->

# Essential OlapCommon

## 5.24 Edit MDX Query before Its Execution

MDX Query can be edited before its execution to retrieve the CellSet through handling the BeforeMdxQueryExecute event of OlapDataManager. The following code example illustrates this.

### C#

```csharp
olapDataManager.BeforeMdxQueryExecute += new QueryExecuteEventHandler(olapDataManager_BeforeMdxQueryExecute);

void olapDataManager_BeforeMdxQueryExecute(object sender, QueryExecutingEventArgs e)
{
    e.MdxQuery = "Edit MDX query here";
}
```

### VB

```vb
Private olapDataManager.BeforeMdxQueryExecute += New QueryExecuteEventHandler(AddressOf olapDataManager_BeforeMdxQueryExecute)

Private Sub olapDataManager_BeforeMdxQueryExecute(ByVal sender As Object, ByVal e As QueryExecutingEventArgs)
    e.MdxQuery = "Edit MDX query here"
End Sub
```

## 5.25 Host BI Silverlight component in ASP.NET MVC Web Project

This section explains how to add the Silverlight components in an MVC project:

1. Open Visual Studio IDE.
2. Go to File → New → Project and create a new Silverlight application.

A dialog window opens as shown below:
```html
© 2013 Syncfusion. All rights reserved. 110 | Page
```
<!-- tags: [olapcommon, mdxquery, olapidatamanager, silverlight, asp.net mvc, tutorial, event handling, code examples, visual studio, mvc project setup] keywords: [mdxquery, olapidatamanager, silverlight, mvc, olapcommon, event, handler, tutorial] -->
```