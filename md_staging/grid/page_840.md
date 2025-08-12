<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_840.jpeg
document_name: grid
page_number: 840
page_id: grid#page_840
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:44:07Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
Private Sub Engine_QueryShowRelationDisplayFields(ByVal sender As Object, ByVal e As QueryShowRelationFieldsEventArgs)
    If e.Relation.ChildTableName = "Countries" Then
        e.ShowRelationFields = ShowRelationFields.Hide
    End If
End Sub
```

## QueryShowField Event

It gets fired for every field in the Field Descriptor Collection of the individual tables in the dataset. It lets you control over the population of field descriptors. Using this event, you can check for specific fields and cancel the population of desired fields at runtime.

### C#

```csharp
this.gridGroupingControl1.Engine.QueryShowField += new QueryShowFieldEventHandler(Engine_QueryShowField);

void Engine_QueryShowField(object sender, QueryShowFieldEventArgs e)
{
    if (e.Field.Name == "GrandChildID")
        e.Cancel = true;
}
```

### VB.NET

```vb
AddHandler gridGroupingControl1.Engine.QueryShowField, AddressOf Engine_QueryShowField

Private Sub Engine_QueryShowField(ByVal sender As Object, ByVal e As QueryShowFieldEventArgs)
    If e.Field.Name = "GrandChildID" Then
        e.Cancel = True
    End If
End Sub
```

## QueryAddRelation Event

It is invoked for every relation that is being added to the RelationDescriptorCollection. By setting e.Cancel to true, you can avoid specific relations being added.

### C#

```csharp
this.gridGroupingControl1.Engine.QueryAddRelation += new
```

## Page-level Navigation/TOC

<!-- tags: [Syncfusion Winforms, grid, event-handling, QueryShowRelationDisplayFields, QueryShowField, QueryAddRelation] keywords: [relation, field descriptor, population, event handling, GridGroupingControl, cancel, dataset, field descriptors] -->