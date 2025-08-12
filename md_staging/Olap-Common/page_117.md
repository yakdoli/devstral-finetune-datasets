```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_117.jpeg
document_name: Olap Common
page_number: 117
page_id: Olap Common#page_117
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:55Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
// Closing the provider connection.
this.dataManager.DataProvider.CloseConnection();
return cellSet;
}
```

### Members
```csharp
public MemberCollection GetChildMembers(string memberUniqueName, string cubeName)
{
    throw new NotImplementedException();
}
public CubeSchema GetCubeSchema(string cubeName)
{
    throw new NotImplementedException();
}
public CubeInfoCollection GetCubes()
{
    throw new NotImplementedException();
}
public MemberCollection GetLevelMembers(string levelUniqueName, string cubeName)
{
    throw new NotImplementedException();
}
#endregion
```

### VB Implementation
```vb
[VB]
Public Class OlapManager
    Implements IOlapDataProvider
    Private dataManager As Syncfusion.OlapSilverlight.Manager.OlapDataProvider
    ''' <summary>
    ''' Initializes a new instance of the <see cref="OlapManager"/> class.
    ''' </summary>
End Class
```

---

<!-- tags: [Olap Common, data provider, cube schema, member collection, VB.NET] keywords: [memberUniqueName, cubeName, levelUniqueName, membercollection, cubeschema, cubes, cubinfocollection, synchronization, exception handling, interface implementation, Winforms] -->
```