# autosimulacrum / socratic-sync

https://www.youtube.com/watch?v=NI5IGAim8XU
https://www.youtube.com/watch?v=6tNS--WetLI
https://www.youtube.com/watch?v=mzlH8lp4ISA

Utilities for doing work for https://www.instagram.com/simulacro.psi/, such as post automation, data cleanup, file organization, etc.

## Workflow

1. read book. mark book. check quality of ocr. remark book with desired quotations.
1. extract annotations from pdf
    - try python
1. cleanup quotes (`quote_cleanup`)
1. convert to docx
1. translate (google) (also fixes worst extraction errors)
    - try gpt
1. fix extraction errors (gpt3.5) (1 cent per 40k chars)
1. manually check translation. manually fix things.
1. make images. download images. organize images. (`organize_images`)
1. make buffer post.

## how to use

### data structure

-   create a folder at the root of this project. it should look like this:

    -   data
        -   {book_name}
            -   text
            -   {put text here}
            -   img
                -   raw
                -   {put unordered images here}

### using `quote_cleanup`

-   fitted to deal with output from obsidian
-   run
-   outputs a `{book}2.md` file for further processing

### using `organize_images`

-   files must be named correctly as per canva workflow (by page number with duplicates for each additional image per post. maximum 10 images per post because of instagram limitations). see `test` for example.
-   put images in the folder `{book}/img/raw`
-   run
-   it will make a folder for each post in `{book}/img/ordered`, which can now be iterated on by the main script

## current

-   ime pt2
-   cis pt2
-   ose
    -   continue from 566

## upcoming

-   beer (pt)
-   hacking (en)
-   grunbaum (en)
-   ose (en)
-   fig (pt)
-   figlou (pt)
-   cr (en)
-   musgrave (en)

## possibly

-   dunker
-   wpf
-   never been modern
-   graeber
-   pasternak & pilati
-   gattei
