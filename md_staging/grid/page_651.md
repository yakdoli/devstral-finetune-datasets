```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_651.jpeg
document_name: grid
page_number: 651
page_id: grid#page_651
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:31:17Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
dr.EndEdit()
i += 1
Continue:
Loop

' Optionally manually flush changes.
If Me.gridGroupingControl1.UpdateDisplayFrequency = 0 Then
    Me.gridGroupingControl1.Update()
End If
```

### Finally
```csharp
End Try
End Sub
```

### Notes on UnboundFields

- It should also take care of the **UnboundFields** whose values are usually dependent on changes to other fields. If unbound fields are used, you can tell the engine which are the fields the unbound field is dependent on, by setting the **ReferencedFields** property. When **ReferencedFields** is set and the engine detects changes to the unbound field, it will automatically also mark the field as changed. This subsequently can affect sort order, group attachment, and so on.

---

### [C#] Example

#### Adding an Unbound Field and Dependency
```csharp
// Add Unbound field 'ShipVia_CompanyName'.
gridGroupingControl1.TableDescriptor.UnboundFields.Add("ShipVia_CompanyName");

// Inform the engine about dependency on ShipVia of this field.
gridGroupingControl1.TableDescriptor.UnboundFields["ShipVia_CompanyName"].ReferencedFields = "ShipVia";
```

---

### [VB.NET] Example

#### Adding an Unbound Field and Dependency
```vb
' Add Unbound field 'ShipVia_CompanyName'.
gridGroupingControl1.TableDescriptor.UnboundFields.Add("ShipVia_CompanyName")

' Inform the engine about dependency on ShipVia of this field.
gridGroupingControl1.TableDescriptor.UnboundFields("ShipVia_CompanyName").ReferencedFields = "ShipVia"
```

---

Here is a sample screen shot.

<!-- tags: Syncfusion, Winforms, Grid, UnboundFields, ReferencedFields, version: 11.4.0.26 -->
```