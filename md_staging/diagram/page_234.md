```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_234.jpeg
document_name: diagram
page_number: 234
page_id: diagram#page_234
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:00Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This page explains how to retrieve or set data using specific members of `PropertyChangingEventArgs` and `PropertyChangedEventArgs`.
- It provides details on the properties and methods associated with these events.
- Includes programmatic examples in C# to demonstrate event handling.

## Content

### PropertyChangingEventArgs Member

| **PropertyChangingEventArgs Member** | **Description** |
|---------------------------------------|------------------|
| Cancel                              | Cancels the PropertyChanged event. |
| NewValue                            | Returns the new value assigned to the property. |
| PropertyContainer                   | Returns the container for the property. |
| PropertyName                        | Returns the name of the property whose value is changed. |

### PropertyChangedEventArgs Member

| **PropertyChangedEventArgs Member** | **Description** |
|-------------------------------------|------------------|
| NodeAffected                       | Returns the name of the node whose property is changed. |
| PropertyName                       | Returns the name of the property whose value is changed. |

### Programmatic Event Handling

Programmatically, the events are written as follows:

```csharp
[C#]

public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)model1.EventSink).PropertyChanged += new Syncfusion.Windows.Forms.Diagram.PropertyChangedEventHandler(Form1_PropertyChanged);
    ((DocumentEventSink)model1.EventSink).PropertyChanging += new PropertyChangingEventHandler(Form1_PropertyChanging);
}

private void Form1_PropertyChanged(Syncfusion.Windows.Forms.Diagram.PropertyChangedEventArgs evtArgs)
{
    MessageBox.Show("PropertyChanged event is fired" + "\n" + "Property Name: " + evtArgs.PropertyName);
}

private void Form1_PropertyChanging(Syncfusion.Windows.Forms.Diagram.PropertyChangingEventArgs eprop)
{
    MessageBox.Show("PropertyChanging event is fired" + "\n" + "Property Name: " + eprop.PropertyName + "\n" + "new");
}
```

## API Reference

### `PropertyChangedEventArgs`

- **NodeAffected**  
  Returns the name of the node whose property is changed.
- **PropertyName**  
  Returns the name of the property whose value is changed.

### `PropertyChangingEventArgs`

- **Cancel**  
  Cancels the PropertyChanged event.
- **NewValue**  
  Returns the new value assigned to the property.
- **PropertyContainer**  
  Returns the container for the property.
- **(PropertyName**  
  Returns the name of the property whose value is changed.

## Code Examples

The provided C# code example demonstrates how to handle the `PropertyChanged` and `PropertyChanging` events for a `Syncfusion.Windows.Forms.Diagram` control.

```csharp
using Syncfusion.Windows.Forms.Diagram;
using System.Windows.Forms;

public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)model1.EventSink).PropertyChanged += new Syncfusion.Windows.Forms.Diagram.PropertyChangedEventHandler(Form1_PropertyChanged);
    ((DocumentEventSink)model1.EventSink).PropertyChanging += new PropertyChangingEventHandler(Form1_PropertyChanging);
}

private void Form1_PropertyChanged(Syncfusion.Windows.Forms.Diagram.PropertyChangedEventArgs evtArgs)
{
    MessageBox.Show("PropertyChanged event is fired" + "\n" + "Property Name: " + evtArgs.PropertyName);
}

private void Form1_PropertyChanging(Syncfusion.Windows.Forms.Diagram.PropertyChangingEventArgs eprop)
{
    MessageBox.Show("PropertyChanging event is fired" + "\n" + "Property Name: " + eprop.PropertyName + "\n" + "new");
}
```

## Cross References

- Refer to the documentation for `Syncfusion.Windows.Forms.Diagram` for additional details on events and properties.

<!-- tags: [Syncfusion, Winforms, Diagram, Events, Properties, PropertyChangingEventArgs, PropertyChangedEventArgs] keywords: [PropertyChanging, PropertyChanged, events, properties, Diagram, Windows Forms, example, C#] -->
```
