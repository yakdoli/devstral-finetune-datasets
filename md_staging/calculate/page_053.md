```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: calculate
page_number: 053
page_id: calculate#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:55Z
fidelity: lossless
-->

# Essential Calculate

Then, in the right drop-down, click each of the four items listed to add the proper code stubs.

![Figure 26: Implementing the ICalcData Interface in VB, Adding the Members](26)

After doing these steps, you will be able to see these methods in the class code. (In the C# code, the region may be collapsed.)

## C#

```csharp
public object GetValorowCol(int row, int col)
{
    // TODO: Add ArrayCalcData1.GetValorowCol implementation.
    return null;
}

public void SetValorowCol(object value, int row, int col)
{
    // TODO: Add ArrayCalcData1.SetValorowCol implementation.
}

public event Syncfusion.Calculate.ValueChangedEventHandler ValueChanged;

public void WireParentObject()
{
    // TODO: Add ArrayCalcData1.WireParentObject implementation.
}
```

## VB

```vb
Public Function GetValorowCol(ByVal row As Integer, ByVal col As Integer) _
    As Object Implements
Syncfusion.Calculate.ICalcData.GetValorowCol
End Function
```

## API Reference

### Methods

- `GetObject GetValorowCol(int row, int col):` Retrieves the value at the specified row and column.
- `void SetValorowCol(object value, int row, int col):` Sets the value at the specified row and column.

### Events

- `ValueChanged`: Triggered when a value is changed.

### Other

- `WireParentObject`: Function to wire the parent object.

### Note:

Ensure to implement the TODO sections for full functionality.

<!-- tags: [syncfusion, sdk, calculate, interface, icalcdata, visual basic, csharp] keywords: [interface implementation, arraycalcdata, valorowcol, setvalue, valuechanged, wireparentobject] -->
```