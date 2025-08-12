```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_835.jpeg
document_name: grid
page_number: 835
page_id: grid#page_835
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:43:35Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Code Implementation

```csharp
End Sub

Public Event PropertyChanged As PropertyChangedEventHandler
Implements INotifyPropertyChanged.PropertyChanged
End Class
```

### Step 3: Generating the Collection Using `BindingList`

Generate the collection using the `BindingList` class, which implements the `ListChanged` events. This allows the grid to listen to changes in the list. Add a few items to the collection.

#### C#

```csharp
BindingList<ParentObj> topList = new BindingList<ParentObj>();
BindingList<ChildObj> childList = new BindingList<ChildObj>();

Random r = new Random();
for (int i = 0; i < 30; i++)
    childList.Add(new ChildObj(string.Format("Name{0}", r.Next(10)), 
                              string.Format("Desc{0}", r.Next(20), r.Next(30))));

for (int i = 0; i < 5; i++)
{
    topList.Add(new ParentObj(string.Format("Name{0}", r.Next(5)), 
                             string.Format("Desc{0}", r.Next(15), r.Next(20)));
    for (int j = i * 5; j < (i * 5) + 5; j++)
        topList[i].Child.Add(childList[j]);
}
```

#### VB.NET

```vb
Private topList As BindingList(Of UniformChildList_2005.ParentObj) = New BindingList(Of UniformChildList_2005.ParentObj)()
Private childList As BindingList(Of UniformChildList_2005.ChildObj) = New BindingList(Of UniformChildList_2005.ChildObj)()

Private r As Random = New Random()
For i As Integer = 0 To 29
    childList.Add(New _
        UniformChildList_2005.ChildObj(String.Format("Name{0}", r.Next(10)), _
                                      String.Format("Desc{0}", r.Next(20), r.Next(30))))
Next i

For i As Integer = 0 To 4
    topList.Add(New U _
        nformChildList_2005.ParentObj(String.Format("Name{0}", r.Next(5)), _
                                     String.Format("Desc{0}", r.Next(15), r.Next(20)))
    Dim j As Integer = i * 5
```
```html
<!-- tags: [syncfusion, windowsforms, grid, bindinglist, listchanged, propertychanged, parentobj, childobj] keywords: [bindinglist, listchanged, propertychanged, topList, childList, random, add, for loop, csharp, vb.net, syncfusion winforms, uniformchildlist_2005.parentobj, uniformchildlist_2005.childobj] -->
``` 
```