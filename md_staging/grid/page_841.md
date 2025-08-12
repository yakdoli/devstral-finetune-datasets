```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_841.jpeg
document_name: grid
page_number: 841
page_id: grid#page_841
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:43:03Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
QueryAddRelationEventHandler(Engine_QueryAddRelation);
void Engine_QueryAddRelation(object sender, QueryAddRelationEventArgs e)
{
    Console.WriteLine(e.Relation.Name);
}
```

## C#

```csharp
[VB.NET]
AddHandler gridGroupingControl1.Engine.QueryAddRelation, AddressOf Engine_QueryAddRelation

Private Sub Engine_QueryAddRelation(ByVal sender As Object, ByVal e As QueryAddRelationEventArgs)
    Console.WriteLine(e.Relation.Name)
End Sub
```

## QueryShowNestedPropertiesFields Event

It is called when there exists nested properties in the bound datasource. With the help of this event, you can determine if the individual fields in the nested property should be displayed.

### C#

```csharp
this.gridGroupingControl.Engine.QueryShowNestedPropertiesFields += new QueryShowNestedPropertiesFieldsEventHandler(Engine_QueryShowNestedPropertiesFields);

void Engine_QueryShowNestedPropertiesFields(object sender, QueryShowNestedPropertiesFieldsEventArgs e)
{
    if (e.PropertyDescriptor.PropertyType == typeof(BaseClass))
        e.Cancel = true;
}
```

### VB.NET

```vb
AddHandler gridGroupingControl1.Engine.QueryShowNestedPropertiesFields, AddressOf Engine_QueryShowNestedPropertiesFields

Private Sub Engine_QueryShowNestedPropertiesFields(ByVal sender As Object, ByVal e As QueryShowNestedPropertiesFieldsEventArgs)
    If e.PropertyDescriptor.PropertyType Is GetType(BaseClass) Then
        e.Cancel = True
    End If
End Sub
```

## API Reference

- **Namespace**: grid
- **Class**: QueryShowNestedPropertiesFieldsEvent
- **Members**:
  - **Event Name**: Engine_QueryShowNestedPropertiesFields
  - **Signature**:
    ```csharp
    void Engine_QueryShowNestedPropertiesFields(object sender, QueryShowNestedPropertiesFieldsEventArgs e)
    ```
    - **Parameters**:
      - `sender`: The object that triggered the event.
      - `e`: Event arguments containing the property details.

### Parameters

| Parameter | Type | Description | Default | Required |
|-----------|------|-------------|---------|----------|
| sender    | object | The sender of the event. | null | Yes |
| e         | QueryShowNestedPropertiesFieldsEventArgs | Event arguments. | N/A | Yes |

### Returns

- Type: void
- Description: This event does not return any value.

### Exceptions

- None.

## Code Examples

### C#

```csharp
this.gridGroupingControl.Engine.QueryShowNestedPropertiesFields += new QueryShowNestedPropertiesFieldsEventHandler(Engine_QueryShowNestedPropertiesFields);

void Engine_QueryShowNestedPropertiesFields(object sender, QueryShowNestedPropertiesFieldsEventArgs e)
{
    if (e.PropertyDescriptor.PropertyType == typeof(BaseClass))
        e.Cancel = true;
}
```

### VB.NET

```vb
AddHandler gridGroupingControl1.Engine.QueryShowNestedPropertiesFields, AddressOf Engine_QueryShowNestedPropertiesFields

Private Sub Engine_QueryShowNestedPropertiesFields(ByVal sender As Object, ByVal e As QueryShowNestedPropertiesFieldsEventArgs)
    If e.PropertyDescriptor.PropertyType Is GetType(BaseClass) Then
        e.Cancel = True
    End If
End Sub
```

## See also

- [QueryAddRelationEvent](#queryaddrelationevent)

<!-- tags: [Syncfusion Winforms, Grid, QueryShowNestedPropertiesFields, Nested Properties] keywords: [nested properties, event, datasource, grid, engine, show fields, cancel, base class, typed, properties] -->
```