```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_832.jpeg
document_name: grid
page_number: 832
page_id: grid#page_832
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:43:22Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Implementation of INotifyPropertyChanged Interface

This section demonstrates the creation of a `ParentObj` class that references instances of another class (`ChildObj`). Both classes implement the `INotifyPropertyChanged` interface to manage property change notifications.

### Class Definition

```csharp
public class ParentObj : INotifyPropertyChanged
{
    private string f1, f2;
    private int f3;
    private BindingList<ChildObj> childObj = new BindingList<ChildObj>();

    public ParentObj(string f1, string f2, int f3, params ChildObj[] c)
    {
        this.f1 = f1;
        this.f2 = f2;
        this.f3 = f3;
        foreach (ChildObj i in c)
            childObj.Add(i);
    }

    public string Field1
    {
        get { return f1; }
        set
        {
            if (f1 != value)
            {
                f1 = value;
                RaisePropertyChanged("Field1");
            }
        }
    }

    public string Field2
    {
        get { return f2; }
        set
        {
            if (f2 != value)
            {
                f2 = value;
                RaisePropertyChanged("Field2");
            }
        }
    }

    // Additional methods and properties for INotifyPropertyChanged implementation
    public event PropertyChangedEventHandler PropertyChanged;

    protected void RaisePropertyChanged(string propertyName)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}
```

### Explanation

- **`ParentObj` Class**: This class serves as the parent record container and implements the `INotifyPropertyChanged` interface. It contains properties `Field1`, `Field2`, and `f3`, which can trigger notifications when their values change.
  
- **`BindingList<ChildObj>`**: This class maintains a collection of `ChildObj` instances, allowing for binding to UI controls like grids or list views.
  
- **Property Change Notification**: The `RaisePropertyChanged` method is used to notify any UI bindings when a property value is updated.

## Cross References

See also:
- [ChildObj Implementation](#childobj-implementation)
- [INotifyPropertyChanged Overview](#inotifypropertychanged-overview)
