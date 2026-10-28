# Testing

Run these checks after installing the plugin and completing LogRocket OAuth. They require access to a LogRocket project with suitable recorded data. Judge each case on live results; do not substitute synthetic data.

The positive and negative cases submitted to OpenAI's review team live in `plugins/logrocket/plugin.json` under `extensions.com.openai.review`. Run those against the reviewer test account before each submission.

| Scenario | Expected behavior |
| --- | --- |
| Ask which LogRocket projects are available | Discovers organizations and projects with `list_organizations` and `list_projects`, and asks the user to choose when there are multiple candidates. Scoped connections omit these tools. |
| Investigate a session URL | Infers IDs from the URL, analyzes the session with `watch_sessions`, polls pending fingerprints, and cites returned session moments. |
| Retrieve only failed network requests from a session | Uses `get_network_entries` with status filters, pages through results as needed, and explains missing or truncated data. |
| Query a saved funnel metric over a concrete time range | Uses `get_metric` with the saved definition and an appropriate timezone, and fetches example drop-off sessions only when requested. |
| Triage severe untriaged issues from the last week | Uses `find_issues` with matching filters, uses inline issue analyses where present, and cites issue URLs. |
| Run a broad Galileo investigation | Uses `use_logrocket` when appropriate, keeps the `chatID`, and polls `thinking` responses through completion. |
| Request all issues over the past year | Explains the 30-day issue history limit rather than presenting clamped or empty results as a full year of coverage. |
| Ask to change issue triage or save a metric | Explains that the tools only query and analyze data, and does not claim an unsupported write succeeded. |
| Access an inaccessible project or hit an auth error | Reports the actual access failure and uses the host's connection flow without extracting or packaging credentials. |
