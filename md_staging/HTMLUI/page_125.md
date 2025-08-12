```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_125.jpeg
document_name: HTMLUI
page_number: 125
page_id: HTMLUI#page_125
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:10:05Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```html
<table border="1">
  <tr>
    <td>This is a table.</td>
  </tr>
</table>
<br />
```

```html
<table class="table" border="1">
  <tr>
    <td>This is another table.</td>
  </tr>
</table>
</body>
</html>
```

## Border Width

- **border-width**: Specifies the thickness for the border of the rendered table. The user can specify the border-width in units.
- **border-bottom-width**: Specifies the thickness for the bottom border of the rendered table
- **border-top-width**: Specifies the thickness for the top border of the rendered table
- **border-left-width**: Specifies the thickness for the left border of the rendered table
- **border-right-width**: Specifies the thickness for the right border of the rendered table

```html
[HTML]
<html>
  <head>
    <style>
      .table {
        border-width: 5;
      }
      table {
        border-left-width: 3;
        border-right-width: 5;
        border-top-width: 6;
        border-bottom-width: 8;
      }
    </style>
  </head>
  <body>
    <table border="1">
      <tr>
        <td>This is a table.</td>
      </tr>
    </table>
    <br />
    ```html
    <table class="table" border="1">
      <tr>
        <td>This is another table.</td>
      </tr>
    </table>
    ```html 
    </body>
</html>
```

## Padding – CSS

The CSS `padding` attribute in HTMLUI is used to define a fixed space between the element's border and its contents. The top, right, bottom, and left padding attributes can be specified independently.

```html
[HTML]
<html>
  <head>
    <style>
      .table {
        padding: 5;
      }
      table {
        padding-left: 25;
        padding-right: 50;
        padding-top: 25;
        padding-bottom: 50;
      }
    </style>
  </head>
  <body>
    ```html
    <table border="1">
      <tr>
        <td>This is a table.</td>
      </tr>
    </table>
    <br />
    ```html 
    <table class="table" border="1">
      <tr>
        <td>This is another table.</td>
      </tr>
    </table>
    ```html 
    </body>
</html>
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

<!-- tags: [HTMLUI, Windows Forms, Border Width, Padding, CSS] keywords: [Table, Border, Padding, CSS Attributes, HTML, Style, Example] -->
``` 
