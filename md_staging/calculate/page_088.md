```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_088.jpeg
document_name: calculate
page_number: 088
page_id: calculate#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:56Z
fidelity: lossless
-->

# Essential Calculate

event whenever a data value changes. WireParentObject is a callback method from CalcEngine which gives the ICalcData object a chance to do whatever it needs to initially set up this notification process. In this particular case, this means subscribing to the DataTable.ColumnChanged event whose event handler will raise the required ValueChanged event. These type of actions cannot be done in the ICalcData constructor as the data source of the DataGrid would not have been set at this point. Using the WireParentObject callback, enables the DataGrid to have things completely set up before the WireParentObject is triggered when the CalcEngine is created.

2. This is the DataTable.ColumnChanged event handler. Its purpose is to raise the ICalcData.ValueChanged event. It uses the CurrencyManager to retrieve the row position of the changed row, and looks up the changed column in the Columns collection. One point to note is that both these values are zero-based indexes. Anytime you interact with an ICalcData object, the indexes have to be one-based. So, when the ValueChangedEventArgs are created, the indexes are incremented by one.

3. This GetValueRowCol implementation returns the value in the DataGrid for a certain row and column index, which are passed in by the caller. These values must be one-based in the call list. So, before they are used to retrieve the value from the DataGrid, they are decremented to be proper zero-based indexes on the DataGrid.

4. This SetValueRowCol implementation sets the value in the DataGrid for a certain row and column index, which are passed in by the caller. Again the row and column indexes are adjusted for the base difference.

5. This is the declaration of the ValueChanged event that was raised in the ColumnChanged event discussed in item two.

## 4.2 Web Control Performance

Syncfusion Essential studio makes use of the class named ScriptResourceAttribute which is used to define a resource in an assembly to be used from a client script file.

Then the resource files which are all used in the Syncfusion controls are gzipped and served over the network. The following screenshot shows this.

<!-- tags: [winforms, syncfusion, datatable, columnchanged, datachanged, valuechanged, currencymanager, webcontrol, performancetuning, calculationengine, essentialstudio, scriptingresources] keywords: [datatable, syncfusion, winforms, datachanged, scriptresourceattribute, gzipped, syncfusioncontrol, performance, calculation, essentialstudio, scriptingresources] -->
```