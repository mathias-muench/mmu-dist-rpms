---
name: copr
description: Add RPM spec files to COPR (Fedora COPR build system)
user-invocable: true
allowed-tools: bash grep read_file
---

# COPR Skill: Adding RPM Spec Files to Fedora COPR

This skill helps you add new RPM spec files to an existing COPR project on copr.fedorainfracloud.org.

## Prerequisites

1. **COPR Account**: Fedora Account System (FAS) account
2. **copr-cli**: Installed and configured with API token at `~/.config/copr`
3. **GitHub Repo**: Your spec files in a GitHub repository
4. **Project**: Existing COPR project with `.copr/Makefile`

## Setup copr-cli (one-time)

Get API token from https://copr.fedorainfracloud.org/api/ and configure:

```bash
mkdir -p ~/.config
cat > ~/.config/copr <<EOF
[copr-cli]
username = YOUR_FAS_USERNAME
token = YOUR_API_TOKEN
copr_url = https://copr.fedorainfracloud.org
EOF
chmod 600 ~/.config/copr
```

Verify with: `copr-cli whoami`

## Add Package to COPR

For SCM-based projects using `.copr/Makefile`:

```bash
copr-cli add-package-scm PROJECT_NAME \
  --clone-url https://github.com/USERNAME/REPO \
  --name PACKAGE_NAME \
  --spec PACKAGE.spec \
  --method make_srpm \
  --webhook-rebuild on
```

**Example:**
```bash
copr-cli add-package-scm mmu-dist-rpms \
  --clone-url https://github.com/mathias-muench/mmu-dist-rpms \
  --name opencode-dist \
  --spec opencode-dist.spec \
  --method make_srpm \
  --webhook-rebuild on
```

## Common Commands

| Command | Description |
|---------|-------------|
| `copr-cli whoami` | Verify authentication |
| `copr-cli list-packages PROJECT` | List packages |
| `copr-cli add-package-scm PROJECT --name NAME --spec FILE.spec --clone-url URL --webhook-rebuild on` | Add SCM package with auto-rebuild |
| `copr-cli edit-package-scm PROJECT --name NAME --webhook-rebuild on/off` | Enable/disable auto-rebuild on existing package |
| `copr-cli list-packages PROJECT` | List packages with JSON config (shows `auto_rebuild`) |
| `copr-cli build PROJECT SRPM_FILE` | Build from SRPM |
| `copr-cli list-builds PROJECT` | View builds |

## Manage Package Config

Check existing package configuration (JSON output includes `auto_rebuild` flag):

```bash
copr-cli list-packages mmu-dist-rpms
```

Enable or disable automatic rebuilds on push for an existing package:

```bash
copr-cli edit-package-scm mmu-dist-rpms --name opencode-dist --webhook-rebuild on
copr-cli edit-package-scm mmu-dist-rpms --name opencode-dist --webhook-rebuild off
```

## Verify Builds

List recent builds and their status:

```bash
copr-cli list-builds mmu-dist-rpms
```

Check the exact version-release that was built (useful to confirm spec changes deployed):

```bash
curl -s https://copr.fedorainfracloud.org/api_3/build/BUILD_ID | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['source']['version'])"
```

Compare local spec versions against latest COPR builds:

```bash
for spec in *.spec; do
  pkg="${spec%.spec}"
  ver=$(grep '^Version:' "$spec" | awk '{print $2}')
  rel=$(grep '^Release:' "$spec" | awk '{print $2}' | sed 's/%{?dist}//')
  echo "$pkg: $ver-$rel"
done
```

## Troubleshooting

**ModuleNotFoundError: No module named 'rich'**
```bash
pip install --user rich
```

**"Project not found"**
- Verify project name format: `username/projectname`
- Check permissions on the project

## Example Workflow

```bash
# 1. Create spec
vim opencode-dist.spec

# 2. Test locally
rpmbuild -bb opencode-dist.spec

# 3. Add to COPR
copr-cli add-package-scm mmu-dist-rpms \
  --clone-url https://github.com/mathias-muench/mmu-dist-rpms \
  --name opencode-dist \
  --spec opencode-dist.spec \
  --method make_srpm \
  --webhook-rebuild on

# 4. Commit and push
git add opencode-dist.spec && git commit && git push

# 5. COPR auto-builds (if webhook-rebuild is on)
```

## References

- COPR Docs: https://docs.pagure.org/copr.copr/
- COPR Web: https://copr.fedorainfracloud.org/
