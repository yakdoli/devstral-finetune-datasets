```html
<!--  
source: image  
domain: syncfusion-sdk  
task: pdf-ocr-to-markdown  
language: en  
source_filename: page_048.jpeg  
document_name: chart  
page_number: 048  
page_id: chart#page_048  
product: Syncfusion Winforms  
version: 11.4.0.26  
timestamp: 2025-08-09T03:18:38Z  
fidelity: lossless  
-->  

# Essential Chart for Windows Forms  

## Content  

```csharp
return xIndex;
}  

// Indicates whether a plottable value is present at the specified point index.  
public bool GetEmpty(int index)  
{  
    return false;  
}  

// Event that should be raised by any implementation of this interface  
// if data that it holds changes. This will cause the chart to be updated accordingly. We don't raise this event in our implementation as our data will be static.  
public event ListChangedEventHandler Changed;  
}  
```  

### [VB.NET]  

```vb  
' Custom Model  
Public Class ArrayModel Implements IChartSeriesModel  
    Private data() As Double  

    Public Sub New(ByVal data() As Double)  
        Me.data = data  
    End Sub  

    ' Returns the number of points in this series.  
    Public ReadOnly Property Count() As Integer  
        Get  
            Return Me.data.GetLength(0)  
        End Get  
    End Property  

    ' Returns the Y value of the series at the specified point index.  
    Public Function GetY(ByVal xIndex As Integer) As Double()  
        Return New Double() {data(xIndex)}  
    End Function  

    ' Returns the X value of the series at the specified point index.  
    Public Function GetX(ByVal xIndex As Integer) As Double()  
        Return New Double() {xIndex}  
    End Function  

    ' Indicates whether a plottable value is present at the specified point index.  
```  

## API Reference  

### Methods  

- **GetX(Integer xIndex) As Double()**  
  Returns the X value of the series at the specified point index.  

- **GetY(Integer xIndex) As Double()**  
  Returns the Y value of the series at the specified point index.  

- **GetEmpty(Integer index) As Boolean**  
  Indicates whether a plottable value is present at the specified point index.  

## Code Examples  

### C#  
```csharp
public bool GetEmpty(int index)  
{  
    return false;  
}
```  

### VB.NET  
```vb  
Public ReadOnly Property Count() As Integer  
    Get  
        Return Me.data.GetLength(0)  
    End Get  
End Property  
```  

<!-- tags: [chart, windows forms, essential chart, data series, plottable values, point index, event handling, syncfusion winforms] keywords: [custom model, point index, data series, empty value, event] -->  
```  
