```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_186.jpeg
document_name: edit
page_number: 186
page_id: edit#page_186
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:32Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

Me.editControl1.AllowDrop = True

## Text Export

The following topics elaborate on the exporting feature in Essential Edit:

### XML, RTF and HTML Export

Edit Control has the ability to export its contents and its associated **syntax highlighting** information into XML, RTF, or HTML formats. This allows the user to share text associated with the Edit Control along with its attributes such as syntax highlighting, line numbers, underlines, and many other useful features in universally accepted formats like XML, RTF, and HTML.

The following methods can be implemented for this purpose:

| Edit Control Method | Description |
|---------------------|-------------|
| SaveAsXML          | Export the Edit Control's contents into XML format and save it into any desired XML file. |
| SaveAsRTF          | Export the Edit Control's contents into RTF format and save it into any desired RTF file. |
| SaveAsHTML         | Export the Edit Control's contents into HTML format and save it into any desired HTML file. |

### Code Example

```csharp
// Export the Edit Control's contents into XML format and save it into a XML file.
this.editControl1.SaveAsXML("testXML.xml");

// Export the Edit Control's contents into RTF format and save it into a RTF file.
this.editControl1.SaveAsRTF("testRTF.rtf");

// Export the Edit Control's contents into HTML format and save it into a HTML file.
this.editControl1.SaveAsHTML("testHTML.html");
```

<!-- tags: [essential edit, windows forms, export, xml, rtf, html, edit control, syntax highlighting, file formats, saving] keywords: [export feature, edit control, xml export, rtf export, html export, file formats, saving files, syntax highlighting] -->
```