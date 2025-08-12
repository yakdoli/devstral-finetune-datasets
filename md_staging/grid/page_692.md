```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_692.jpeg
document_name: grid
page_number: 692
page_id: grid#page_692
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
}
}

public string FirstName
{
    get { return first_name; }
    set
    {
        if (first_name != value)
        {
            first_name = value;
            RaisePropertyChanged("FirstName");
        }
    }
}

public string LastName
{
    get { return last_name; }
    set
    {
        if (last_name != value)
        {
            last_name = value;
            RaisePropertyChanged("LastName");
        }
        last_name = value;
    }
}

public string Address
{
    get { return address; }
    set
    {
        if (address != value)
        {
            address = value;
            RaisePropertyChanged("Address");
        }
    }
}

public string City
{
    get { return city; }
}
```

## Overview
- Illustrates property getters and setters for a WinForms application.
- Demonstrates the use of the `RaisePropertyChanged` method to notify of property changes.
- Includes implementation details forFirstName, LastName, Address, and City properties.

## Content

### Property Implementation with Change Notification

The code snippet showcases how to implement properties within a class, specifically designed to work with Windows Forms applications. Each property (FirstName, LastName, Address, and City) has a getter and setter method. The setters include a condition to ensure the property is updated only if the value has changed. When a change is detected, the `RaisePropertyChanged` method is invoked to notify any bindings or observers of the change.

### Property Change Notification

The `RaisePropertyChanged` method is called with the name of the property being changed. This is crucial for applications using data binding or model-view patterns where the UI needs to update dynamically as the model changes.

## API Reference

### Properties

#### `FirstName`
- **Getter**: Returns the current value of `first_name`.
- **Setter**: Updates the `first_name` field if it differs from the provided `value`.

#### `LastName`
- **Getter**: Returns the current value of `last_name`.
- **Setter**: Updates the `last_name` field if it differs from the provided `value`.

#### `Address`
- **Getter**: Returns the current value of `address`.
- **Setter**: Updates the `address` field if it differs from the provided `value`.

#### `City`
- **Getter**: Returns the current value of `city`.

## Code Examples

The following examples demonstrate how to use these properties:

```csharp
// Example: Setting and getting the FirstName property
public void UpdateFirstName(string newValue)
{
    FirstName = newValue;
    Console.WriteLine($"Updated FirstName to: {FirstName}");
}

// Example: Monitoring property changes
public void PropertyChangeListener()
{
    firstName.RaisePropertyChanged += (sender, args) => 
    {
        Console.WriteLine($"Property {args.PropertyName} changed.");
    };
}
```

## Page-level Navigation/TOC
- Property Implementation with Change Notification
- Property Change Notification

## Cross References
- See also: Data Binding, Model-View-ViewModel (MVVM), Property Change Notification

<!-- tags: [syncfusion, winforms, grid, properties, raisingpropertychange, data binding] keywords: [firstname, lastname, address, city, raisepropertychanged, getters, setters] -->
```