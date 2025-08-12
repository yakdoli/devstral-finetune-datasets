```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_682.jpeg
document_name: grid
page_number: 682
page_id: grid#page_682
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:10Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

- Create a class(Class1) whose instances will represent the records. Its properties represent the record fields.
- Create another class(Class2) that implements the interfaces IBindingList and INotifyPropertyChanged, in order to be notified of any property value change. This class will represent the list of records and will act as the data store for your grouping grid.
- Implements the necessary events: ListChanged and PropertyChanged.
- Raise ListChanged event once the list is modified.
- Make the SupportChangeNotifications property to return true.
- Create an instance of Class2 and add a list of records into it. Then assign this list to the DataSource of the grouping grid.

>Note: For the complete code refer the sample:

**\<<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Custom Collections\IBindingList Demo**

## 4.3.4.2.3.3 ITypedList

This section demonstrates the implementation of ITypedList which will be used for complex data binding. It is best to use this interface where you want a type to explicitly specify the properties it exposes instead of letting the TypeDescriptor to find out using reflection. The interface contains two methods: GetItemProperties and GetListName.

The GetItemProperties accepts no parameters and returns a PropertyDescriptorCollection. In this method, you can use TypeDescriptor.GetProperties to load the properties from your type. The GetListName returns the name of the list.

### Implementation

Follow the steps below to create a collection (Books Collection) that implements ITypedList and bind this collection to the grouping grid.

1. Create a class **Book**, that represents the structure of the record.

```csharp
class Book
{
    public Book(string bname, string author)
    {
        this.bookName = bname;
    }
}
```

## API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->

<!-- tags: [syncfusion, winforms, grid, essential grid, ibindinglist, inotifypropertychanged, itypedlist, listchanged, propertychanged, books, record representation, complex data binding, typedlist, api reference, grid, code examples, implementation] -->
```
