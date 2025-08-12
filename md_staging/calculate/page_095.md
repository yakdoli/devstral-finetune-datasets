```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_095.jpeg
document_name: calculate
page_number: 095
page_id: calculate#page_095
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:35Z
fidelity: lossless
-->

# Essential Calculate

## 4.3.2 Using Essential XlsIO

Essential XlsIO will give you an Excel-like Automation-type support without having MS Excel installed on the host system. This means that you can use this library to read and write an XLS file and hold its contents in memory.

### Limitation

- You cannot perform actual computations on the contents of the XLS file. Essential Calculate adds this ability.

A sample which illustrates the usage of Essential XlsIO with Essential Calculate is available in the following sample installation location:

```plaintext
<Install Location>\Windows\Calculate.Windows\Samples\2.0\Xls File Using CalcEngine Demo\cs
```

In this sample, the following two classes are used:

- **ExcelRWCalcSheet**: which is derived from `CalcSheet` and implements `Syncfusion.XlsIO.IWorksheet`
- **ExcelRWWorkbook**: which is derived from `CalcWorkbook` and implements `Syncfusion.XlsIO.IWorkbook`

These classes use XlsIO library through the supported interfaces to populate a `CalcWorkbook` object from an XLS file. In addition, the derived classes use overrides to get and set the data through the XlsIO objects that holds the XLS data, instead of relying on the internal data storage that is available in `CalcSheet`. This gives us the ability to change values in the `CalcWorkbook` object and view the newly computed results. So, when you want to use an XLS file in your business objects and modify the values or get new calculated results, you can add these two classes to your project and utilize the support immediately in the same manner as this sample.

## 4.3.3 Car Insurance Sample Details

The following sample code snippet creates an XlsIO workbook from the Excel spreadsheet that was shown earlier. It creates a form that enables you to change input values for the spreadsheet, and then displays the corresponding cost of insurance for these input values.

Given below is the code from the Form.Load event handler.

```csharp
[C#]
private ExcelRWCalcWorkbook calcWB;
```

<!-- tags: [syncfusion, windows forms, xlsio, calculate, car insurance sample] keywords: [essential xlsio, excel-like automation, calcengine demo, business objects, computed results, derived classes, form.load event] -->
```