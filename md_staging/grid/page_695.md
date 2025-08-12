```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_695.jpeg
document_name: grid
page_number: 695
page_id: grid#page_695
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:15Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
        End If
    End Set
End Property

Sub RaisePropertyChanged(ByVal name As String)
    RaiseEvent PropertyChanged(Me, New
        PropertyChangedEventArgs(name))
End Sub

Public Event PropertyChanged As PropertyChangedEventHandler
Implements INotifyPropertyChanged.PropertyChanged

End Class
```

## Content

2. **Instantiate BindingList <T> class by specifying the type of the collection as CustomClass and add a few records into it. This will create a collection of CustomClass type objects.**

### C#

```csharp
using System.Collections.Generic;

BindingList<CustomClass> bl = new BindingList<CustomClass>();
bl.Add(new CustomClass(0101, "Charlotte", "Cooper", "49 Gilbert St.", "London"));
bl.Add(new CustomClass(0102, "Shelley", "Burke", "P.O. Box 78934", "New Orleans"));
bl.Add(new CustomClass(0103, "Regina", "Murphy", "707 Oxford Rd.", "Ann Arbor"));
bl.Add(new CustomClass(0104, "Yoshi", "Nagase", "9-8 Sekimai Musashino-shi", "Tokyo"));
bl.Add(new CustomClass(0105, "Mayumi", "Ohno", "Calle del Rosal 4", "Oviedo"));
```

### VB.NET

```vb
Imports System.Collections.Generic

Dim bl As BindingList(Of CustomClass) = New BindingList(Of CustomClass)()
bl.Add(New CustomClass(101, "Charlotte", "Cooper", "49 Gilbert St.", "London"))
bl.Add(New CustomClass(102, "Shelley", "Burke", "P.O. Box 78934", "New Orleans"))
bl.Add(New CustomClass(103, "Regina", "Murphy", "707 Oxford Rd.", "Ann Arbor"))
bl.Add(New CustomClass(104, "Yoshi", "Nagase", "9-8 Sekimai Musashino-shi", "Tokyo"))
```

## Page-level Navigation/TOC (if applicable)
- This page provides instructions on how to instantiate a `BindingList<T>` class with a specific collection type and populate it with custom records.

## Cross References
- Refer to the documentation on `CustomClass` and `BindingList<T>` for more detailed information.
- For additional resources, consult the sections on defining custom classes and implementing data binding in Windows Forms.

<!-- tags: [grid, binding, windows forms, custom data, INotifyPropertyChanged] keywords: [bindinglist, customclass, propertychanged, raisepropertychanged, windows forms, data binding, c#, vb.net] -->
```