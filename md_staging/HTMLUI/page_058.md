```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_058.jpeg
document_name: HTMLUI
page_number: 058
page_id: HTMLUI#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:06:25Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Explains the use of HTML elements in HTMLUI for interactive user interfaces.
- Focuses on the `SupportedEvents` property and `MergeSupportedEvents` method in customizing HTML elements.
- Demonstrates property and method functionality in both C# and VB.NET.

## Content

### 4.5 HTML Elements

HTMLUI supports various elements in an HTML document for rendering and presenting them to the user. It allows the user to dynamically access these elements to produce rich, customized user interfaces. Each HTML element defines properties and methods that can be used for customization.

#### The property `SupportedEvents` and the method `MergeSupportedEvents` are common to most HTML elements.

##### SupportedEvents

This property returns an array of events supporting the element.

**[C#]**

```csharp
// SupportedEvents property returns an array of events supporting the element.
Hashtable htmlElements = this.htmluiControl1.Document.GetElementsByUserIdHash();
BRElementImpl br = htmlElements["br"] as BRElementImpl;
this.label1.Text = this.br.SupportedEvents.Length.ToString();
```

**[VB.NET]**

```vb
' SupportedEvents property returns an array of events supporting the element.
Private htmlElements As Hashtable = Me.HtmluiControl1.Document.GetElementsByUserIdHash()
Private tr As BRElementImpl = CType(IIf(TypeOf htmlElements("br") Is BRElementImpl, htmlElements("br"), Nothing), BRElementImpl)
Private Me.label1.Text = Me.br.SupportedEvents.Length.ToString()
```

##### MergeSupportedEvents

The `MergeSupportedEvents` method is used to merge the standard and special events.

**[C#]**

```csharp
// MergeSupportedEvents method is to merge the standard and special events.
Hashtable htmlElements = this.htmluiControl1.Document.GetElementsByUserIdHash();
INPUTElementImpl txt = htmlElements["txt"] as INPUTElementImpl;
string[] specialEvents = new string[2];
specialEvents[0] = "Yes";
specialEvents[1] = "No";
MessageBox.Show("Before Merging: " + this.txt.SupportedEvents.Length.ToString());
this.txt.MergeSupportedEvents(specialEvents);
MessageBox.Show("After Merging: " + this.txt.SupportedEvents.Length.ToString());
```

### Notes

- The `SupportedEvents` property is crucial for understanding the events that can be linked to an HTML element.
- The `MergeSupportedEvents` method allows the fusion of custom events with the standard events for enhanced functionality and customization.

## API Reference (if applicable)

This section can include detailed references to the relevant APIs and their usage within the context of HTML elements in HTMLUI.

## Code Examples

The examples provided in both C# and VB.NET illustrate practical implementations of the `SupportedEvents` property and the `MergeSupportedEvents` method.

## Page-level Navigation/TOC (if applicable)

This section could include a local Table of Contents for this page, ensuring that users can navigate through the functionality related to HTML elements effectively.

## Cross References

- See also: Other sections on HTMLUI event handling and customization.

## RAG Annotations

<!-- tags: HTMLUI, WinForms, SupportedEvents, MergeSupportedEvents, customization keywords: event handling, user interfaces, HTML elements -->
```