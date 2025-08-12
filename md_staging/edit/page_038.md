```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_038.jpeg
document_name: edit
page_number: 038
page_id: edit#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:56:08Z
fidelity: lossless
-->

## Overview

- This page explains how to invoke and utilize the Editor Keys Binding dialog in Windows Forms applications using the `ShowKeysBindingEditor` method of the Edit Control.
- It illustrates the Keys Binding dialog box and describes how to register user-defined commands and bind custom keystroke combinations to them.
- Code examples demonstrate registering the "File.Open" command and assigning a `Ctrl+O` shortcut.

## Content

The Editor Keys Binding dialog is invoked using the `ShowKeysBindingEditor` method of the Edit Control.

### Keys Binding Dialog Box

The following illustration shows the Keys Binding dialog box.

![Figure 10: Preview of Keys Binding Dialog Box](https://i.imgur.com/Example.png)

**Figure 10: Preview of Keys Binding Dialog Box**

### Registering Custom Commands and Key Bindings

You can also make use of the `RegisteringKeyCommands` and `RegisteringDefaultKeyBindings` events to specify user-defined commands and bind the desired custom keystroke combinations to them.

### Example: Registering "File.Open" Command

This following code snippet registers the "File.Open" command and binds a `Ctrl+O` keystroke combination to it.

#### Code: Registering the "File.Open" Command

```csharp
this.editControl.ShowKeysBindingEditor();

// Bind the action name to the action using the RegisteringKeyCommands and ProcessCommandEventHandler events.
private void this.editControl_RegisteringKeyCommands(object sender, EventArgs e)
{
    this.editControl.Commands.Add("File.Open").ProcessCommand += new ProcessCommandEventHandler(Command_Open);
}
```

### Notes on Implementation

- Ensure that the `ShowKeysBindingEditor` method is called to display the dialog box where users can set custom key bindings.
- Use the `RegisteringKeyCommands` event to add custom commands and their associated actions.
- Bind the desired keystrokes using the `ProcessCommandEventHandler` to execute the command.

## API Reference

### Events
- `RegisteringKeyCommands`: Triggers when custom commands need to be registered.
- `ProcessCommandEventHandler`: Handles the execution of registered commands.

### Methods
- `ShowKeysBindingEditor()`: Invokes the Editor Keys Binding dialog to configure custom key bindings.
- `Add(String actionName)`: Adds a new action to the commands list.

### Parameters
| Name | Type | Description |
|------|------|-------------|
| actionName | String | The name of the action to be added. |

### Returns
None

### Exceptions
- None explicitly mentioned in the context.

## Code Examples

#### C#

```csharp
// Invoke the Editor Keys Binding dialog.
this.editControl.ShowKeysBindingEditor();

// Bind the action name to the action using the RegisteringKeyCommands and ProcessCommandEventHandler events.
private void this.editControl_RegisteringKeyCommands(object sender, EventArgs e)
{
    this.editControl.Commands.Add("File.Open").ProcessCommand += new ProcessCommandEventHandler(Command_Open);
}
```

## Tags and Keywords

```html
<!-- tags: Syncfusion Winforms, Editor Control, Keys Binding, Custom Key Bindings, RegisteringCommands, ProcessCommandEventHandler, CustomShortcuts -->
<!-- keywords: Syncfusion, WinForms, Editor, KeysBinding, CustomCommands, RegisteringKeyCommands, ProcessCommandEventHandler, CustomShortcuts -->
```
```