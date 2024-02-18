R3ND3R3R attempts to guess what glyph most closely approximates the pixels
rendered in a box. In order to do this, it needs to know what glyphs look like;
in other words, it needs a font. By default, it uses the [IBM VGA
font](https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_vga_8x16). Many
thanks to VileR at [The Ultimate Oldschool PC Font
Pack](https://int10h.org/oldschool-pc-fonts/) for the font itself. Then, to aid
parsing, we convert it to
[yaff](https://github.com/robhagemans/monobit/blob/master/YAFF.md) using the
lovely [monobit](https://github.com/robhagemans/monobit/) utility.

