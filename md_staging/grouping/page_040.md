```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: grouping
page_number: 040
page_id: grouping#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:59Z
fidelity: lossless
-->

# Essential Grouping

In addition to grouping data, you may want to filter it for some special criteria. For example, you may want to see the total monthly sales due to orders under some value. Essential Grouping gives you the flexibility to add calculated values to the data, and then use these values to produce other information like total monthly sales due for respective order etc.

The following data manipulation techniques are available in Essential Grouping:

## 4.3.1 Filters

Another collection that is part of the schema information in the `Engine.TableDescriptor` is the `RecordFilters` collection. This collection lets you filter the data to see only the items that are in your data list and that satisfy the criteria that is specified. You can express the criteria as a logical expression using the property names, algebraic, and logical operators. You can also use LIKE, MATCH, and IN operators.

### 1. In the Console Application used in lessons 1 and 2, comment out all the code that is in the `Main` method and add the following code to create a data object and set it into the Grouping Engine.

[C#]

```csharp
static void Main(string[] args)
{
    // Create an arraylist of random MyObjects.
    ArrayList list = new ArrayList();
    Random r = new Random();

    for (int i = 0; i < 10; i++)
    {
        list.Add(new MyObject(r.Next(5)));
    }

    // Create a Grouping.Engine object.
    Engine groupingEngine = new Engine();

    // Set its datasource.
    groupingEngine.SetSourceList(list);
}
```

[VB.NET]
```vb
Sub Main(ByVal args As String())
    ' Create an arraylist of random MyObjects.
    Dim list As New ArrayList()
    Dim r As New Random()

    For i As Integer = 0 To 9
        list.Add(New MyObject(r.Next(5)))
    Next

    ' Create a Grouping.Engine object.
    Dim groupingEngine As New Engine()

    ' Set its datasource.
    groupingEngine.SetSourceList(list)
End Sub
```

<!-- tags: [grouping, filtering, essential grouping, record filters, data manipulation] keywords: [grouping, filters, criteria, logical operators, data object, Grouping.Engine, SetSourceList, ArrayList, Random, MyObject] -->
```