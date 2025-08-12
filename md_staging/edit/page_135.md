```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_135.jpeg
document_name: edit
page_number: 135
page_id: edit#page_135
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:12Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Demonstrates syntax highlighting in HTML with embedded JavaScript.
- Explains the feature's functionality and availability in a sample installation path.
- Provides references to related features and API documentation.

## Content

### Figure 44: Syntax Highlighting illustrated in HTML with Embedded JScript

```html
<a href="#ca" class="hide">
</a>
<div id="dPage" class="page">
<script language="javascript">
var hN = window.location.hostname.toLowerCase();
if (window.location.pathname == "/" && (hN == "www.microsoft.com" || hN == "home.microsoft.com" || hN == "redir.url.microsoft.com")) {
    var rs = '';
    var r = window.document.referrer;
    var TG = '<layer visibility="hide"><div style="display:none;">';

    if ('' != r) {
        TG += '&amp;r=' + escape(r);
    }

    TG += '" height="0" width="0" hspace="0" vspace="0" border="0"><img src="http://c1.microsoft.com/c.gif?DI=4050&amp;PS=3155;" alt=" ">';
    document.writeln(TG);
}
</script>
```

- **Description**: The above code snippet demonstrates the use of embedded JavaScript within HTML to implement dynamic behavior. The script checks the hostname and path to conditionally render elements based on certain criteria.

#### Sample Installation Path
- A sample demonstrating the above feature is available in the following path:
  ```
  ..\My Documents\Syncfusion\EssentialStudio\Version-Number\Windows\Edit.Windows\Samples\2.0\Syntax Highlighting_SyntaxColoringDemo
  ```

### See Also
- **Syntax Highlighting and Code Coloring**: XML Based Configuration Files (referenced in the document).

### 4.6 Runtime Features

The runtime features of the `Edit` control are as follows:

#### 4.6.1 Insert Mode

<!-- tags: Syncfusion, Windows Forms, Edit Control, Syntax Highlighting, Runtime Features, Insert Mode, Version 11.4.0.26 -->
```