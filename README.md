# OpenImpact Dispatcher

- **Repo:** `Synthesis-OpenServ`
- **Primary track:** OpenServ
- **Category:** orchestration
- **Submission status:** implementation ready, waiting for credentials and TxIDs.

A load-bearing service fabric for discovery, scheduling, execution receipts, and build-story outputs across the whole swarm.

## Selected concept

A coordinator exposes load-bearing service interfaces for discovery, scheduling, execution receipts, and build-story outputs. The contract layer stores job policies and completion receipts while Python workers route tasks to track-specific adapters.

## Idea shortlist

1. Autonomous Public-Goods Dispatch
2. x402 Agentic Service Hub
3. ERC-8004-backed DeFi Ops Queue

## Partners covered

OpenServ, Octant, Filecoin, ERC-8004 Receipts, Olas, Uniswap, Markee

## Architecture

```mermaid
flowchart TD
    Signals[Discover signals]
    Planner[Agent runtime]
    DryRun[Dry-run artifact]
    Contract[OpenServJobBoard policy contract]
    Verify[Verify and render submission]
    Signals --> Planner --> DryRun --> Contract --> Verify
    Contract --> openserv[OpenServ]
    Contract --> octant[Octant]
    Contract --> filecoin[Filecoin]
    Contract --> erc_8004_receipts[ERC-8004 Receipts]
    Contract --> olas[Olas]
    Contract --> uniswap[Uniswap]
```

## Repository layout

- `src/`: shared policy contracts plus the repo-specific wrapper contract.
- `script/`: Foundry deployment entrypoint.
- `agents/`: Python runtime, partner adapters, and project metadata.
- `scripts/`: CLI utilities for running the loop and rendering submissions.
- `docs/`: architecture, credentials, demo script, and security notes.
- `submissions/`: generated `synthesis.md` snippet for this repo.

## Action catalog

| Action | Partner | Purpose | Max USD | Sensitivity |
| --- | --- | --- | --- | --- |
| `openserv_job_dispatch` | OpenServ | Use OpenServ for a bounded action in this repo. | $10 | medium |
| `octant_signal_publish` | Octant | Use Octant for a bounded action in this repo. | $25 | medium |
| `filecoin_proof_store` | Filecoin | Use Filecoin for a bounded action in this repo. | $20 | medium |
| `erc_8004_receipts_receipt_anchor` | ERC-8004 Receipts | Use ERC-8004 Receipts for a bounded action in this repo. | $1 | medium |
| `olas_market_hire` | Olas | Use Olas for a bounded action in this repo. | $20 | medium |
| `uniswap_quote_route` | Uniswap | Use Uniswap for a bounded action in this repo. | $220 | medium |
| `markee_repo_message` | Markee | Use Markee for a bounded action in this repo. | $5 | low |

## Commands

```bash
python3 -m unittest discover -s tests
forge test
python3 scripts/run_agent.py
python3 scripts/plan_live_demo.py
python3 scripts/render_submission.py
```

## Credentials

| Partner | Variables | Docs |
| --- | --- | --- |
| OpenServ | OPENSERV_API_KEY, OPENSERV_AGENT_URL | https://docs.openserv.ai/ |
| Octant | OCTANT_SIGNAL_URL | https://octant.app/ |
| Filecoin | FILECOIN_API_TOKEN, FILECOIN_UPLOAD_URL | https://docs.filecoin.cloud/ |
| ERC-8004 Receipts | RPC_URL | https://eips.ethereum.org/EIPS/eip-8004 |
| Olas | OLAS_API_KEY, OLAS_REQUEST_URL | https://docs.olas.network/ |
| Uniswap | UNISWAP_API_KEY, UNISWAP_QUOTE_URL | https://developers.uniswap.org/ |
| Markee | MARKEE_API_KEY, MARKEE_MESSAGE_URL | https://markee.xyz/ |

## Live demo plan

1. Copy .env.example to .env and fill the required keys.
2. Deploy the contract with forge script script/Deploy.s.sol --broadcast for OpenServJobBoard.
3. Run python3 scripts/run_agent.py to produce a dry run for openimpact_dispatcher.
4. Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
5. Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
