```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_406.jpeg
document_name: tools
page_number: 406
page_id: tools#page_406
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:52Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the `Closing Event` of the `PopupCalculator` control.
- Implements the event to display the final value of the `Calculator` control.
- Includes sample code in C# and VB.NET to handle the event.

## Content

### Closing Event of the `PopupCalculator` control

#### Overview
The `Closing Event` of the `PopupCalculator` control is raised when the control is closed after the `=` button is clicked. This event can be used to display the final value of the `Calculator` control.

#### Implementation

##### C#

```csharp
this.popupCalculator1.Closing += new
PopupCalculatorClosingEventHandler(this.HandlePopupCalculatorClosingEvent);

public void HandlePopupCalculatorClosingEvent(object sender, CalculatorClosingEventArgs args)
{
    // Event logging
    string item = args.FinalValue.ToString();
    string eventlogmessage = String.Format("Event: {0} FinalValue: {1}\r\n", "CalculatorClosing", item);
    Console.WriteLine(eventlogmessage);
}
```

##### VB.NET

```vb
Private Me.popupCalculator1.Closing += New
PopupCalculatorClosingEventHandler(Me.HandlePopupCalculatorClosingEvent)

Public Sub HandlePopupCalculatorClosingEvent(ByVal sender As Object, ByVal args As CalculatorClosingEventArgs)
    ' Event logging
    Dim item As String = args.FinalValue.ToString()
    Dim eventlogmessage As String = String.Format("Event: {0} FinalValue: {1}" & Constants.vbCrLf, "CalculatorClosing", item)
    Console.WriteLine(eventlogmessage)
End Sub
```

#### Event Log Message

The event log message shows the last action in the `Calculator` control, as illustrated in the figure below:

**Figure 206: Event log Message of the last action in the Calculator Control**

![Event Log Message](https://example.com/event_log_message.png)

---

## API Reference

- **Event Name**: `PopupCalculatorClosingEvent`
- **Args**: `CalculatorClosingEventArgs`
- **Properties**:
  - `FinalValue`: The final value of the `Calculator`.
  - `Cancel`: A flag to indicate whether the closing can be canceled.

## Code Examples

### C# Example

```csharp
using System;
using Syncfusion.WinForms.Controls;

public class CalculatorExample
{
    private PopupCalculator popupCalculator1;

    public CalculatorExample()
    {
        // Initialize the PopupCalculator control
        popupCalculator1 = new PopupCalculator();
        popupCalculator1.Closing += new
            PopupCalculatorClosingEventHandler(HandlePopupCalculatorClosingEvent);
    }

    public void HandlePopupCalculatorClosingEvent(object sender, CalculatorClosingEventArgs args)
    {
        // Handle the event
        string item = args.FinalValue.ToString();
        string eventlogmessage = String.Format("Event: {0} FinalValue: {1}\r\n", "CalculatorClosing", item);
        Console.WriteLine(eventlogmessage);
    }
}
```

### VB.NET Example

```vb
Imports Syncfusion.WinForms.Controls

Public Class CalculatorExample
    Private popupCalculator1 As PopupCalculator

    Public Sub New()
        ' Initialize the PopupCalculator control
        popupCalculator1 = New PopupCalculator()
        AddHandler popupCalculator1.Closing, AddressOf HandlePopupCalculatorClosingEvent
    End Sub

    Public Sub HandlePopupCalculatorClosingEvent(ByVal sender As Object, ByVal args As CalculatorClosingEventArgs)
        ' Handle the event
        Dim item As String = args.FinalValue.ToString()
        Dim eventlogmessage As String = String.Format("Event: {0} FinalValue: {1}" & Constants.vbCrLf, "CalculatorClosing", item)
        Console.WriteLine(eventlogmessage)
    End Sub
End Class
```

---

<!-- tags: [Syncfusion, WinForms, Calculator, Event, PopupCalculator, FinalValue] keywords: [Closing Event, PopupCalculator, Calculator, FinalValue, Event Logging, C#, VB.NET] -->
```