# SPACE-READ — hardening model

## Threat model

We assume that a public repository can receive hostile pull requests, malicious forks, compromised dependencies/actions, accidental owner changes, and compromised external AI agents.

The target is not an abstract promise of invulnerability. The target is a bounded blast radius:

`external compromise != Core compromise`

## Controls

1. **No reverse channel.** SPACE-READ contains no Core credential, Core write API, or publication command that accepts input from the public layer.
2. **Least privilege CI.** Workflows use read-only repository permissions.
3. **Immutable actions.** Every third-party GitHub Action must be pinned to a full commit SHA. GitHub documents SHA pinning as the immutable form of an Action reference. 
4. **No hostile workflow execution.** `pull_request_target` and `workflow_run` are forbidden in this public read-only repository.
5. **No public secrets.** CI must not consume repository secrets.
6. **No self-hosted runner.** Public contributions must never execute on infrastructure containing Core credentials or trusted network access.
7. **Code ownership.** Security-sensitive paths are assigned to the repository owner. This becomes an enforcement control when branch/ruleset requirements require CODEOWNERS approval.
8. **Adversarial regression.** Every boundary change is tested by malicious mutations in a temporary copy.
9. **Provenance.** Publications carry source, transformation, verification and publication metadata. This follows the general supply-chain principle that provenance should describe where and how an artifact was produced. See SLSA.
10. **Fail closed.** Unknown or weakened security conditions cause CI failure rather than being silently accepted.

## GitHub controls still requiring repository-owner configuration

The repository currently reports no GitHub rulesets. Therefore repository-side policy is not yet enforcing CODEOWNERS or protected-main requirements.

Required settings on the trusted repository boundary:

- protect `main`;
- require pull request before merge;
- require at least one owner review for security-sensitive paths;
- require the validation workflow to pass;
- dismiss stale approvals after new commits;
- restrict who may bypass the rules;
- prohibit force-push and deletion of `main`;
- require Actions to be pinned to full-length commit SHAs where the repository policy supports it.

These controls are deliberately separated from repository code because GitHub repository policy is a control-plane setting, not a file inside SPACE-READ.

## Supply-chain direction

The long-term target is a controlled publication pipeline:

`SPACE Core snapshot -> deterministic validation -> publication artifact -> signed/provenance record -> SPACE-READ`

The reverse direction is never part of the publication mechanism.

## Current boundary

SPACE-READ is public and therefore its files must be treated as untrusted input. The validator and CI must remain incapable of modifying SPACE Core. A fork, issue, pull request, or external AI proposal is not an accepted Core change.
