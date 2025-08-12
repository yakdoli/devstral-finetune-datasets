```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_292.jpeg
document_name: diagram
page_number: 292
page_id: diagram#page_292
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:09Z
fidelity: lossless
--> 

## Essential Diagram for Windows Forms

### Overview
- Detecting when a property value changes in the property editor is crucial for dynamically updating UI components.
- Demonstrating how to create and manage symbol palettes dynamically in Windows Forms.

## Content

### 5.35 How to Detect whether a Property Value is Changed in the Property Editor?
The `PropertyValueChanged` event can be utilized to detect changes in property values within the property editor. The following code example illustrates this.

```csharp
//PropertyValueChanged event.
propertyEditor1.PropertyGrid.PropertyValueChanged += new
PropertyValueChangedEventHandler(PropertyGrid_PropertyValueChanged);

private void PropertyGrid_PropertyValueChanged(object s,
PropertyValueChangedEventArgs e)
{
    //Here, capture the changed property (e.ChangedItem) and process the same.
}
```

```vb.net
'PropertyValueChanged event.
AddHandler propertyEditor1.PropertyGrid.PropertyValueChanged, AddressOf PropertyGrid_PropertyValueChanged

Private Sub PropertyGrid_PropertyValueChanged(ByVal s As Object, ByVal e As
PropertyValueChangedEventArgs)
    'Here, capture the changed property (e.ChangedItem) and process the same.
End Sub
```

### 5.36 How to Add Dynamically Created Symbol Palette to PaletteGroupBar
The following code sample demonstrates how to add a dynamically created symbol palette to the PaletteGroupBar control.

```csharp
//Create an instance of SymbolPalette.
```

## API Reference

### WinForms-specific conventions
- The `PropertyValueChanged` event is triggered when a property value is modified in the PropertyGrid control.
- The `SymbolPalette` class represents a dynamically created palette used for inserting symbols into the diagram.

## Code Examples

### Detection of Property Value Changes
C#, VB.NET examples provided demonstrate handling the `PropertyValueChanged` event to capture changes in property values.

### Creating Symbol Palettes
Example code demonstrates the creation and addition of a `SymbolPalette` to the PaletteGroupBar control.

<!-- tags: [syncfusion, winforms, propertygrid, symbolpalette, propertyvaluechanged, palettegroupbar] keywords: [propertyGrid, propertyValueChanged, symbolPalette, property changed detection, palette addition] -->
```