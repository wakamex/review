#!/bin/bash
# Deploy the /review/ page on mihaicosma.com.
#
# Source:  ./site/{index.html,paper.html,style.css}
# Target:  mc-new:/var/www/mihaicosma.com/review/
#
# At deploy time the HTML's __DATA_SHA__ placeholder is substituted with the
# current commit SHA, so the jsDelivr URL becomes
#   https://cdn.jsdelivr.net/gh/wakamex/review@<sha>/...
# instead of @main. Commit-pinned URLs are never cached stale: each commit
# is a fresh cache key on the edge, so the live site always sees the data
# it was deployed against. Cost: every data update needs a redeploy.
#
# Requires that HEAD has been pushed to origin/main, since jsDelivr fetches
# from GitHub and 404s on unknown SHAs.

set -euo pipefail

REPO_DIR="$(dirname "$(realpath "$0")")"
SITE_DIR="$REPO_DIR/site"
ZONE="us-central1-a"
HOST="mc-new"
TARGET_DIR="/var/www/mihaicosma.com/review"
FILES=(index.html paper.html style.css)

# --- sanity checks -----------------------------------------------------------

for f in "${FILES[@]}"; do
    if [ ! -f "$SITE_DIR/$f" ]; then
        echo "ERROR: $SITE_DIR/$f not found — nothing to deploy" >&2
        exit 1
    fi
done

cd "$REPO_DIR"

SHA="$(git rev-parse HEAD)"
SHORT_SHA="$(git rev-parse --short=12 HEAD)"

# Make sure the commit we're pinning to has actually been pushed — otherwise
# jsDelivr won't be able to fetch the data and the live site will 404 every
# JSON file.
echo "→ checking that $SHORT_SHA is on origin/main"
git fetch --quiet origin main
REMOTE_SHA="$(git rev-parse origin/main)"
if [ "$SHA" != "$REMOTE_SHA" ]; then
    echo "ERROR: HEAD ($SHORT_SHA) does not match origin/main ($(git rev-parse --short=12 origin/main))." >&2
    echo "       Push first, then redeploy — otherwise jsDelivr can't fetch this SHA." >&2
    exit 1
fi

# --- stage with SHA substitution --------------------------------------------

STAGE="$(mktemp -d -t review-deploy.XXXXXX)"
trap 'rm -rf "$STAGE"' EXIT

cp "${FILES[@]/#/$SITE_DIR/}" "$STAGE/"

# style.css has no placeholder, but pin the HTML files to the current SHA.
sed -i "s/__DATA_SHA__/$SHORT_SHA/g" "$STAGE/index.html" "$STAGE/paper.html"

# Sanity: confirm no stragglers were left unsubstituted.
if grep -q "__DATA_SHA__" "$STAGE"/*.html; then
    echo "ERROR: __DATA_SHA__ placeholder still present after sed — bailing." >&2
    grep -n "__DATA_SHA__" "$STAGE"/*.html >&2 || true
    exit 1
fi

echo "→ pinned HTML to gh/wakamex/review@$SHORT_SHA"

# --- scp + install -----------------------------------------------------------

REMOTE_STAGE="review-site.$$.$(date +%s)"

echo "→ scp staged files → $HOST:~/$REMOTE_STAGE/"
gcloud compute ssh "$HOST" --zone="$ZONE" --command="mkdir -p ~/$REMOTE_STAGE"
gcloud compute scp \
    "${FILES[@]/#/$STAGE/}" \
    "$HOST:~/$REMOTE_STAGE/" \
    --zone="$ZONE"

echo "→ ssh install to $TARGET_DIR/"
gcloud compute ssh "$HOST" --zone="$ZONE" --command="\
    sudo mkdir -p '$TARGET_DIR' && \
    sudo mv ~/'$REMOTE_STAGE'/index.html '$TARGET_DIR/index.html' && \
    sudo mv ~/'$REMOTE_STAGE'/paper.html '$TARGET_DIR/paper.html' && \
    sudo mv ~/'$REMOTE_STAGE'/style.css  '$TARGET_DIR/style.css'  && \
    rmdir ~/'$REMOTE_STAGE' && \
    sudo chown -R root:www-data '$TARGET_DIR' 2>/dev/null || true && \
    sudo chmod 755 '$TARGET_DIR' && \
    sudo chmod 644 '$TARGET_DIR'/*"

echo "✓ deployed → https://mihaicosma.com/review/  (data pinned to @$SHORT_SHA)"
