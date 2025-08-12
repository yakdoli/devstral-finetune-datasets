```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_828.jpeg
document_name: grid
page_number: 828
page_id: grid#page_828
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:58Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Create a class (`ChildObj`) to represent child table records in a `WinForms` environment.
- The class implements the `INotifyPropertyChanged` interface for property change notifications.
- Demonstrates the use of private fields and public properties with getter/setter methods for managing table record data.

## Content

### Step 1: Create the `ChildObj` class
The following C# code snippet defines the `ChildObj` class, which is used to represent child table records. This class inherits from `INotifyPropertyChanged` to notify UI components of property changes.

```csharp
public class ChildObj : INotifyPropertyChanged
{
    private string f1, f2;
    private int f3;

    public ChildObj(string f1, string f2, int f3)
    {
        this.f1 = f1;
        this.f2 = f2;
        this.f3 = f3;
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

    public int Field3
    {
        get { return f3; }
        set
        {
            if (f3 != value)
            {
                f3 = value;
                RaisePropertyChanged("Field3");
            }
        }
    }

    public event PropertyChangedEventHandler PropertyChanged;

    protected virtual void RaisePropertyChanged(string propertyName)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}
```

### Explanation
- **Fields**:
  - `f1`, `f2` (strings) and `f3` (integer) are private fields used to store the record data.
- **Constructor**:
  - Initializes the `ChildObj` instance with the provided values for `f1`, `f2`, and `f3`.
- **Properties**:
  - `Field1`, `Field2`, and `Field3` are public properties with get/set accessors.
  - The `set` method checks for changes and raises the `PropertyChanged` event if a value has changed.
- **Event**:
  - `PropertyChanged` is implemented to notify UI components or bindings that a property has been modified.
- **Helper Method**:
  - `RaisePropertyChanged` is a protected method to simplify the invocation of the `PropertyChanged` event.

### Usage
This `ChildObj` class can be instantiated and used to populate child table records in a `WinForms` application. It ensures that changes to the object's properties are reflected in the UI through the `INotifyPropertyChanged` interface.

## API Reference
- **Namespace**: The `ChildObj` class is typically placed in an application-specific or domain-related namespace.
- **Properties**:
  - `Field1`: Represents the first string property of the child record.
  - `Field2`: Represents the second string property of the child record.
  - `Field3`: Represents the integer property of the child record.
- **Event**:
  - `PropertyChanged`: Triggered when a property value changes.

## Cross References
- Refer to the documentation on **Syncfusion's Windows Forms Grid** for more details on integrating `ChildObj` instances into grid controls as child records.
- See the [INotifyPropertyChanged Interface](https://docs.microsoft.com/en-us/dotnet/api/system.componentmodel.inotifypropertychanged?view=net-8.0) for more information on property change notifications in .NET.

<!-- tags: [Syncfusion, WinForms, Grid, INotifyPropertyChanged, ChildObj, Namespace, Properties, Event] keywords: [Windows Forms, property change notification, Grid, child table records, implementation, INotifyPropertyChanged] -->
```