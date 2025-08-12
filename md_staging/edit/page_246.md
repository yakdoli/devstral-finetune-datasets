```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_246.jpeg
document_name: edit
page_number: 246
page_id: edit#page_246
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:58Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Content

### 4.14.6.2 ContextChoiceSelectedTextInsert Event

This event is discussed in the [Context Choice](#context-choice) topic.

### 4.14.6.3 ContextChoiceClose Event

This event is discussed in the [Context Choice](#context-choice) topic.

### 4.14.6.4 ContextChoiceItemSelected Event

This event is discussed in the [Context Choice](#context-choice) topic.

### 4.14.6.5 ContextChoiceUpdate Event

This event occurs when the context choice list is updated.

The event handler receives an argument of type **IContextChoiceController**. The following **IContextChoiceController** members provide information specific to this event:

| Member                | Description                                                |
|-----------------------|------------------------------------------------------------|
| Dropper               | Gets / sets dropping lexem.                                |
| ExtendItemsFilteringString | Specifies whether autocomplete string should be extended. |
| FormSize             | Gets / sets size of the context choice form.               |
| Images               | Gets collection of the INamedImage items.                  |
| IsVisible            | Specifies whether context choice window associated with the current controller is visible. |
| Items                | Gets collection of the context choice items.               |
| LexemBeforeDropper   | Gets / sets lexem situated before dropper.                 |

## Page-level Navigation/TOC (if applicable)

- **ContextChoiceSelectedTextInsert Event**
- **ContextChoiceClose Event**
- **ContextChoiceItemSelected Event**
- **ContextChoiceUpdate Event**

## Cross References

- See also: [Context Choice](#context-choice)

### WinForms-specific conventions

- This section explains the behavior and usage of context choice-related events in WinForms.
- **IContextChoiceController** provides specific methods and properties for event handling.

<!-- tags: [product, module, control, api, version?] keywords: [ContextChoiceSelectedTextInsert, ContextChoiceClose, ContextChoiceItemSelected, ContextChoiceUpdate, IContextChoiceController] -->
```