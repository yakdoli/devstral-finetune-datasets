```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_046.jpeg
document_name: grouping
page_number: 046
page_id: grouping#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:28Z
fidelity: lossless
-->

# Essential Grouping

```csharp
Random r = new Random();

for (int i = 0; i < 10; i++)
{
    list.Add(new MyObject(r.Next(5)));
}

// Create a Grouping.Engine object.
Engine groupingEngine = new Engine();

// Set its datasource.
groupingEngine.SetSourceList(list);
```

## VB.NET

```vb
' Create an arraylist of random MyObjects.
Dim list As New ArrayList()
Dim r As New Random()

Dim i As Integer
For i = 0 To 10
    list.Add(New MyObject(r.Next(5)))
Next

' Create a Grouping.Engine object.
Dim groupingEngine As New Engine()

' Set its datasource.
groupingEngine.SetSourceList(list)
```

14. Now you must add code to list the data, add an expression property, and then display the value of the expression. To retrieve the value, you must use the `Record.GetValue` method by passing it as the name of the expression that you had assigned when it was created.

## Code Examples

### Displaying the Data Before Filtering

```csharp
// Display the data before filtering.
foreach (Record rec in groupingEngine.Table.FilteredRecords)
{
    MyObject obj = rec.GetData() as MyObject;
    if (obj != null)
    {
        Console.WriteLine(obj);
    }
}
```

## API Reference

### Methods

- `GetValue(expressionName)`
  - **Parameters**:
    - `expressionName`: Type (string) - The name of the expression to retrieve the value for.
  - **Returns**: Type (Object) - The value of the specified expression.

## Cross References

See also:
- [Expression Evaluation](#expression-evaluation)
- [Grouping Engine Setup](#grouping-engine-setup)

<!-- tags: [Syncfusion Winforms, Grouping, Data Visualization] keywords: [grouping, essential grouping, data visualization, filtering, expression evaluation, Record.GetValue] -->
```