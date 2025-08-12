```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_311.jpeg
document_name: tools
page_number: 311
page_id: tools#page_311
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:29Z
fidelity: lossless
-->

# Essential Tools for Windows Forms  

## Overview  
- Provides an overview of the AutoComplete control and its associated events in Windows Forms.  
- Details the AutoCompleteItemSelected Event and BeforeAddItem Event, highlighting their usage and behavior.  
- Discusses event customization and matching routines for the AutoComplete control.  

## Content  

### AutoComplete Events  

#### Overview of AutoComplete Events  

The events of the AutoComplete control are as follows.  

| AutoComplete Events                              | Description                                                                                                  |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| BeforeAddItem                                    | Handled when a new item is about to be added.                                                              |
| AutoCompleteCustomize                             | Handled to customize the AutoCompletion.                                                                    |
| AutoCompleteItemBrowsed                          | Handled when the user selects an item from the list of possible matches when the AutoComplete is set to AutoSuggest. |
| AutoCompleteItemSelected Event                   | Occurs when a new item has been selected by the user when the AutoComplete mode is set to AutoSuggest.         |
| DropDownClosed                                   | Occurs when the AutoComplete dropdown is closed.                                                             |
| DropDownDisplayed                                | Occurs when the AutoComplete dropdown is displayed.                                                          |
| MatchItem                                        | Enables you to provide a custom matching routine for the current value in the Edit control.                   |
| PreMatchItem                                     | Handled before the AutoComplete control performs a matching operation for the current text content of the active Edit control. |
| TargetChanging                                   | Occurs when the target control of the AutoComplete control changes.                                          |

#### AutoCompleteItemSelected Event  
**3.5.1.1.4.1 AutoCompleteItemSelected Event**  

- **Description:**  
  AutoCompleteItemSelected Event is raised when a new item has been selected by the user when the AutoComplete mode is set to AutoSuggest.  

- **Discussion:**  
  This event is discussed in the **External DataSource** topic.  

#### BeforeAddItem Event  
**3.5.1.1.4.2 BeforeAddItem Event**  

- **Description:**  
  Handled when a new item is about to be added.  

## API Reference  

Not applicable for this specific page content.  

## Code Examples  

No specific code examples are provided on this page.  

## Page-level Navigation/TOC  

- AutoComplete Events (3.5.1.1.4)  
  - AutoCompleteItemSelected Event (3.5.1.1.4.1)  
  - BeforeAddItem Event (3.5.1.1.4.2)  

## Cross References  

- Refer to the **External DataSource** topic for further details on the AutoCompleteItemSelected Event.  

<!-- tags: [Syncfusion, Windows Forms, AutoComplete, Event Handling, AutoSuggest, AutoCompleteItemSelected, BeforeAddItem] keywords: [AutoComplete, Events, AutoSuggest, AutoCompletion, Customization, MatchItem, DropDown, Selected Item] -->
```