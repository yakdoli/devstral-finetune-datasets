```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_094.jpeg
document_name: calculate
page_number: 094
page_id: calculate#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:54Z
fidelity: lossless
-->

# Essential Calculate

Figure 41: Form interface for our Excel Workbook

![Form interface for our Excel Workbook](https://i.imgur.com/st0exiF.png)

Before learning about the actual code used in this sample to access XLS files, you need to know about a couple of classes in Essential Calculate as well as the role that Essential XlsIO will play.

## 4.3.1 CalcSheet and CalcWorkbook Classes

In the Adding Calculation Support section, you would have learnt how to support referencing multiple `ICalcData` objects in a workbook fashion. The technique used there relies on registering each `ICalcData` object directly with a single instance of the `CalcEngine`. Different `ICalcData` objects are managed by tying together in a Tab Control as the Tab Pages. To support a general workbook structure where there are no support objects like Tab Pages and Tab Controls to provide the links, the Essential Calculate library includes two classes: `CalcSheet` and `CalcWorkbook`.

- The `CalcSheet` class is an `ICalcData` derived object that plays the role of a single worksheet.
- It does have the optional facility to hold row/column type data objects that can be set through indexing an instance of the class.
- This class will allocate storage to hold such data.
- The `CalcWorkbook` class is a collection of `CalcSheets`.
- You can use these classes to manage the support for working with Excel spreadsheets.

> **Note:** For more detailed information on these classes, check out the class reference.

## Page-level Navigation/TOC (if applicable)
_Not applicable on this page._

## Cross References
_Not applicable on this page._

<!-- tags: [Essential Calculate, CalcSheet, CalcWorkbook, ICalcData, CalcEngine, XlsIO, workbook, worksheet, Excel spreadsheets, Syncfusion Winforms, 11.4.0.26] keywords: [calculation support, workbook structure, Excel files, interface, library, class reference, detailed information] -->
```