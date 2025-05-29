# msgraph-min

*A super-lightweight Microsoft Graph client generated with Kiota, trimmed to just the endpoints we use at Metaview.*

Endpoints included:
- `/me/events/{id}`
- `/me/calendar/calendarView`
- `/me/calendar/events`
- `/search/query`

---

## Why this repo exists

The official **microsoft-graph-python** SDK ships the entire Graph surface and weighs ~180 MB uncompressed—well over AWS Lambda’s 250 MB limit.  
`msgraph-min` is generated with **Kiota’s `--include-path`** filter so it contains **only the models & request-builders we need**, keeping deployment packages small enough.

---

## Regenerating / updating the client

Only needed when you adopt new Graph endpoints or want newer Kiota runtime versions.

1. Install Kiota CLI (once):
   - `brew install kiota`

2. Regenerate into `src/msgraph_min`:

   ```bash
   OPENAPI=https://aka.ms/graph/v1.0/openapi.yaml
   kiota generate \
     --language python \
     --class-name GraphServiceClient \
     --namespace-name msgraph_min \
     --openapi "$OPENAPI" \
     --include-path "/me/events/{event-id}" \
     --include-path "/me/calendar/calendarView" \
     --include-path "/me/calendar/events" \
     --include-path "/search/query" \
     --output src/msgraph_min \
     --clean-output \
     --exclude-backward-compatible
   ```

   Add more `--include-path` lines if you need new endpoints.

3. Update downstream `pyproject.toml` files with the new commit.