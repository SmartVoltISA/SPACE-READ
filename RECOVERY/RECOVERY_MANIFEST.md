# SPACE-READ Recovery Manifest

This recovery point preserves the complete SPACE-READ project state at a known Git commit.

## Current point

- Branch: `recovery/space-read-2026-08-25`
- Snapshot source: `hardening/v0.2`
- Source commit: `36e279a2392e70a9c4373e5f0a56fa5a8b79f494`
- Recovery-anchor commit: recorded by Git after adding this manifest

## Recovery rule

Recover by exact Git commit/branch reference. Do not reconstruct the project from memory or disconnected files.

A recovery point is a historical reference, not a second Core and not an authorization channel.

## Verification

The snapshot is expected to contain the complete project tree inherited from the source commit. Future recovery points must record their exact SHA and verification result.

## Known limitation

This is a Git recovery snapshot, not an independent offline backup. A separate offline/exported backup should be maintained before treating recovery as disaster-proof.
