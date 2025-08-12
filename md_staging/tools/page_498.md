```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_498.jpeg
document_name: tools
page_number: 498
page_id: tools#page_498
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:17:10Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```vb
End Set
End Property

Public Property CalendarMonthBackground() As Color
    Get
        Return BackColor
    End Get
    Set(ByVal value As Color)
        BackColor = value
    End Set
End Property

Public Property Value() As DateTime
    Get
        Return SelectionStart
    End Get
    Set(ByVal value As DateTime)
        SelectionStart = SelectionEnd = value
    End Set
End Property

Public Event NullButtonDown As DateTimePickerAdv.NullButtonEventHandler
Public Event SelectDate As DateTimePickerAdv.SelectDateEventHandler
Public Event DateChange As DateTimePickerAdv.DateChangedEventHandler

Public Sub New()
    AddHandler Me.DateSelected, AddressOf OnDateSelected
    AddHandler Me.DateChanged, AddressOf OnDateChanged
End Sub

Protected Sub OnDateSelected(ByVal sender As Object, ByVal e As System.Windows.Forms.DateRangeEventArgs)
    RaiseEvent SelectDate(Me, New EventArgs())
End Sub

Protected Sub OnDateChanged(ByVal sender As Object, ByVal e As System.Windows.Forms.DateRangeEventArgs)
    RaiseEvent DateChange(Me, New EventArgs())
End Sub

Public ReadOnly Property Culture() As String
    Get
        Return "Not Supported"
    End Get
End Property
```

## API Reference

### Properties

#### CalendarMonthBackground()
- **Type:** Color
- **Description:** Gets or sets the color used for the calendar month background.

#### Value()
- **Type:** DateTime
- **Description:** Gets or sets the selected date.

#### Culture()
- **Type:** String
- **Description:** Returns `"Not Supported"` indicating that this property is not supported.

### Events

#### NullButtonDown
- **Type:** DateTimePickerAdv.NullButtonEventHandler
- **Description:** Triggered when the null button is pressed.

#### SelectDate
- **Type:** DateTimePickerAdv.SelectDateEventHandler
- **Description:** Triggered when a date is selected.

#### DateChange
- **Type:** DateTimePickerAdv.DateChangedEventHandler
- **Description:** Triggered when the date is changed.

### Subroutines

#### New()
- **Description:** Initializes a new instance of the class and adds handlers for the `DateSelected` and `DateChanged` events.

#### OnDateSelected
- **Parameters:**
  - `sender` As Object
  - `e` As System.Windows.Forms.DateRangeEventArgs
- **Description:** Raises the `SelectDate` event.

#### OnDateChanged
- **Parameters:**
  - `sender` As Object
  - `e` As System.Windows.Forms.DateRangeEventArgs
- **Description:** Raises the `DateChange` event.

<!-- tags: [Syncfusion, WinForms, DateTimePickerAdv, properties, events, methods] keywords: [CalendarMonthBackground, Value, Culture, NullButtonDown, SelectDate, DateChange] -->
```