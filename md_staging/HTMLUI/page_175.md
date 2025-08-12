```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_175.jpeg
document_name: HTMLUI
page_number: 175
page_id: HTMLUI#page_175
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:47Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

*Note:* The string entered inside the GetManifestResourceStream method is in reference to the Default namespace found in the Properties window of the C# file in the Solution Explorer. This may vary for the users.

## How To Print the Contents Of the HTMLUI Control?

The document available in the HTMLUI control can be printed with the help of the HTMLUIPrintDocument class. The Print method of this class is used to start the document printing process.

### C#

```csharp
// represents printing support in the HTMLUI control
HTMLUIPrintDocument pd;
pd = new HTMLUIPrintDocument(this.htmluiControl1.Document);

// starts the printing process
pd.Print();
```

### VB.NET

```vbnet
' represents printing support in the HTMLUI control
Private pd As HTMLUIPrintDocument
Private pd = New HTMLUIPrintDocument(Me.HtmluiControl1.Document)

' Starts the printing process
pd.Print()
```

## How To Specify a CSS File For HTML Content?

Style sheets contain the styles to be applied for the elements in the HTML document. HTMLUI supports the use of styles in three modes:

- Inline style sheet (inside an HTML element)
- Internal style sheet (inside the tag)
- External style sheet (as a separate file)

The HTMLUI control supports formatting the HTML document with style sheets at run time. The LoadCSS method of the HTMLUI control loads the styles from the specified CSS and refreshes the current document on the HTMLUI control with the applied styles.

### C#

```csharp
```

```markdown
## Overview
- 1-3 bullets summarizing the page scope using only visible text.

## Content
- The document available in the HTMLUI control can be printed using the HTMLUIPrintDocument class.
- Style sheets can be specified for HTML content using three modes: inline, internal, and external.
- The LoadCSS method is used to apply styles from a specified CSS file.

### How To Print the Contents Of the HTMLUI Control?

#### Printing the HTMLUI Document
The process of printing the contents of the HTMLUI control involves:

1. Creating an instance of the HTMLUIPrintDocument class.
2. Assigning the document to be printed to this instance.
3. Calling the Print method to start the printing process.

#### Example in C#

```csharp
// HTMLUIPrintDocument is used to represent printing support
HTMLUIPrintDocument pd;
pd = new HTMLUIPrintDocument(this.htmluiControl1.Document);
pd.Print();
```

#### Example in VB.NET

```vbnet
' HTMLUIPrintDocument is used to represent printing support
Private pd As HTMLUIPrintDocument
Private pd = New HTMLUIPrintDocument(Me.HtmluiControl1.Document)
pd.Print()
```

### How To Specify a CSS File For HTML Content?

#### CSS Modes Supported
- **Inline Style Sheet:** Styles are applied directly within an HTML element.
- **Internal Style Sheet:** Styles are placed inside the tag of the HTML document.
- **External Style Sheet:** Styles are defined in a separate CSS file.

#### Applying CSS Using LoadCSS
The LoadCSS method loads the styles from a specified CSS file and refreshes the current HTMLUI control with the applied styles.

#### Example in C#

```csharp
// Example usage of LoadCSS method (to be completed with specific implementation details)
```

## API Reference

- **HTMLUIPrintDocument Class**
  - **Methods**
    - Print(): Starts the printing process for the HTMLUI document.

- **HTMLUI Control**
  - **Methods**
    - LoadCSS(string cssFilePath): Loads and applies the specified CSS file to the HTMLUI document.

## Code Examples

#### Printing Example

**C#**
```csharp
HTMLUIPrintDocument pd;
pd = new HTMLUIPrintDocument(this.htmluiControl1.Document);
pd.Print();
```

**VB.NET**
```vbnet
Private pd As HTMLUIPrintDocument
Private pd = New HTMLUIPrintDocument(Me.HtmluiControl1.Document)
pd.Print()
```

### CSS Application Example

**C#**
```csharp
// Example usage of LoadCSS method (to be completed with specific implementation details)
```

## Cross References

- See also: [HTMLUI Control Reference](#htmlui-control-reference)
- See also: [Printing and Exporting in HTMLUI](#printing-and-exporting)

<!-- tags: Syncfusion, HTMLUI, Windows Forms, Printing, CSS, HTMLUI Control, External Style Sheet, Internal Style Sheet, Inline Style Sheet, LoadCSS, Print Method, VB.NET, C# -->
```