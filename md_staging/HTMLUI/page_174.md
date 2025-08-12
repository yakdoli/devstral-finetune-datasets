```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_174.jpeg
document_name: HTMLUI
page_number: 174
page_id: HTMLUI#page_174
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:13:55Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

### Loading HTML from an URL

```csharp
using System.Net;

Uri uri = new Uri("http://www.syncfusion.com");
HtmluiControl.LoadHTML(uri);
```

```vb.net
Imports System.Net

Private uri As Uri = New Uri("http://www.syncfusion.com")
HtmluiControl1.LoadHTML(uri)
```

### Loading HTML from a String

```csharp
string htmlCode ="<HTML><HEAD><TITLE>HI</TITLE></HEAD><BODY bgcolor='#ffffff'><INPUT type='button' id='btn'/></INPUT></BODY></HTML>";
this.htmluiControl1.LoadFromString(htmlCode);
```

```vb.net
Private htmlCode As String = "<HTML><HEAD><TITLE>HI</TITLE></HEAD><BODY bgcolor='#ffffff'><INPUT type='button' id='btn'/></INPUT></BODY></HTML>"
Me.HtmluiControl1.LoadFromString(htmlCode)
```

### Loading a HTML File as an Embedded Resource

To load a HTML file as an embedded resource, follow these steps:

1. Add an HTML file as an Embedded Resource to the application.
2. Set its **BuildAction** as Embedded Resource.
3. Include the following code snippet.

#### Code Snippet for C#
```csharp
Stream htmlStream =
    (Stream)Assembly.GetExecutingAssembly().GetManifestResourceStream("LoadingFileFromResource.resfile.htm");
this.htmluiControl1.LoadHTML(htmlStream);
```

#### Code Snippet for VB.NET
```vb.net
Private htmlStream As Stream =
    CType(System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream("LoadingFileFromResource.resfile.htm"), Stream)
Me.HtmluiControl1.LoadHTML(htmlStream)
```

---
  
<!-- tags: [Syncfusion Winforms, HTMLUI, Embedded Resources, HTML Loading, C#, VB.NET] keywords: [LoadHTML, LoadFromString, Embedded Resource, BuildAction, URI, HTML code, Stream] -->
```