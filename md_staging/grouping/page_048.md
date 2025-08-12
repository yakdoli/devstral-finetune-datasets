```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_048.jpeg
document_name: grouping
page_number: 048
page_id: grouping#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:27Z
fidelity: lossless
-->

## Essential Grouping

![Figure 19: Screen showing the initial data followed by values computed using the expression 2.1 * [B] + 3.2](attachment://2.png)

### 4.3.3 Sorting

To sort your data, you must add the name of the property that you want to sort to the `Engine.TableDescriptor.SortedColumns` collection.

To demonstrate this, create and sort a dataset in a Console Application:

In the Console Application, comment out all the code that is in the `Main` method and add this code to create a data object, set it into the `GroupingEngine`, display the data, sort it by property A, and re-display the sorted data.

```csharp
[C#]

// Create an ArrayList of random MyObjects.
ArrayList list = new ArrayList();
Random r = new Random();

for(int i = 0; i < 10; i++)
{
    list.Add(new MyObject(r.Next(5)));
}

// Create a Grouping.Engine object.
Engine groupingEngine = new Engine();
```

## API Reference (if applicable)

### WinForms-specific conventions

- Use C# examples unless VB is explicitly shown.
- Indicate namespaces and types correctly, such as `Syncfusion.Windows.Forms.Tools.TabControlAdv` or `Syncfusion.Windows.Forms.Grid`.

### Example Usage

The snippet demonstrates creating a dataset and initializing a `GroupingEngine` for sorting purposes.

## Code Examples

```csharp
// Example showing the creation of a random dataset and its sorting.
ArrayList list = new ArrayList();
Random r = new Random();

for(int i = 0; i < 10; i++)
{
    list.Add(new MyObject(r.Next(5)));
}

Engine groupingEngine = new Engine();
```

<!-- tags: [syncfusion, windows forms, grouping, sorting, tabledescriptor] keywords: [sort, property, data, dataset, demo, c#, main method, console application, groupingengine, random data] -->
```