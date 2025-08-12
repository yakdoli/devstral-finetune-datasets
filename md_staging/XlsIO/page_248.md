```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_248.jpeg
document_name: XlsIO
page_number: 248
page_id: XlsIO#page_248
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:06:09Z
fidelity: lossless
-->

### Links

**Overview**

- This section explains how to create and manage hyperlinks within an Excel workbook using the **Insert Hyperlink** feature. Key functionalities include linking to other places in the workbook, files, web pages, and email addresses, all of which can be customized with text and tooltips.

**Content**

A hyperlink is a convenient way to allow the user of a workbook to instantly access another place in the workbook, or another workbook, or a file associated with another application. A hyperlink can be inserted in a cell or a shape in Excel. Select the cell or shape, and select Hyperlink from the Insert menu, or right-click anywhere in the cell or shape, and then select Hyperlink from the pop-up menu. You can enter a cell reference in the current workbook, browse to another workbook, a different file, or a web page, and even enter an email address and subject line. You can also edit the text for a hyperlink in a cell.

Following is the Insert Hyperlink dialog box of MS Excel that allows to set various hyperlinks.

![](https://i.imgur.com/1337.png)

**Figure 84: Inserting Hyperlink**

XlsIO provides support to set the following types of hyperlinks with the **Type** and **Address** properties of the **IHyperlink** interface.

- Hyperlink to a Worksheet Range
- Hyperlink to Website
- Hyperlink to e-mail
- Hyperlink to external files

You can also set the text to be displayed in a hyperlink, and a tooltip that shows the purpose of the link, by using the **TextToDisplay** and **ScreenTip** properties.

Following code example illustrates how to insert various hyperlinks.

## References

- Relevant APIs: `IHyperlink`, `TextToDisplay`, `ScreenTip`
- Screenshots: **Figure 84: Inserting Hyperlink**

<!-- tags: [XlsIO, hyperlinks, Excel, Insert Hyperlink, IHyperlink, WINFORMS, 11.4.0.26] keywords: [hyperlinks, Excel, cell reference, external files, web pages, email addresses, hyperlink properties, XlsIO, Insert Hyperlink, IHyperlink] -->
```