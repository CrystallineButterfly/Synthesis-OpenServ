# Live readiness

- **Project:** OpenImpact Dispatcher
- **Track:** OpenServ
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:17+00:00`

## Trust boundaries

- **OpenServ** — `rest_json` — Dispatch jobs and expose swarm service endpoints.
- **Octant** — `rest_json` — Publish scored public-goods signals and DPI artifacts.
- **Filecoin** — `file_upload` — Persist proofs, logs, and evidence bundles offchain.
- **ERC-8004 Receipts** — `contract_call` — Anchor identity, task receipts, and reputation updates.
- **Olas** — `rest_json` — Hire and serve marketplace requests with receipts.
- **Uniswap** — `rest_json` — Quote swaps and bounded liquidity moves.
- **Markee** — `rest_json` — Publish GitHub-adjacent build stories and repo messages.

## Offline-ready partner paths

- **Filecoin** — prepared_filecoin_bundle
- **ERC-8004 Receipts** — prepared_contract_call

## Live-only partner blockers

- **OpenServ**: OPENSERV_API_KEY, OPENSERV_AGENT_URL — https://docs.openserv.ai/
- **Octant**: OCTANT_SIGNAL_URL — https://octant.app/
- **Olas**: OLAS_API_KEY, OLAS_REQUEST_URL — https://docs.olas.network/
- **Uniswap**: UNISWAP_API_KEY, UNISWAP_QUOTE_URL — https://developers.uniswap.org/
- **Markee**: MARKEE_API_KEY, MARKEE_MESSAGE_URL — https://markee.xyz/

## Highest-sensitivity actions

- `openserv_job_dispatch` — OpenServ — Use OpenServ for a bounded action in this repo.
- `octant_signal_publish` — Octant — Use Octant for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for OpenServJobBoard.
- Run python3 scripts/run_agent.py to produce a dry run for openimpact_dispatcher.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
