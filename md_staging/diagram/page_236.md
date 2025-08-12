```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_236.jpeg
document_name: diagram
page_number: 236
page_id: diagram#page_236
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:21:04Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates the flow of a property changing event in a Windows Forms application.
- Highlights the sequence of events: Start, Process, Check, and End.
- Includes a dialog box notification for the `PropertyChanging event`.

## Content

### Diagram Explanation
The diagram below illustrates the sequence of steps involved in handling a property changing event in a Windows Forms application.

#### Diagram:
- **START**: The process begins here.
- **PROCESS**: The process logic is executed.
- **CHECK**: The system checks the current status or conditions.
- **END**: The process concludes.
  
#### Dialog Box Notification
The dialog box shows the following details:
- **Event**: `PropertyChanging event is fired`
- **Property Name**: `LineStyle.LineColor`
- **New Value**: `Color [DarkBlue]`
- **Action**: An "OK" button is available to acknowledge the change.

##### Figure: Property Changing Event
![Diagram showing the sequence of Property Changing Event](attachment:Figure_146_Property_Changing_Event.png)

### Detailed Breakdown
- **Start**: The process initiates, indicating the beginning of an event flow.
- **Process**: The main logic or processing takes place.
- **Check**: A check is performed to determine the current state or the implications of the property change.
- **End**: The process concludes, marking the completion of the event handling.
- **Dialog Box**: A pop-up dialog alerts the user that the `LineStyle.LineColor` property is about to change to `DarkBlue`.

## API Reference (if applicable)

### Events
- **PropertyChanging**
  - **Description**: Triggered when a property is about to be changed.
  - **Parameters**:
    - `propertyName`: Name of the property being changed.
    - `newValue`: The new value the property is about to take.
  - **Handler Example**:
    ```csharp
    private void OnPropertyChanging(object sender, PropertyChangingEventArgs e)
    {
        MessageBox.Show($"PropertyChanging event is fired\nProperty Name: {e.PropertyName}\nnew Value: {e.NewValue}");
    }
    ```

## Code Examples

### C# Example
```csharp
using Syncfusion.Windows.Forms.Diagram;
using System.Windows.Forms;

public class DiagramForm : Form
{
    private Diagram diagram;

    public DiagramForm()
    {
        InitializeComponent();
        diagram.PropertyChanging += OnPropertyChanging;
    }

    private void OnPropertyChanging(object sender, PropertyChangingEventArgs e)
    {
        MessageBox.Show($"PropertyChanging event is fired\nProperty Name: {e.PropertyName}\nnew Value: {e.NewValue}");
    }
}
```

## Page-level Navigation/TOC (if applicable)
- [Essential Diagram Overview](#diagram-overview)
- [Handling PropertyChanging Event](#handling-propertychanging-event)
- [Sample Implementation](#sample-implementation)

## Cross References
- See also: `Diagram Controls`, `Events in Windows Forms`, `Property Handling in Diagrams`.

## RAG Annotations
<!-- tags: [diagram, windows forms, property changing event, windows forms controls, syncfusion winforms, essential diagram] keywords: [propertychanging event, line style, darkblue, dialog box, process flow, check, end, start] -->
```