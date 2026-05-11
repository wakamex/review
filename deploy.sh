#!/bin/bash
# Deploy the /review/ page on mihaicosma.com.
#
# Source:  ./site/{index.html,paper.html,style.css}
# Target:  mc-new:/var/www/mihaicosma.com/review/
#
# Only the /review/ subfolder of the live site is touched. The JSON data
# (teasers, board summaries, reviewer cycles) is served from jsDelivr,
# pointing at github.com/wakamex/review@main — so this script handles
# only the page itself. Push to github to refresh the data.

set -euo pipefail

SITE_DIR="$(dirname "$(realpath "$0")")/site"
ZONE="us-central1-a"
HOST="mc-new"
TARGET_DIR="/var/www/mihaicosma.com/review"

for f in index.html paper.html style.css; do
    if [ ! -f "$SITE_DIR/$f" ]; then
        echo "ERROR: $SITE_DIR/$f not found — nothing to deploy" >&2
        exit 1
    fi
done

STAGE_DIR="$(mktemp -u review-site.XXXXXX)"

echo "→ scp  $SITE_DIR/{index,paper}.html style.css → $HOST:~/$STAGE_DIR/"
gcloud compute ssh "$HOST" --zone="$ZONE" --command="mkdir -p ~/$STAGE_DIR"
gcloud compute scp \
    "$SITE_DIR/index.html" \
    "$SITE_DIR/paper.html" \
    "$SITE_DIR/style.css" \
    "$HOST:~/$STAGE_DIR/" \
    --zone="$ZONE"

echo "→ ssh  install to $TARGET_DIR/"
gcloud compute ssh "$HOST" --zone="$ZONE" --command="\
    sudo mkdir -p '$TARGET_DIR' && \
    sudo mv ~/'$STAGE_DIR'/index.html '$TARGET_DIR/index.html' && \
    sudo mv ~/'$STAGE_DIR'/paper.html '$TARGET_DIR/paper.html' && \
    sudo mv ~/'$STAGE_DIR'/style.css  '$TARGET_DIR/style.css'  && \
    rmdir ~/'$STAGE_DIR' && \
    sudo chown -R root:www-data '$TARGET_DIR' 2>/dev/null || true && \
    sudo chmod 755 '$TARGET_DIR' && \
    sudo chmod 644 '$TARGET_DIR'/*"

echo "✓ deployed → https://mihaicosma.com/review/"
