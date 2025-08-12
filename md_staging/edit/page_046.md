```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_046.jpeg
document_name: edit
page_number: 046
page_id: edit#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:56:40Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Lists various lexical macros used to specify settings for configuring textual elements.
- Explains how to add these macros to the current configuration in a Windows Forms application.
- Provides an example in C# for creating and adding a lexical macro to the `Edit Control`.

## Content

### Lexical Macros

| Macro Name                           | Description                                                                                                      |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------|
| `DigitMacro`                         | Contains all Unicode decimal digits. This is the same as: `[0-9]`                                             |
| `HexDigitMacro`                      | Contains all Unicode hexadecimal digits. This is same as: `[0-9a-fA-F]`                                      |
| `LineTerminatorMacro`                | Contains all Unicode line terminators. This is the same as: `[\r\n\u2028\u2029]`                          |
| `LineTerminatorWhitespaceMacro`      | Contains all Unicode line terminators and whitespace characters. This is the same as: `[ \t\n\u2028\u2029\f\v\u0085]` |
| `NonAlphaMacro`                      | Contains the inverse of `AlphaMacro`.                                                                      |
| `NonDigitMacro`                      | Contains the inverse of `DigitMacro`.                                                                      |
| `NoneMacro`                          | Contains no characters.                                                                                      |
| `NonHexDigitMacro`                   | Contains the inverse of `HexDigitMacro`.                                                                   |
| `NonLineTerminatorMacro`             | Contains the inverse of `LineTerminatorMacro`.                                                              |
| `NonLineTerminatorWhitespaceMacro`   | Contains the inverse of `LineTerminatorWhitespaceMacro`.                                                    |
| `NonWhitespaceMacro`                 | Contains the inverse of `WhitespaceMacro`.                                                                 |
| `NonWordMacro`                       | Contains the inverse of `WordMacro`.                                                                        |
| `WhitespaceMacro`                    | Contains all Unicode whitespace characters. This is the same as: `[ \t\n\r\u2029\u2028\u0085]`            |
| `WordMacro`                          | Contains all Unicode word characters. This is the same as: `[0-9a-zA-Z]`                                     |

### Adding Lexical Macros to Configuration

The lexical macros are used to specify configuration settings, and can be added to the current configuration language settings, as shown below.

### Code Example

```csharp
[C#]

// Create and add a lexical macro to the Edit Control.LexicalMacrosManager's collection.
// The Add method also returns the IMacro object associated with the lexical macro.
IMacro macro = this.EditControl.LexicalMacrosManager.Add("testMacro", @"\+");
```

## API Reference

### Methods

- **`Add(name, pattern)`**: Adds a lexical macro to the `LexicalMacrosManager` and returns the `IMacro` object associated with the lexical macro.
  - **`name`**: The name of the lexical macro.
  - **`pattern`**: The regular expression pattern for the lexical macro.

### Objects

- **`IMacro`**: Represents a macro that can be used in lexical analysis.

### Namespace

- `Syncfusion.Windows.Forms.Edit`

## Cross References

- Refer to the documentation on `LexicalMacrosManager` for more detailed information on how to manage and utilize lexical macros in your application.

<!-- tags: [Syncfusion Winforms, Lexical Macros, Edit Control, Windows Forms] keywords: [LexicalMacrosManager, IMacro, Add, pattern, WordMacro, DigitMacro, HexDigitMacro, LineTerminatorMacro] -->
```