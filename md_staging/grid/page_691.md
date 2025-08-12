```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_691.jpeg
document_name: grid
page_number: 691
page_id: grid#page_691
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:03Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Off these classes, the `IBindingList` implementation has some specialities. The `BindingList<T>` automatically raises `ListChanged` event when the `INotifyPropertyChanged.PropertyChanged` event is raised in a child object. It also raises it when items are added or removed. When you implement custom collection and want the grid to react to changes in the data source, you should implement `IBindingList` and raise `ListChanged` events.

## Implementation

Follow the steps below to implement a generic collection and bind it to our grouping grid control. This implementation uses `BindingList<T>` class.

### Steps

1. Create a class (`CustomClass`) whose objects represent the records and properties represent the record fields. This class implements `INotifyPropertyChanged` interface in order to trigger the grid to react to changes in the list.

#### Code Example

```csharp
public class CustomClass : INotifyPropertyChanged
{
    int id;
    string first_name;
    string last_name;
    string address;
    string city;

    public CustomClass(int id, string fname, string lname, string addr, string city)
    {
        this.id = id;
        first_name = fname;
        last_name = lname;
        address = addr;
        this.city = city;
    }

    public int ID
    {
        get { return id; }
        set
        {
            if (id != value)
            {
                id = value;
                RaisePropertyChanged("ID");
            }
        }
    }
}
```
```html
<!-- tags: [IBindingList, BindingList, INotifyPropertyChanged, Property Changed Event, CustomCollection, Grid Control, Grouping, Windows Forms] keywords: [BindingList<T>, ListChanged, INotifyPropertyChanged.PropertyChanged, RaisesPropertyChangedEvent, CustomClass, Data Binding] -->
```