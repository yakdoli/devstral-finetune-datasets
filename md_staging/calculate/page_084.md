```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_084.jpeg
document_name: calculate
page_number: 084
page_id: calculate#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:43Z
fidelity: lossless
-->

# Essential Calculate

```vb
engine = New Syncfusion.Calculate.CalcEngine(Me.dataGrid1)

' 4) Track dependencies required for auto calculations.
engine.UseDependencies = True

' 5) Register multiple ICalcData objects for cross sheet references.
Dim sheetfamilyID As Integer = CalcEngine.CreateSheetFamilyID()
engine.RegisterGridAsSheet("DG1", Me.dataGrid1, sheetfamilyID)
engine.RegisterGridAsSheet("DG2", Me.dataGrid2, sheetfamilyID)
engine.RegisterGridAsSheet("DG3", Me.dataGrid3, sheetfamilyID)
engine.RegisterGridAsSheet("DG4", Me.dataGrid4, sheetfamilyID)
engine.RegisterGridAsSheet("DG5", Me.dataGrid5, sheetfamilyID)

' DataGridWorkBookForm_Load
End Sub
```

The following is an explanation of the preceding code.

1. Assign the datasources to the DataGrids.
2. **ResetSheetFamilyID** clears any static members of the CalcEngine class and sets the engine state to operate with a single ICalcData object.
3. Creates an instance of the CalcEngine object.
4. Sets the engine object to track calculation dependencies so that cells can be automatically updated as other cell values change.
5. This is the code that registers a name for each ICalcData object so that the CalcEngine can support references across ICalcData objects.

## 4.1.2.3 Conventions

There are two conventions that are honored by Essential Calculate. While processing strings that are used as data values, any string beginning with `"="` is treated as a formula that is to be parsed and evaluated. You can change the `"="` to some other character by setting this static (Shared in VB) member, CalcEngine.FormulaCharacter. If you call Parse routines directly from code, the FormulaCharacter is optional.
```


<!-- tags: [product, Syncfusion Winforms, module, control, calcengine, version: 11.4.0.26] keywords: [CalcEngine, ICalcData, sheetfamilyID, dependence tracking, cross sheet references, Conventions, FormulaCharacter] -->
```