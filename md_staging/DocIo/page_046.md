```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_046.jpeg
document_name: DocIo
page_number: 046
page_id: DocIo#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:36Z
fidelity: lossless
-->

# Essential DocIO

```xml
<namespaces>
    ....
    <add namespace="Syncfusion.DocIO.Base"/>
</namespaces>
```

Essential DocIO is now deployed in your ASP.NET MVC application.

## Creating a Word document in an ASP.NET MVC Application

The following steps illustrate how to create a Word document in an MVC application.

### Step 1: View

Add a Button to the aspx page in View as follows.

#### [ASPX]

```html
<% Html.BeginForm("HelloWorld", "GettingStarted", FormMethod.Post); %>
{
    <table width="400px">
        <tr>
            <td align="left" width="100%" cellpadding="0" cellspacing="0" border="0">
                <input type="checkbox" name="Browser" style="font-size:12px; font:Trebuchet MS" value="Browser" /> Open Document inside Browser
            </td>
            <td align="right">
                <input type="submit" style="margin-right: 3px; height:27px; font-size:12px; font:Trebuchet MS" value="Create PDF" />
            </td>
        </tr>
    </table>
<% Html.EndForm(); %>
}
```

- `Html.BeginForm("HelloWorld", "GettingStarted", FormMethod.Post)` represents the `Form` tag. When the form is submitted, the "HelloWorld" action in the "GettingStartedController" gets invoked.
- `HelloWorld` represents an Action.
- `GettingStarted` represents a controller.

### Step 2: Create Custom ActionResult
```html
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [Essential DocIO, ASP.NET MVC, Word document creation, HelloWorld, GettingStarted, Custom ActionResult] keywords: [Essential DocIO, ASP.NET MVC, Word document, form submission, controller action, checkbox, submit button, Create PDF] -->
```