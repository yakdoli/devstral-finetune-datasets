```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: HTMLUI
page_number: 059
page_id: HTMLUI#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:06:02Z
fidelity: lossless
-->

Essential HTMLUI for Windows Forms

```
[VB.NET]
```vb
' MergeSupportedEvents method is to merge the standard and special events.
Private htmlElements As Hashtable = 
Me.HtmluiControl1.Document.GetElementsByUserIdHash()
Private txt As INPUTElementImpl = CType(IIf(TypeOf htmlElements("txt") Is INPUTElementImpl, htmlElements("txt"), Nothing), INPUTElementImpl)
Private specialEvents As String() = New String(1) {}
Private specialEvents(0) = "Yes"
Private specialEvents(1) = "No"
MessageBox.Show("Before Merging:" + Me.txt.SupportedEvents.Length.ToString())
Me.txt.MergeSupportedEvents(specialEvents)
MessageBox.Show("After Merging:" + Me.txt.SupportedEvents.Length.ToString())
```
```

## 4.5.1 Element Types

The following are the various HTML elements supported by Essential HTMLUI.

| Anchor Element      | Body Element       | Bold Element       | BR Element        | Custom Element      | Div Element        |
|---------------------|--------------------|--------------------|-------------------|---------------------|--------------------|
| EM Element          | Font Element       | Form Element       | H1 - H6 Element   | Header Element      | HR Element         |
| I Element           | IMG Element        | Input Element      | LI Element        | Link Element        | OL Element         |
| PRE Element         | Script Element     | Select Element     | Span Element      | Strong Element      | Style Element      |
| TD Element          | TextArea Element   | TH Element         | TR Element        | U Element           | UL Element         |

## 4.5.2 A - Anchor Element

The **A** element is used in creating links to another document or in creating bookmarks within the same document. This element is defined by the `<a>` tag in the HTML code. The **AElementImpl** class contains the properties and methods related to this element. Some of the important properties and methods are listed below:

### Properties

## API Reference
- None provided in the current scope.

## Code Examples
- None provided in the current scope.

## RAG Annotations
<!-- tags: [HTMLUI, Syncfusion Winforms, ElementTypes, AnchorElement, AElementImpl] keywords: [HTML elements, links, bookmarks, H1-H6, styled elements, custom elements] -->
```