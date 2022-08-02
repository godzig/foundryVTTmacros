# foundryVTTmacros

Playing around with foundry macros.

## Release Process

To create a release, after committing to the main branch, create and push a
release tag with the version and description, e.g.

```
git tag -a v0.0.4 -m "Move script to database."
git push --tags

```

## Script Entry Overrides

Default database tags may be overridden with colon-separated key-value pairs
at the beginning of the script.  See `scripts/Twilight_Sanctuary.js` for an
example of this functionality.
