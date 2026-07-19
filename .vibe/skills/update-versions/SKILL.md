---
name: update-versions
description: Update the versions od dist rpms to the latest upstream release
---

# Update Versions

Updates the versions od dist rpms to the latest upstream release.

## When to use this skill

Binaries in upstream (mostly github artifacts) have new releases and the user wants to use them via yum/dnf.

## Workflow

1. **Find all latest release pages** in the URL fields of all rpm spec files.

2. **Update the version field in all rpm spec files accordingly**

3. **Verfiy rpm spec files** are still syntactically correct.

## Notes / conventions to respect

- Do not reset releases. They track the versions of the rpm spec file independently.
