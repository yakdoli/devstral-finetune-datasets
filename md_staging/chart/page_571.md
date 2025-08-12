```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_571.jpeg
document_name: chart
page_number: 571
page_id: chart#page_571
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:47Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Sample Location

My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Chart.Windows\Samples\2.0\Import\Data from Excel

### 4.14 Exporting

Essential Chart has built-in support for exporting the chart control into various image formats. Also, using our complementary products like Essential XlsIO, DocIO and PDF you can also export the chart image into Excel, Word Doc and PDF documents.

More on this here:

#### 4.14.1 Exporting as an Image

The chart image can easily be exported as an image file in several different formats.

##### Programmatically

```csharp
[C#]
private string fileName;
fileName = Application.StartupPath + "\\chartexport";
fileName = fileName + ".gif";

this.chartControl1.SaveImage(fileName);

// Launches the file.
System.Diagnostics.Process.Start(fileName);
```

```vb.net
[VB.NET]

Private fileName As String
fileName = Application.StartupPath + "\chartexport"
fileName = fileName + ".gif"

Me.chartControl1.SaveImage(fileName)
```

---

**© 2013 Syncfusion. All rights reserved.** 571 | Page
```