```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: HTMLUI
page_number: 036
page_id: HTMLUI#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:04:38Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## 4.1.2.1 Loading the File From Disk

The HTML file that is located in the user's disk can be loaded into the HTMLUIControl. It is loaded by specifying the location of the file in the disk.

### [C#]

```csharp
// Load the specified HTML Document from user's drive.
string filepath = @"C:\MyProjects\LoadHTML\FromDisk.htm";
this.htmluiControl1.LoadHTML(filepath);
```

### [VB.NET]

```vbnet
' Load the specified HTML Document from user's drive.
Private filepath As String = "C:\MyProjects\LoadHTML\FromDisk.htm"
Me.HtmluiControl1.LoadHTML(filepath)
```

The following image shows file loaded from the User's Drive.

![](https://raw.githubusercontent.com/llissued-datasets/llm-rag-datasets/main/images/image_3.png)

**Figure 15**: Loading HTML document from the User's Drive into the HTMLUI Control

## Page-level Navigation/TOC (if applicable)
- [unclear]
  
<!-- tags: [HTMLUI, Windows Forms, HTML, File Loading, LoadHTML] keywords: [HTMLUIControl, C#, VB.NET, File Path, User's Drive, Loading Files] -->
```