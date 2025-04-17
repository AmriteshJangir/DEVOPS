#!/bin/bash

# === CONFIGURATION ===
OWNER="your-github-username"
REPO="your-repo-name"
END_USER="collaborator-username"

# === PROTECT MAIN BRANCH ===
gh api \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  /repos/$OWNER/$REPO/branches/main/protection \
  -f enforce_admins=true \
  -f required_pull_request_reviews.dismiss_stale_reviews=true \
  -f required_pull_request_reviews.required_approving_review_count=1 \
  -f restrictions.users[]=$OWNER \
  -f restrictions.users[]=$END_USER \
  -f required_status_checks.strict=true \
  -f required_status_checks.contexts[]=ci \
  -f allow_force_pushes=false \
  -f allow_deletions=false

# === GRANT READ-ONLY ACCESS TO EVERYONE ELSE (OPTIONAL) ===
# You can add other users with pull access only (suggest-only)
# Example:
# gh api -X PUT -H "Accept: application/vnd.github+json" \
# /repos/$OWNER/$REPO/collaborators/readonly-user -f permission=pull

echo "✅ Main branch secured. Only $OWNER and $END_USER can push."
