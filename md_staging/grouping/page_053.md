```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: grouping
page_number: 053
page_id: grouping#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:15Z
fidelity: lossless
-->

# Essential Grouping

```cpp
sy = int.Parse(y.ToString().Substring(1));
return sy - sx;
}
catch 
{ 
    throw new ArgumentException("A must be in the form 'an***'");
}
}
```

### [VB.NET]

```vb
Public Class AComparer
    Implements IComparer
    
    ' Implementing IComparer to define the object comparisons.
    Public Function Compare(ByVal x As Object, ByVal y As Object) As Integer _
        Implements IComparer.Compare
        
        If x Is Nothing And y Is Nothing Then
            Return 0
        Else
            If x Is Nothing Then
                Return -1
            Else
                If y Is Nothing Then
                    Return 1
                Else
                    Dim sx As Integer = 0
                    Dim sy As Integer = 0
                    Try
                        ' Ignoring the leading character to have numerical sorting.
                        sx = Integer.Parse(x.ToString().Substring(1))
                        sy = Integer.Parse(y.ToString().Substring(1))
                        Return sy - sx
                    Catch
                    End Try
                End If
            End If
        End If
    End Function
End Class
```

16. Add this code to the Main method to use this custom comparer to sort column A.

---

Copyright © 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion Winforms, Essential Grouping, Comparer, Custom Sorting] keywords: [Syncfusion Winforms, Custom Comparer, Compare Method, Object Comparison, Numerical Sorting] -->
```