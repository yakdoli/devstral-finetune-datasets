```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_059.jpeg
document_name: grouping
page_number: 059
page_id: grouping#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:08Z
fidelity: lossless
-->

# Essential Grouping

## 5 Frequently Asked Questions

The following are some common tasks that you might encounter as you use Essential Grouping in your applications:

### 5.1 How to Access the Value of a Record Or Field?

The `groupingEngine.Table.Records` property will allow you to access the records (items) in your `IList` and particular fields (properties) in the records.

#### Code Examples

##### [C#]
```csharp
// Assumes the datasource is an IList holding objects of type MyObject.
// Retrieves the third object in the list.
MyObject o = this.groupingEngine.Table.Records[2].GetData() as MyObject;

// A is a public property of MyObject, so "A" is treated as a field.
object someValue = this.groupingEngine.Table.Records[2].GetValue("A");
```

##### [VB.NET]
```vbnet
' Assumes the datasource is an IList holding objects of type MyObject.
' Retrieves the third object in the list.
Dim o As MyObject = CType(Me.groupingEngine.Table.Records(2).GetData(), MyObject)

' A is a public property of MyObject, so "A" is treated as a field.
Dim someValue As Object = Me.groupingEngine.Table.Records(2).GetValue("A")
```

### Note:
<!-- tags: [Essential Grouping, Records, Property Access, C#, VB.NET] keywords: [groupingEngine, Table.Records, GetValue, IList, MyObject, field access, property retrieval] -->
```