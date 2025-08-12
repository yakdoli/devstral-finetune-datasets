```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_046.jpeg
document_name: HTMLUI
page_number: 046
page_id: HTMLUI#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:05:46Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

MHTML enables you to send and receive Web pages and other HTML documents by using email programs. MHTML enables you to embed images directly into the body of your email messages rather than attaching them to the message. MHTML uses MIME, which provides facilities to allow multiple objects in a single Internet email message {comma removed} to represent formatted multifont text messages, non-textual materials such as images, and so on. HTMLUI supports the usage of the simple MHTML files. The HTMLUI control allows the user to load the MHTML files from the user's drive with the help of the `LoadHTML` method.

### C# Code Example

```csharp
// LoadHTML() method for loading the mht files in HTMLUI is limited to use filenames only
// No overloads are supported.
this.htmluiControl.LoadHTML(@"C:\MyProjects\MHTSupport\sample.mht");
```

### VB.NET Code Example

```vb
' LoadHTML() method for loading the mht files in HTMLUI is limited to use filenames only
' No overloads are supported.
Me.htmluiControl.LoadHTML("C:\MyProjects\MHTSupport\sample.mht")
```

<!-- tags: [product, Syncfusion Winforms, control, HTMLUI, API, version] keywords: [MHTML, MIME, email, multifont, text messages, images, user interface, HTMLUI, LoadHTML] -->
```