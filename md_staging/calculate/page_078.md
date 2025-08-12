<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_078.jpeg
document_name: calculate
page_number: 078
page_id: calculate#page_078
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:47Z
fidelity: lossless
-->

# Essential Calculate

Essential Calculate enables you to add calculation support to arbitrary business objects through its ICalcData interface. In this section, you will learn how to define this interface and use it with a Windows Forms DataGrid.

## 4.1.2.1 The ICalcData Interface

ICalcData has three methods and one event. This interface allows the CalcEngine class in Essential Calculate to communicate with arbitrary data sources that implement this interface.

- GetValueRowCol - Returns the data value of a specified row and column
- SetValueRowCol - Sets the data value of a specified row and column
- WireParentObject - A callback to the data object that occurs as the CalcEngine is being created. The purpose is to give the data object a chance to do any initialization steps it may need, such as subscribe to events to handle changes in data notifications.
- ValueChanged - An event that is raised whenever data changes. The ICalcData implementer raises this event when the data changes. The CalcEngine listens to this event and accordingly reacts to data changes. It is through this event that formulas are processed and dependencies are tracked by the CalcEngine.

## 4.1.2.2 Working with System.Windows.Forms.DataGrid

A Windows Forms Data Grid is a rectangular container that holds data in cells. Such a container is a natural medium for using calculation support. To add Essential Calculation support to classes that represent data in a row/column format like a Data Grid, you will have to derive the class and implement the ICalcData interface. This interface contains three methods and one event. Once you add the appropriate interface implementation, your derived object will have formula support.

The following is a discussion of using Essential Calculate with a Data Grid as an ICalcData object based on the Essential Studio\Windows\Calculation.Windows\Samples\DataGridCalculator sample that ships with the product. The sample has a derived DataGrid class that implements ICalcData. Below is a screenshot of a sample screen. The sample sets the column header text to A, B, and so on, and places 1, 2, and so on, in the first column along with random integers in the other columns. This is done to remind you of the Excel-like cell notation of A1, A2, B2, and so on. This is the notation supported by Essential Calculate formulas using ICalcData objects.

<!-- tags: [syncfusion, windows forms, data grid, calculation, icalcdata, calcengine, essenticalcalculate, version: 11.4.0.26] keywords: [data grid, calculation support, icalcdata interface, windows forms, row column format, calcengine, formula support, datagridcalculator] -->