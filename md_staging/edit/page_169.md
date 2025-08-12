```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_169.jpeg
document_name: edit
page_number: 169
page_id: edit#page_169
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:08Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Provides details on configuring and handling the Context Prompt in Windows Forms.
- Explains the use of configuration files to specify Context Prompt settings.
- Describes how to populate the Context Prompt Pop-up using specific events and methods.

## Content

### Context Prompt Pop-up

#### Figure 58: Context Prompt Pop-Up

The image illustrates a code snippet showing a sample usage of the Context Prompt Pop-up in a Windows Forms application, where the context prompt dropdown is visible.

#### Context Prompt Configuration
The Context Prompt displaying characters are specified in the configuration file by using the `DropContextPrompt` field in the lexem for the corresponding character. If you wish to display the ContextPrompt pop-up in response to the opening brace - `"("` or opening curly brace -`"{`" being typed, use the following XML code:

```xml
[XML]

<lexem BeginBlock="(" Type="Operator" DropContextPrompt="true"/>  
<lexem BeginBlock="{ " Type="Operator" DropContextPrompt="true"/>
```

The preceding code has to be placed within the `<lexems>` section of the configuration file.

### Populating Context Prompt Pop-up

#### Event Handling
The Context Prompt is populated by handling the `ContextPromptOpen` event of Edit Control, and adding new prompts using the `AddPrompt` method.

#### Edit Control Event Description
| Edit Control Event    | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| ContextPromptOpen     | This event occurs when the Context Prompt has been opened.              |

## API Reference

### Events
- **`ContextPromptOpen`**  
  This event occurs when the Context Prompt has been opened.

### Methods
- **`AddPrompt`**  
  Used to add new prompts to the Context Prompt.

## Code Examples

```csharp
// Example in C#
// Required for Windows Form Designer support
InitializeComponent();

this.editControl1.Configurator.Open(@"...\\...\\config.xml");

this.Items.Add(
    // Specify the text of the item, its tooltip text, and image index
);
```

## Page-level Navigation/TOC
- Context Prompt Displaying Characters
- Populating Context Prompt Pop-up

## Cross References
- Refer to configuration file documentation for more details on using lexems.
- See also: Edit Control Events and Methods for complete API details.

### RAG Annotations
<!-- tags: [windows forms, context prompt, configuration file, lexem, event handling] keywords: [contextpromptopen, addprompt, editcontrol, windows forms, configuration, lexems, prompting] -->
```
