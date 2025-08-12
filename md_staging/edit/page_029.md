```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_029.jpeg
document_name: edit
page_number: 029
page_id: edit#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:55:45Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

### Creating and Configuring ConfigLexem Objects

#### Step 1: Defining the Format and Creating a ConfigLexem Object

**[C#]**
```csharp
// Creating a ConfigLexem object that belongs to the above defined format.
ConfigLexem configLex = new ConfigLexem("<%@", "%>", FormatType.Custom, false);

// Defining its attributes.
configLex.IsBeginRegex = false;
configLex.IsEndRegex = false;
configLex.ContinueBlock = ".+";
configLex.IsContinueRegex = true;
configLex.FormatName = "CodeBehind";
```

**[VB.NET]**
```vb.net
// Creating a ConfigLexem object that belongs to the above defined format.
Dim configLex As ConfigLexem = New ConfigLexem("<%", "%>", FormatType.Custom, False)

' Defining its attributes.
configLex.IsBeginRegex = False
configLex.IsEndRegex = False
configLex.ContinueBlock = ".+"
configLex.IsContinueRegex = True
configLex.FormatName = "CodeBehind"
```

#### Step 2: Adding the ConfigLexem Object to the Lexems Collection

**[C#]**
```csharp
this.editControl1.Language.Lexems.Add(configLex);
```

**[VB.NET]**
```vb.net
Me.editControl1.Language.Lexems.Add(configLex)
```

#### Step 3: Adding Splits and Extensions to the Language

**[C#]**
```csharp
// Adding the necessary split definitions to the current language's Splits collection.
this.editControl1.Language.Splits.Add("<%@");
this.editControl1.Language.Splits.Add("%>");

// Adding the necessary extension definitions to the current language's Extensions collection.
```

### Summary

1. **Creating a ConfigLexem Object**: Establishes a custom lexical element format for the editor, specifying its attributes such as delimiters, regex behavior, and formatting.
2. **Adding to Lexems Collection**: Integrates the ConfigLexem object into the editor's language lexems collection to define its behavior within the text editor.
3. **Defining Splits and Extensions**: Extends the language by adding specific split and extension definitions to support custom language constructs.

## API Reference

### ConfigLexem Properties

- **IsBeginRegex**: Indicates whether the beginning delimiter should be treated as a regular expression.
- **IsEndRegex**: Indicates whether the ending delimiter should be treated as a regular expression.
- **ContinueBlock**: Defines the continuation block for the lexem.
- **IsContinueRegex**: Indicates whether the continuation block should be treated as a regular expression.
- **FormatName**: Specifies the formatting style for the lexem.

### Methods

- **Add to Lexems Collection**:
  - `Language.Lexems.Add(ConfigLexem configLex)`: Adds a ConfigLexem object to the editor's language lexems collection.

- **Adding Splits and Extensions**:
  - `Language.Splits.Add(string splitDefinition)`: Adds a split definition to the language's splits collection.
  - `Language.Extensions.Add(string extensionDefinition)`: Adds an extension definition to the language's extensions collection.

## Code Examples

### Example 1: Creating and Adding a ConfigLexem

```csharp
ConfigLexem configLex = new ConfigLexem("<%@", "%>", FormatType.Custom, false);
configLex.IsBeginRegex = false;
configLex.IsEndRegex = false;
configLex.ContinueBlock = ".+";
configLex.IsContinueRegex = true;
configLex.FormatName = "CodeBehind";

this.editControl1.Language.Lexems.Add(configLex);
```

### Example 2: Adding Splits and Extensions

```csharp
this.editControl1.Language.Splits.Add("<%@");
this.editControl1.Language.Splits.Add("%>");
```

## Page-level Navigation/TOC

- **Creating and Configuring ConfigLexem Objects**
  - Defining the Format and Creating a ConfigLexem Object
  - Adding the ConfigLexem Object to the Lexems Collection
  - Adding Splits and Extensions to the Language

- **Summary**
  - Key Steps in Customizing the Language Lexems
  - Integrating Custom Lexical Elements

- **API Reference**
  - Properties and Methods for ConfigLexem and Language

- **Code Examples**
  - Example 1: Creating and Adding a ConfigLexem
  - Example 2: Adding Splits and Extensions

<!-- tags: [Syncfusion Winforms, ConfigLexem, Language Lexems, Custom Formatting, API Reference, Code Examples, Editor] keywords: [ConfigLexem, FormatType.Custom, IsBeginRegex, IsEndRegex, ContinueBlock, IsContinueRegex, FormatName, Language.Lexems.Add, Language.Splits.Add, Language.Extensions.Add] -->
```