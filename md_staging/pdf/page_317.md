```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_317.jpeg
document_name: pdf
page_number: 317
page_id: pdf#page_317
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:18Z
fidelity: lossless
-->

# Essential PDF

## Overview
- The ConvertToImage method converts the URL into an image, recognizing tables, images, lists, and similar elements.
- Supports both HTTP/HTTPS addresses and local physical paths.
- Dynamically generated documents like .asp or .aspx require HTTP invocation.

## Content

### ConvertToImage Method

The `ConvertToImage` method converts a URL into an image representation, recognizing various HTML elements such as tables, images, lists, etc. The URL parameter can be an HTTP or HTTPS address or a local physical path.

- **HTTP/HTTPS Address**: Example: `http://www.server.com/path/file.html`
- **Local Path**: Example: `c:\path\file.html`

#### Important Notes

> **Note**: If you want to open a dynamically generated document such as .asp or aspx file, you need to invoke it through HTTP even if this file is local to your own script.

#### Overloaded ConvertToImage Method

The overloaded `ConvertToImage` method allows converting an HTML page into an image while maintaining an aspect ratio, which helps prevent text truncation at the corners.

##### C#

```csharp
Image img = html.ConvertToImage("http://www.google.com", ImageType.Metafile, (int)width, -1, AspectRatio.KeepWidth);
```

##### VB.NET

```vbnet
Dim img As Image = html.ConvertToImage("http://www.google.com", ImageType.Metafile, CInt(width), -1, AspectRatio.KeepWidth)
```

#### HTML To PDF Conversion

> **Note**: HTML To PDF conversion allows text selection and search within the generated document. However, on machines where IE9 is installed, the document may contain Bitmap images that restrict text selection and search. This behavior can be altered for specific webpages by modifying the registry value. For more details, refer to the Frequently Asked Questions section.

### Authentication

You can use the `ConvertToImage` method to access authenticated web pages by passing user credential values as arguments. The following code examples illustrate this.

#### C#

```csharp
Image img = html.ConvertToImage("http://www.google.com", ImageType.Metafile, (int)width, -1, AspectRatio.KeepWidth, "UserName", "Password");
```

#### VB.NET

```vbnet
Dim img As Image = html.ConvertToImage("http://www.google.com", ImageType.Metafile, CInt(width), -1, AspectRatio.KeepWidth, "UserName", "Password")
```

## RAG Annotations
<!-- tags: [Syncfusion Winforms, ConvertToImage, Authentication, URL] keywords: [ConvertToImage, HTML To PDF, authentication, text selection, search, IE9, dynamically generated documents, .asp, .aspx, URL parameters, C#, VB.NET] -->
```