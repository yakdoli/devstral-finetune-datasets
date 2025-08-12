```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_496.jpeg
document_name: tools
page_number: 496
page_id: tools#page_496
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:16:38Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section covers advanced controls and features for customizing date and time selection in Windows Forms applications.
- It includes event handling for date selection, date change, and null button clicks.
- Demonstrates the implementation of a custom calendar class with event firing capabilities.

## Content

### Control Events and Handling

Public events for DateTimePickerAdv are declared as follows:

```csharp
public event DateTimePickerAdv.NullButtonEventHandler NullButtonDown;
public event DateTimePickerAdv.SelectDateEventHandler SelectDate;
public event DateTimePickerAdv.DateChangedEventHandler DateChange;
```

#### Custom Calendar Class Implementation

The `MyCustomCalendar` class attaches event handlers for `DateSelected` and `DateChanged` events:

```csharp
public MyCustomCalendar()
{
    this.DateSelected += new System.Windows.Forms.DateRangeEventHandler(OnDateSelected);
    this.DateChanged += new System.Windows.Forms.DateRangeEventHandler(OnDateChanged);
}
```

Event handling methods are protected and trigger the corresponding events:

```csharp
protected void OnDateSelected(object sender, System.Windows.Forms.DateRangeEventArgs e)
{
    if (SelectDate != null)
    {
        SelectDate(this, new EventArgs());
    }
}

protected void OnDateChanged(object sender, System.Windows.Forms.DateRangeEventArgs e)
{
    if (DateChange != null)
    {
        DateChange(this, new EventArgs());
    }
}
```

### Specific Features

- **Culture Property**: The `Culture` property is defined as follows:

  ```csharp
  public string Culture
  {
      get { return "Not Supported"; }
  }
  ```

- **Null Button Event**: The `FireNullEvent` method triggers the `NullButtonDown` event:

  ```csharp
  public void FireNullEvent()
  {
      if (NullButtonDown != null)
      {
          NullButtonDown(this, new EventArgs());
      }
  }
  ```

#### Interface Implementation

The class implements the `IDateTimePickerAdvCalendar` interface:

```csharp
CultureInfo IDateTimePickerAdvCalendar.Culture
{
    get { throw new Exception("The method or operation is not implemented."); }
}
```

## Code Examples

The following code snippet demonstrates the use of custom calendar event handling:

```csharp
// Example of attaching event handlers and firing a null button event
MyCustomCalendar calendar = new MyCustomCalendar();
calendar.NullButtonDown += (sender, e) =>
{
    MessageBox.Show("Null button clicked.");
};

calendar.FireNullEvent();
```

## API Reference

### Namespace: Syncfusion.Windows.Forms.Tools

#### Class: MyCustomCalendar
- **Properties**
  - `Culture`: Returns a string indicating culture support, currently returning "Not Supported".
- **Methods**
  - `FireNullEvent`: Triggers the `NullButtonDown` event.
- **Events**
  - `NullButtonDown`: Triggered when the null button is clicked.
  - `SelectDate`: Triggered when a date is selected.
  - `DateChange`: Triggered when a date is changed.

## Cross References
See also:
- Date range event handlers in the `System.Windows.Forms` namespace.
- Exception handling for unsupported methods or operations.

<!-- tags: [syncfusion, winforms, datetimepickeradv, calendar, date, eventhandling, interface, nullbutton, datechange, selectdate] keywords: [date selection, event handlers, custom calendar, culture support, datetime picker, change, select, null] -->
```