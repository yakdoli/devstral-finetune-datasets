```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_055.jpeg
document_name: XlsIO
page_number: 055
page_id: XlsIO#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:51:34Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Guide to deploying and using Essential XlsIO in an ASP.NET MVC application.
- Instructions for creating an Excel document with worksheets.

## Content

### Deployment of Essential XlsIO

1. **Note**: X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.
2. Add the following under the `<namespaces>` tag of Web.config file.

#### Web.config Configuration
```xml
<namespaces>
    ....
    <add namespace="Syncfusion.XlsIO"/>
</namespaces>
```

Essential XlsIO is now deployed in your ASP.NET MVC application.

### Creating and Adding an Excel Document (With Worksheets) to the Application

The following steps illustrate how to create a worksheet in an MVC application.

#### Step 1: View

Add a `Button` to the aspx page in the View, as illustrated by the following code:

```aspx
[ASPX]
<% Html.BeginForm("createsheet", "GettingStarted", FormMethod.Post);
    %>
<input type="submit" value="Create Document" />
<% 
    Html.EndForm(); 
%>
```

#### Step 2: Create a Custom ActionResult Class

In an MVC application, the controller returns an action result. In particular, it returns an action that derives from the base `ActionResult` class. 

But, if you want to return some other type of content to a browser, such as an image, a XlsIO file, or a Microsoft Excel document, you need to create your own action result. The following code example illustrates how to create a custom action result:

```csharp
public class ExcelActionResult : ActionResult
{
    public override void ExecuteResult(ControllerContext context)
    {
        // Implementation for custom result (e.g., creating and returning an Excel file)
    }
}
```

## API Reference

Refer to the official Syncfusion documentation for more information on `Syncfusion.XlsIO` namespace and its features.

## Code Examples

The provided code examples demonstrate how to integrate `Syncfusion.XlsIO` into an MVC application to create and manipulate Excel documents.

## Cross References

See also:
- Essential XlsIO documentation for more detailed examples and usage cases.
- Syncfusion's official documentation for further information on custom action results in MVC.

<!-- tags: [Essential XlsIO, MVC, ActionResults, Excel, Syncfusion.Winforms, version 11.4.0.26] keywords: [worksheet, Excel, deployment, action result, custom, Web.config, namespaces, controller, ASP.NET MVC, integration] -->
```