# auto-simulacrum / socratic-sync

Instagram post automation for https://www.instagram.com/simulacro.psi/

## Contains

-   src in en (when available)
-   src in pt-BR
-   img src

-   automation
    -   image generation
    -   post scheduling
-   request that gets a random post
    -   post it to stories

## current

-   ime (tem pt)
-   cis (tem pt)

## upcoming

-   beer
-   hacking
-   grunbaum
-   ose
-   fig
-   figlou
-   cr
-   musgrave

## possibly

-   dunker
-   wpf
-   never been modern
-   graeber
-   pasternak & pilati
-   gattei

## done

-   ...

## References

-   instagram api

    -   https://levelup.gitconnected.com/automating-instagram-posts-with-python-and-instagram-graph-api-374f084b9f2b
    -   https://skolo.online/documents/instagram/#pre-requisites-for-instagram-automation
    -   https://developers.facebook.com/docs/instagram-api/
    -   https://developers.facebook.com/docs/instagram-basic-display-api
    -   https://developers.facebook.com/docs/instagram-api/guides/content-publishing/
    -   https://developers.facebook.com/blog/post/2021/01/26/introducing-instagram-content-publishing-api/
    -   https://aphrx.medium.com/automating-social-media-posts-with-python-instagram-graph-api-b9bd81eac5c
    -   https://igsumo.com/

-   image generation
    -   https://www.analyticsvidhya.com/blog/2021/05/automate-your-image-processing-using-python/
    -   https://towardsdatascience.com/automate-graphic-design-using-python-e161bce62cfe
    -   https://neptune.ai/blog/image-processing-python
    -   https://www.youtube.com/watch?v=D6Qo0YAvuQM
    -   https://playwright.dev/python/docs/intro
    -   https://oxylabs.io/blog/playwright-web-scraping
    -   https://www.browserstack.com/guide/playwright-tutorial

## using prepare_data

-   files must be named correctly (by page number with duplicates for each additional image per post. max 10)
-   set them in the folder called `data-src/raw/{BOOK_NAME}`
-   set constants in prepare_data
-   it will make a folder for each post in `data-src/ordered/{BOOK_NAME}`, which can now be iterated by the main script
