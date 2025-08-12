```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_434.jpeg
document_name: XlsIO
page_number: 434
page_id: XlsIO#page_434
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:33Z
fidelity: lossless
-->

## Essential XlsIO

```csharp
workbook.SaveAs("Sample.xlsm", ExcelSaveType.SaveAsTemplate);
```

```vbnet
' Open an existing XLTM file.
workbook = application.Workbooks.Open("MacroTemplate.xlsm", ExcelOpenType.Automatic)

' Save the file as XLSM.
workbook.Version = ExcelVersion.Excel2007
workbook.SaveAs("Sample.xlsm", ExcelSaveType.SaveAsTemplate)
```

### 5.1.18 How to Create Template Markers Using XlsIO?

Report created in Excel provides ordered and rich look for large datasets. This article focuses on creating an Excel report using template markers. A template marker is a special marker symbol created in an Excel template which will be bound the required user data. Essential XlsIO allows you to create and bind the template markers to data from various sources, such as data table, variables and arrays. This allows the user to control the data formats for the data bound to the template document.

#### How Does it Work?

Markers are applied in the template to the required cells. This will include the data source name and field name of interest. During data binding a search is conducted for the data source name and the field name in the Excel workbook and the corresponding data from the data source is bound to the marker. Cells in the worksheet can be filled with single data source or with multiple records. Format of these data can be changed using the arguments of the markers.

#### What is the Syntax of the Markers in Template?

Each marker starts with some prefix (by default it is “%” character) and followed by the variable name and properties. There could be several arguments after a variable which are delimited by some character (by default it is semicolon “;”).

![Figure 164: Marker Syntax](https://i.imgur.com/example.png)

#### What are the Various Sources of Binding Data to Markers?
```


<!-- tags: [XlsIO, Winforms, Excel report, template markers, data binding, data sources] keywords: [template markers, data binding, Essential XlsIO, Excel template, data source, field name, marker syntax, template markers in Excel, Excel report ] -->
```