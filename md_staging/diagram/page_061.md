```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: diagram
page_number: 061
page_id: diagram#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:11:26Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

```csharp
dlgHF.Header = diagram1.Model.HeaderFooterData.Header;
dlgHF.Footer = diagram1.Model.HeaderFooterData.Footer;
dlgHF.MeasurementUnits = diagram1.Model.MeasurementUnits;

if (dlgHF.ShowDialog() == DialogResult.OK)
{
   diagram1.Model.HeaderFooterData.Header = dlgHF.Header;
   diagram1.Model.HeaderFooterData.Footer = dlgHF.Footer;
}
```

![Diagram Header Footer Dialog Box](https://i.imgur.com/image.jpg "Diagram Header Footer Dialog Box")

Figure 33: Diagram Header Footer Dialog Box

### 4. Print Preview

It will show a preview of the page which will appear when printed. The **Print Preview** dialog shows the preview of the page with the following:

- Page setup
- Page border set up
- Header and footers in the page

The following code snippet can be used for creating Print Preview dialog.

#### Code Example

```csharp
[C#]

if (diagram1 != null)
```

### Page-Level Navigation/TOC
- Essential Diagram for Windows Forms
  - Diagram Header Footer Dialog Box
  - Print Preview

### Cross References
- Refer to Figure 33: Diagram Header Footer Dialog Box

<!-- tags: [syncfusion-winforms, essential-diagram, print-preview, header-footer] keywords: [print preview, diagram header, footer, dialog box, page setup, page border, header footer, code snippet, C#] -->
```