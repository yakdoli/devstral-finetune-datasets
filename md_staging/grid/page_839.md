```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_839.jpeg
document_name: grid
page_number: 839
page_id: grid#page_839
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:43:51Z
fidelity: lossless
-->

## GridGroupingControl.ShowRelationFields Property

```csharp
Me.gridGroupingControl1.ShowRelationFields = ShowRelationFields.ShowAllRelatedFields;
```

### MaxNestedCollectionRecursionLevel Property

When nested collection is used, this property specifies the number of levels of recursion allowed when self-relations are detected. Below settings lets the grid to loop through up to four recursion levels.

#### [C#]

```csharp
this.gridGroupingControl1.Engine.MaxNestedCollectionRecursionLevel = 4;
```

#### [VB.NET]

```vb
Me.gridGroupingControl1.Engine.MaxNestedCollectionRecursionLevel = 4
```

### QueryShowRelationDisplayFields Event

It is raised for every foreign-key relation. It allows you to control at run-time related fields of the child table should be added to the FieldDescriptorCollection. Inside this event, you can check for specific fields and set e.Cancel to true to avoid adding those fields.

#### [C#]

```csharp
this.gridGroupingControl1.Engine.QueryShowRelationDisplayFields += new QueryShowRelationFieldsEventHandler(Engine_QueryShowRelationDisplayFields);

void Engine_QueryShowRelationDisplayFields(object sender, QueryShowRelationFieldsEventArgs e)
{
    if (e.Relation.ChildTableName == "Countries")
    {
        e.ShowRelationFields = ShowRelationFields.Hide;
    }
}
```

#### [VB.NET]

```vb
AddHandler gridGroupingControl1.Engine.QueryShowRelationDisplayFields, AddressOf Engine_QueryShowRelationDisplayFields
```

---

### API Reference

#### Properties
- `ShowRelationFields`: Enables the display of related fields in a `GridGroupingControl`.
- `MaxNestedCollectionRecursionLevel`: Defines the number of self-relation recursion levels allowed in a nested collection.

---

### Code Examples

#### C# Example
```csharp
// Enable display of all related fields
this.gridGroupingControl1.ShowRelationFields = ShowRelationFields.ShowAllRelatedFields;

// Set the recursion level to 4
this.gridGroupingControl1.Engine.MaxNestedCollectionRecursionLevel = 4;

// Handle the QueryShowRelationDisplayFields event
this.gridGroupingControl1.Engine.QueryShowRelationDisplayFields += new QueryShowRelationFieldsEventHandler(Engine_QueryShowRelationDisplayFields);

void Engine_QueryShowRelationDisplayFields(object sender, QueryShowRelationFieldsEventArgs e)
{
    if (e.Relation.ChildTableName == "Countries")
    {
        e.ShowRelationFields = ShowRelationFields.Hide;
    }
}
```

#### VB.NET Example
```vb
' Enable display of all related fields
Me.gridGroupingControl1.ShowRelationFields = ShowRelationFields.ShowAllRelatedFields

' Set the recursion level to 4
Me.gridGroupingControl1.Engine.MaxNestedCollectionRecursionLevel = 4

' Handle the QueryShowRelationDisplayFields event
AddHandler gridGroupingControl1.Engine.QueryShowRelationDisplayFields, AddressOf Engine_QueryShowRelationDisplayFields

Sub Engine_QueryShowRelationDisplayFields(ByVal sender As Object, ByVal e As QueryShowRelationFieldsEventArgs)
    If e.Relation.ChildTableName = "Countries" Then
        e.ShowRelationFields = ShowRelationFields.Hide
    End If
End Sub
```

---

### Page-level Navigation/TOC

- [GridGroupingControl.ShowRelationFields Property](#gridgroupingcontrolshowrelationfields-property)
  - [MaxNestedCollectionRecursionLevel Property](#maxnestedcollectionrecursionlevel-property)
  - [QueryShowRelationDisplayFields Event](#queryshowrelationdisplayfields-event)

---

### Reports

#### Summary
- This page explains the advanced features of the GridGroupingControl in Syncfusion WinForms, focusing on properties and events related to handling related fields and nested collections.

#### Report History
- **2025-08-09**: Updated code examples and clarified descriptions for QueryShowRelationDisplayFields event handling.

---

### Cross References

- **Related Controls**: GridGroupingControl
- **Related Properties**: ShowRelationFields, MaxNestedCollectionRecursionLevel
- **Related Methods**: QueryShowRelationDisplayFields

<!-- tags: [Syncfusion Winforms, GridGroupingControl, Properties, Events, Nested Collections, Related Fields] keywords: [GridGroupingControl, ShowRelationFields, MaxNestedCollectionRecursionLevel, QueryShowRelationDisplayFields, related fields, nested collection, recursion, event handling] -->
```